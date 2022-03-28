<template>
<v-alert
  v-model="displayAlert"
  closable
  prominent
  type="error"
>
  {{ validationMessage }}
</v-alert>
<v-container
>
  <v-card>

    <v-card-title>
      {{ cardTitle }}
    </v-card-title>
    <v-form
      @submit="onSubmit" 
      ref="formRef" 
      v-model="valid"
    >
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-checkbox 
              label="Active" 
              v-model="employeeData.activestatus"
            ></v-checkbox>
          </v-col>
          <v-col cols="12">
            <v-text-field 
              label="Nickname" 
              v-model="employeeData.nickname"
              :rules="[v => !!v || 'Nickname is required']"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field 
              label="Full name"
              v-model="employeeData.fullname"
              :rules="[v => !!v || 'Fullname is required']"
              required
          ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field 
              label="Mobile" 
              v-model="employeeData.mobile"
              :rules="[v => /[0-9]{9,10}/.test(v) || 'Mobile number must be 9 or 10 digits']"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field 
              label="Email" 
              :rules="[v => /.+@.+\..+/.test(v) || 'Email must be formatted like examplel@mail.com']"
              v-model="employeeData.email"
            ></v-text-field>
          </v-col>
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

<script>
import { onMounted, ref } from 'vue'
import { createEmployee, editEmployee } from './employee'

export default {
  props: ['employee', 'cardTitle'],
  emits: ['closeDialog', 'eventSubmitEmployeeForm'],

  setup(props, context) {
    const employeeData = ref({})
    const valid = ref(false)
    const formRef = ref(null)
    const displayAlert = ref(false)
    const validationMessage = ref('')

    onMounted(() => {
      setData()
    })

    const onSubmit = async () => {
      try {
        if (employeeData.value.id === undefined) {
          await createEmployee(employeeData.value)
        } else {
          await editEmployee(props.employee.id, employeeData.value)
        }
        context.emit('closeDialog')
        context.emit('eventSubmitEmployeeForm')
      } catch (error) {
        validationMessage.value = (await error.json()).detail
        displayAlert.value = true 
        setTimeout(() => { 
          displayAlert.value = false
          setData()
        }, 2000)
      }
    }

    const setData = () => {
      const incomingData = Object.assign({}, props.employee)
      if (incomingData.id === undefined) {
        employeeData.value = {
          'activestatus': true
        }
      } else {
        employeeData.value = {
          ...incomingData
        }
      }
    }

    return {
      employeeData,
      onSubmit,
      formRef,
      valid,
      displayAlert,
      validationMessage
    }
  },
}
</script>

<style scoped>
:deep(.v-input__details) {
  margin-bottom: 0;
}
</style>