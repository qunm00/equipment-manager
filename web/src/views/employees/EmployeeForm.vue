<template>
<Alert :displayAlert="displayAlert">
  {{ validationMessage }}
</Alert>

<BaseForm
  @submitForm="onSubmit"
  @closeDialog="$emit('closeDialog')"
>
  <template #title>
    {{ cardTitle }}
  </template>

  <template #formFields>
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
  </template>
</BaseForm>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import Alert from '../../components/Alert.vue';
import BaseForm from '../../components/BaseForm.vue';
import { createEmployee, editEmployee } from './employee'

const props = defineProps(['employee', 'cardTitle'])
const emits = defineEmits(['closeDialog', 'eventSubmitEmployeeForm'])

const employeeData = ref({'activestatus': true})
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
    emits('closeDialog')
    emits('eventSubmitEmployeeForm')
  } catch (error) {
    validationMessage.value = (await error.json()).detail
    displayAlert.value = true 
    setTimeout(() => { 
      displayAlert.value = false
    }, 2000)
  }
}

const setData = () => {
  const incomingData = Object.assign({}, props.employee)
  if (incomingData.id !== undefined) {
    employeeData.value = {
      ...incomingData
    }
  }
}
</script>