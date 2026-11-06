"""Optional native discovery probe; does not request a model turn.

Uses existing Codex configuration. The app-server protocol is experimental.
"""
import json
import queue
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / '.agents' / 'skills' / 'frontscope' / 'SKILL.md'


def probe():
    binary = shutil.which('codex')
    if not binary:
        print('BLOCKED: codex executable not found. Nothing was installed.')
        return 2
    process = subprocess.Popen(
        [binary, 'app-server', '--stdio'], cwd=ROOT,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        text=True, encoding='utf-8',
    )
    messages = queue.Queue()

    def read_messages():
        for line in process.stdout:
            try:
                messages.put(json.loads(line))
            except ValueError:
                continue

    threading.Thread(target=read_messages, daemon=True).start()

    def send(payload):
        process.stdin.write(json.dumps(payload) + '\n')
        process.stdin.flush()

    def response(request_id):
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            item = messages.get(timeout=max(0.1, deadline - time.monotonic()))
            if item.get('id') == request_id:
                if 'error' in item:
                    raise RuntimeError('Request rejected by the app-server.')
                return item['result']
        raise TimeoutError('No response from the app-server.')

    def find_skill(item):
        if isinstance(item, dict):
            if (item.get('name') == 'frontscope' and
                    Path(item.get('path', '')).resolve() == EXPECTED.resolve()):
                return item
            for value in item.values():
                found = find_skill(value)
                if found:
                    return found
        elif isinstance(item, list):
            for value in item:
                found = find_skill(value)
                if found:
                    return found
        return None

    try:
        send({'id': 1, 'method': 'initialize', 'params': {
            'clientInfo': {'name': 'frontscope-validation', 'version': '0.1.0'},
            'capabilities': {'experimentalApi': True},
        }})
        response(1)
        send({'method': 'initialized', 'params': {}})
        send({'id': 2, 'method': 'skills/list', 'params': {
            'cwds': [str(ROOT)], 'forceReload': True,
        }})
        found = find_skill(response(2))
        if not found or found.get('enabled') is not True:
            print('FAILED: FrontScope from this repository was not found enabled.')
            return 1
        print(json.dumps({key: found.get(key) for key in ('name', 'path', 'scope', 'enabled')}, ensure_ascii=False))
        print('OK: native discovery; no model turn requested. Workflow execution not evaluated.')
        return 0
    except (queue.Empty, TimeoutError, RuntimeError, OSError) as error:
        print(f'BLOCKED: discovery not completed ({type(error).__name__}).')
        return 2
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)
        process.stdin.close()
        process.stdout.close()


if __name__ == '__main__':
    sys.exit(probe())
