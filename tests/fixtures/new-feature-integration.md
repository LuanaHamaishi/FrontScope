# New feature crossing UI and API boundaries

Synthetic Vue feature package. The user requests an invitation form: submit an email, call the existing invitation API client, and show the returned invitation in the list. API validation failure must display the server message without adding an item; pending state prevents duplicate submissions. Source and relevant tests are within normal implementation scope. No separate authorization is needed for this test work; commits, dependency installation, and production access are outside scope.

Existing project conventions: pure validators have unit tests; component/API flows use Vitest and Vue Test Utils integration tests with a synthetic HTTP boundary. Tooling is already present. The real API client and list update should participate in that integration test; mocking the entire client/form/list interaction would hide the requested integration. No E2E suite exists and there is no requirement to introduce one.

The request is to plan implementation and validation from this supplied profile, not modify or run an application that has not been provided. The agent should choose coverage for successful submission, API error, and pending/duplicate behavior, explain boundaries and observable assertions, and retain existing tests. It should not refuse to create tests because the behavior is new or make an E2E platform mandatory.
