<template>
<v-card>
  <slot></slot>
  <v-card-actions>
    <v-spacer></v-spacer>
    <v-btn @click="emits('confirmDelete')">Yes</v-btn>
    <v-btn @click="emits('closeDeleteDialog')">No</v-btn>
  </v-card-actions>
</v-card>
</template>

<script setup>
const emits = defineEmits(['closeDeleteDialog', 'confirmDelete'])
</script>