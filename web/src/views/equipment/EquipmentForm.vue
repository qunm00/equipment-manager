<template>
<Alert v-model="displayAlert">
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
      <v-text-field
        label="Device name"
        v-model="deviceData.name"
        :rules="[v => !!v || 'Device name is required!']"
        required
      ></v-text-field>
    </v-col>
  
    <v-col cols="10">
      <v-select
        :items="categories"
        label="Device category"
        v-model="selectedCategory"
        :rules="[v => !!v || 'Device category is required!']"
        required
      ></v-select>
    </v-col>
    <v-col>
      <v-btn 
        icon="mdi-plus"
        @click="$emit('openAddCategory')"
      ></v-btn>
    </v-col>
  
    <v-col cols="12">
      <v-text-field
        label="Serial number"
        v-model="deviceData.serialnumber"
        :rules="[v => !!v || 'Device serial number is required!']"
        required
      ></v-text-field>
    </v-col>
  
    <v-col cols="12">
      <v-select
        :items="employees"
        label="Borrower"
        v-model="selectedEmployee"
      ></v-select>
    </v-col>
  </template>
</BaseForm>
</template>

<script setup>
import { onMounted, ref } from 'vue'

import Alert from '../../components/Alert.vue';
import BaseForm from '../../components/BaseForm.vue';

import { 
  createDevice, 
  editDevice, 

} from './equipment'

import {
  getCategoryByName
} from './category'

import {
  getEmployeeByName
} from '../employees/employee'

const props = defineProps([
  'device', 
  'categories', 
  'employees', 
  'cardTitle',
  'fetchedCategories',
  'fetchedEmployees'
])

const emits = defineEmits([
  'closeDialog', 
  'openAddCategory', 
  'eventSubmitDeviceForm'
])

const validationMessage = ref(null)
const displayAlert = ref(false)

const deviceData = ref({})

const selectedCategory = ref(null)
const selectedEmployee = ref(undefined)

onMounted(() => {
  setData()
})

const onSubmit = async () => {
  const categoryID = (await getCategoryByName(selectedCategory.value)).id
  const employeeID = selectedEmployee.value === undefined 
    ? undefined 
    : (await getEmployeeByName(selectedEmployee.value)).id

  let payload = {
    ...deviceData.value,
    'category': parseInt(categoryID)
  }

  if (employeeID !== undefined) {
    payload = {...payload, 'employee': parseInt(employeeID)}
  } else {
    delete payload.employee
  }

  try {
    if (deviceData.value.id === undefined) {
      await createDevice(payload)
    } else {
      await editDevice(payload)
    }
    emits('closeDialog')
    emits('eventSubmitDeviceForm')
  } catch (error) {
    validationMessage.value = (await error.json()).detail
    displayAlert.value = true
    setTimeout(() => {
      displayAlert.value = false
    }, 2000)
  }
}

const setData = () => {
  const incomingData = Object.assign({}, props.device)
  if (incomingData.id !== undefined) {
    deviceData.value = {
      ...incomingData
    }
    selectedCategory.value = incomingData.category.category
    selectedEmployee.value = incomingData.employee ? incomingData.employee.nickname : undefined
  }
}
</script>