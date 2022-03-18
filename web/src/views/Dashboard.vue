<template>
<form>
  <v-container>
    <label for="something">Something</label>
    <input ref="input" type="text" name="something" style="border: 2px solid black; border-radius: 6px;" />
  </v-container>

  <v-container>
    <v-form v-model="valid" ref="form" lazy-validation>
      <v-text-field></v-text-field>
      <v-btn>Submit</v-btn>
    </v-form>
  </v-container>
</form>
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

    return {
      input,
      form,
      valid
    }
  },
}
</script>
