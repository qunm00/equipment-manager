<template>
<v-card>
  <v-card-title>{{ cardTitle }}</v-card-title>
  <v-form
    @submit="onSubmit"
    ref="formRef"
    v-model="valid"
  >
    <v-container fluid>
      <v-row>
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
            :rules="[v => !!v || 'Device category is required!']"
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
      </v-row>

      <v-row justify="space-between">
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-col>
          <v-btn type="submit">Submit</v-btn>
        </v-col>
        <v-col>
          <v-btn @click="$emit('closeDialog')">Cancel</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</v-card>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { 
  createDevice, 
  editDevice, 
  getCategoryByName
} from './equipment'
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

const valid = ref(false)
const formRef = ref(null)
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
    console.log(error)
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

<style scoped>
:deep(.v-input__details) {
  margin-bottom: 0;
}
</style>