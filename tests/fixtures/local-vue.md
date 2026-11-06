# Contexto fornecido

Pacote Vue 3.4.38 com Composition API e TypeScript. Estado visual simples permanece no componente; não há store compartilhada ou evidência de gargalo. Escopo: somente este componente, sem edição. Os números de linha, quando usados, são locais ao bloco.

```vue
<script setup lang="ts">
import { computed, ref } from 'vue';
const open = ref(false);
const label = computed(() => open.value ? 'Ocultar detalhes' : 'Mostrar detalhes');
</script>

<template>
  <section>
    <button :aria-expanded="open" @click="open = !open">{{ label }}</button>
    <p v-if="open">Detalhes do produto</p>
  </section>
</template>
```
