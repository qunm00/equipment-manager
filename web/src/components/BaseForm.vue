<template>
<v-container>
  <v-card>
    <v-card-title>
      <slot name="title"/>
    </v-card-title>

    <!-- <v-form
      @submit="onSubmit"
      ref="formRef"
      v-model="valid"
    > -->
    <v-form
      @submit="onSubmit"
    >
      <v-container>
        <v-row>
          <slot name="formFields" />
        </v-row>

        <v-row>
          <v-spacer></v-spacer>
          <v-col cols="4">
            <v-btn type="submit">Submit</v-btn>
          </v-col>
          <v-col cols="4">
            <v-btn @click="$emit('closeDialog')">Cancel</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>
</v-container>
</template>

<script setup>
// const props = defineProps(['valid', 'formRef'])
const emits = defineEmits(['submitForm', 'closeDialog'])

const onSubmit = () => {
  emits('submitForm')
}
</script>

<style scoped>
:deep(.v-input__details) {
  margin-bottom: 0;
}
</style>