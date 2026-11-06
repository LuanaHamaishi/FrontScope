# Supplied context

Vue 3.4.38 package with Composition API and TypeScript. Simple visual state remains in the component; there is no shared store or evidence of a bottleneck. Scope: this component only, without editing. Any line references are local to the block.

```vue
<script setup lang="ts">
import { computed, ref } from 'vue';
const open = ref(false);
const label = computed(() => open.value ? 'Hide details' : 'Show details');
</script>

<template>
  <section>
    <button :aria-expanded="open" @click="open = !open">{{ label }}</button>
    <p v-if="open">Product details</p>
  </section>
</template>
```
