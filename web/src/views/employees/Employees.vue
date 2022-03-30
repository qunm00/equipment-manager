<template>
<v-container>
  <v-row
    align="center"
    justify="end"
  >
    <v-col
      cols="12"
      lg="3"
    >
      <v-text-field
        density="compact"
        hide-details
        label="Search employees"
        prepend-inner-icon="mdi-magnify"
        variant="underlined"
        v-model="searchTerm"
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
        @click="clickEditEmployee({})"
        id="add-button"
      >
        Add Employee
      </v-btn>
    </v-col>
  </v-row>
</v-container>

<v-container>
  <v-row wrap>
    <v-col
      v-for="employee in filteredEmployees"
      :key="employee.id"
      cols="12"
      sm="6"
      lg="3"
    >
      <v-card>
        <v-card-header>
          <v-card-header-text>
            <v-card-title>{{employee.nickname}}</v-card-title>
            <v-card-subtitle>{{employee.fullname}}</v-card-subtitle>
          </v-card-header-text>
  
          <v-card-avatar>
            <v-chip 
             :color="employee.activestatus ? 'green': 'red'"
             size="large"
            >
              {{employee.activestatus ? 'active' : 'inactive'}}
            </v-chip>
          </v-card-avatar>
        </v-card-header>
  
        <v-card-text>
          <span><v-icon>mdi-phone</v-icon> {{employee.mobile}}</span><br>
          <span><v-icon>mdi-email</v-icon> {{employee.email}}</span><br>
        </v-card-text>

        <v-card-actions>
          <v-btn
            color="success"
            @click="clickEditEmployee(employee)"
            id="edit-button"
            prepend-icon="mdi-pencil"
          >
            Edit
          </v-btn>
          <v-btn
            color="error"
            @click="clickDeleteEmployee(employee)"
            prepend-icon="mdi-delete"
          >
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</v-container>

<v-dialog v-model="displayEditForm" id="edit-form"> 
  <EmployeeForm
    :employee="data.employee"
    :cardTitle="formTitle" 
    @eventSubmitEmployeeForm="fetchEmployees"
    @closeDialog="displayEditForm = !displayEditForm"
  />
</v-dialog>

<v-dialog v-model="displayDeleteDialog">
  <Alert :displayAlert="displayAlert">
    {{ alertMessage }}
  </Alert>
  <v-container>
    <DeleteDialog
      @confirmDelete="confirmDeleteEmployee"
      @closeDeleteDialog="displayDeleteDialog = !displayDeleteDialog"
    >
      <v-card-title>{{`Delete employee ${data.employee.nickname}`}}</v-card-title>
      <v-card-text>
          <span>{{`${data.employee.fullname}`}}</span><br>
          <span><v-icon>mdi-phone</v-icon>{{` ${data.employee.mobile}`}}</span><br>
          <span><v-icon>mdi-email</v-icon>{{` ${data.employee.email}`}}</span><br>
      </v-card-text>
    </DeleteDialog>
  </v-container>
</v-dialog>
</template>


<script setup>
import { onMounted, computed, ref, reactive } from 'vue'
import Alert from '../../components/Alert.vue'
import EmployeeForm from './EmployeeForm.vue'
import DeleteDialog from '../../components/DeleteDialog.vue';
import { getEmployees, deleteEmployee, filterEmployees } from './employee'
import { toggler } from '../../utils'

const data = reactive({
  'employees': [],
  'employee': null
})
const displayAlert = ref(false)
const alertMessage = ref(null)
const displayEditForm = ref(false)
const displayDeleteDialog = ref(false)
const formTitle = ref('')
const searchTerm = ref('')


const fetchEmployees = async () => {
  try {
    data.employees = await getEmployees()
  } catch (error) {
    console.log(error)
  }
}

const filteredEmployees = computed(() => {
  return filterEmployees(data.employees, searchTerm.value.toLowerCase())
})

const clickEditEmployee = (chosenOne) => {
  formTitle.value = chosenOne.id ? `Edit ${chosenOne.nickname} information` : 'Add a new employee'
  data.employee = chosenOne 
  toggler(displayEditForm)
}

const clickDeleteEmployee = (chosenOne) => {
  data.employee = chosenOne
  toggler(displayDeleteDialog)
}

const confirmDeleteEmployee = async () => {
  try {
    await deleteEmployee(data.employee.id)
    await fetchEmployees()
    toggler(displayDeleteDialog)
  } catch (error) {
    alertMessage.value = (await error.json()).detail
    displayAlert.value = true
    setTimeout(() => {
      displayAlert.value = false
    }, 2000)
  }
}

onMounted(() => {
  fetchEmployees()
})
</script>

<style>
body .v-dialog .v-overlay__content {
  max-height: 100%;
}
</style>