<template>
<form>
  <v-container>
    <label for="something">Something</label>
    <input ref="input" type="text" name="something" style="border: 2px solid black; border-radius: 6px;" />
  </v-container>

  <v-container>
    <v-form v-model="valid" ref="form" lazy-validation>
      <v-text-field></v-text-field>
      <v-btn prepend-icon="mdi-account-group">Submit</v-btn>
    </v-form>
  </v-container>
</form>
<div class="text-center ma-2">
  <v-btn
    @click="openAlert"
  >
    Open Alert
  </v-btn>
</div>
</template>

<script>
import { onMounted, ref } from 'vue'

export default {
  setup() {
    const input = ref(null)
    const form = ref(null)
    const valid = ref(false)

    onMounted(() => {
      input.value.focus()
      console.log(form.value)
    })

    const openAlert = () => {
      alert('Something')
    }

    return {
      input,
      form,
      valid,
      openAlert
    }
  },
}
</script>
