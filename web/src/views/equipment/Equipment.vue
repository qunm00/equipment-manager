<template>
<v-container>
  <v-row
    align="center"
    justify="space-between"
  >
    <v-col
      cols="12"
      lg="3"
    >
      <v-select
        :items="data.categories"
        label="Categories"
        v-model="toolbarCategory"
        hide-details
      >
      </v-select>
    </v-col>
    <v-col
      cols="12"
      lg="3"
    >
      <v-select
        :items="data.employees"
        label="Employees"
        v-model="toolbarEmployee"
        hide-details
      >
      </v-select>
    </v-col>
    <v-spacer></v-spacer>
    <v-col
      cols="12"
      lg="3"
    >
      <v-text-field
        density="compact"
        hide-details
        label="Search serial number"
        prepend-inner-icon="mdi-magnify"
        variant="underlined"
        v-model="toolbarSerialNumber"
      >
      </v-text-field>
    </v-col>
    <v-col
      cols="12"
      md="3"
      lg="2"
      align="center"
    >
      <v-btn
        color="primary"
        @click="clickEditDevice({})"
      >Add Device</v-btn>
    </v-col>
  </v-row>
</v-container>

<v-container>
  <v-table
  >
    <thead>
      <tr>
        <th>Device name</th>
        <th>Device category</th>
        <th>Serial number</th>
        <th>Borrower</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr 
        v-for="device in filteredEquipment"
        :key="device.id"
      >
        <td>{{ device.name }}</td>
        <td>{{ device.category.category }}</td>
        <td>{{ device.serialnumber }}</td>
        <td>{{ device.employee ? device.employee.nickname : ''}}</td>
        <td>
          <v-row
            justify="space-around"
            no-gutters
          >
            <v-col>
              <v-btn 
                size="small" 
                icon="mdi-pencil"
                color="success"
                variant="text"
                @click="clickEditDevice(device)"
              ></v-btn>
            </v-col>
            <v-col>
              <v-btn 
                size="small"
                icon="mdi-delete"
                color="error"
                variant="text"
                @click="clickDeleteDevice(device)"
              ></v-btn>
            </v-col>
          </v-row>
        </td>
      </tr>
    </tbody>
  </v-table>
</v-container>

<v-dialog 
  v-model="displayEditForm"
  :retain-focus="editFormFocus"
>
  <EquipmentForm
    :device="data.device"
    :categories="data.categories"
    :employees="data.employees"
    :fetchedCategories="fetchedCategories"
    :fetchedEmployees="fetchedEmployees"
    :cardTitle="formTitle"
    @closeDialog="displayEditForm = !displayEditForm"
    @openAddCategory="displayCategoryDialog = !displayCategoryDialog; editFormFocus = !editFormFocus"
    @eventSubmitDeviceForm="fetchEquipment"
  />
</v-dialog>

<v-dialog v-model="displayDeleteDialog">
  <DeleteDialog
    @confirmDelete="confirmDeleteDevice"
    @closeDeleteDialog="displayDeleteDialog = !displayDeleteDialog"
  >
    <v-card-title>Delete device</v-card-title>
    <v-card-text>Device: <b>{{data.device.name}}</b></v-card-text>
    <v-card-text>Serial number: <b>{{data.device.serialnumber}}</b></v-card-text>
  </DeleteDialog>
</v-dialog> 


<v-dialog v-model="displayCategoryDialog">
  <CategoryForm
    @fetchCategories="fetchCategories"
    @closeCategoryDialog="displayCategoryDialog = !displayCategoryDialog"
    @focusEditForm="editFormFocus = !editFormFocus"
  >
  </CategoryForm>
</v-dialog>
</template>

<script setup>
import { 
  reactive, 
  ref, 
  onMounted,
  computed
} from 'vue'

import EquipmentForm from './EquipmentForm.vue'
import CategoryForm from './CategoryForm.vue';
import DeleteDialog from '../../components/DeleteDialog.vue';

import {
  toggler
} from '../../utils'

import { 
  getEquipment, 
  deleteDevice, 
  filterEquipment

} from './equipment'

import {
  getCategories, 
} from './category'

import { getEmployees } from '../employees/employee'

const data = reactive({
  'equipment': [],
  'categories': [],
  'employees': [],
  'device': null
})


const formTitle = ref(null)

const fetchedCategories = ref(null)
const fetchedEmployees = ref(null)

const editFormFocus = ref(true)
const displayEditForm = ref(false)
const displayDeleteDialog = ref(false)
const displayCategoryDialog = ref(false)

const toolbarCategory = ref(undefined)
const toolbarEmployee = ref(undefined)
const toolbarSerialNumber = ref('')

onMounted(() => {
  fetchEquipment()
  fetchCategories()
  fetchEmployees()
})

const fetchEquipment = async () => {
  try {
    data.equipment = await getEquipment()
  } catch (error) {
    console.log(error)
  }
}

const filteredEquipment = computed(() => {
  return filterEquipment(
    data.equipment, 
    toolbarCategory.value, 
    toolbarEmployee.value, 
    toolbarSerialNumber.value
  )
})

const fetchCategories = async () => {
  try {
    fetchedCategories.value = await getCategories()
    fetchedCategories.value.forEach(item => {
      if (!data.categories.includes(item.category)) {
          data.categories.push(item.category)
      }
    })
  } catch (error) {
    console.log(error)
  }
}

const fetchEmployees = async () => {
  try {
    fetchedEmployees.value = await getEmployees()
    fetchedEmployees.value.forEach(employee => {
      if (!data.employees.includes(employee.nickname) && employee.activestatus) {
        data.employees.push(employee.nickname)
      }
    })
  } catch (error) {
    console.log(error)
  }
}

const clickEditDevice = (chosenOne) => {
  formTitle.value = chosenOne.id 
    ? `Edit ${chosenOne.name} ${chosenOne.serialnumber}`
    : 'Add a new device'
  data.device = chosenOne
  toggler(displayEditForm)
}

const clickDeleteDevice = (chosenOne) => {
  data.device = chosenOne 
  toggler(displayDeleteDialog)
}

const confirmDeleteDevice = async () => {
  await deleteDevice(data.device.id)
  await fetchEquipment()
  toggler(displayDeleteDialog)
}
</script>

<style>
body .v-dialog .v-overlay__content {
  max-height: 100vh;
}
</style>