<template>
<v-alert
  v-model="displayAlert"
  closeable
  type="error"
>
  <slot></slot>
</v-alert>
</template>

<script setup>
const props = defineProps(['displayAlert'])
</script>