<template>
<v-container>
  <v-row>
    <h1>Employees</h1>
    <v-spacer></v-spacer>
    <v-btn
      color="primary"
      @click="buttonClick({})"
      id="add-button"
    >
      Add Employee
    </v-btn>
  </v-row>
</v-container>

<v-container>
  <v-row wrap>
    <v-col
      v-for="employee in employees"
      :key="employee.id"
      cols="12"
      md="6"
      lg="4"
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
          <!-- rename buttonClick -->
          <v-btn
            color="success"
            @click="buttonClick(employee)"
            id="edit-button"
          >
            <v-icon>mdi-pencil</v-icon>
            Edit
          </v-btn>
          <v-btn
            color="error"
            @click="confirmDelete(employee)"
          >
            <v-icon>mdi-delete</v-icon>
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</v-container>

<!-- change displayDialog to something elaborate -->
<v-dialog v-model="displayDialog">
  <v-card>
    <EmployeeForm
      :employee="employee"
      :cardTitle="formTitle" 
      @eventSubmitEmployeeForm="fetchEmployees"
      @closeDialog="toggleDialog"
    />
  </v-card>
</v-dialog>

<v-dialog v-model="displayDeleteConfirmation">
  <v-card>
    <v-card-title>{{`Delete`}}</v-card-title>
  </v-card>
</v-dialog>
</template>


<script>
import { onMounted, ref } from 'vue'
import EmployeeForm from './EmployeeForm.vue'
import { deleteEmployee } from './employee'

export default {
  setup() {
    const employees = ref(null)
    const employee = ref({})
    const displayDialog = ref(false)
    const formTitle = ref('')
    const displayDeleteConfirmation = ref(false)

    const buttonClick = (chosenOne) => {
      formTitle.value = chosenOne.id ? `Edit ${chosenOne.nickname} information` : 'Add a new employee'
      employee.value = chosenOne 
      displayDialog.value = !displayDialog.value
    }

    const fetchEmployees = async () => {
      try {
        employees.value = await (await fetch('/api/employees')).json()
      } catch (error) {
        console.log(error)
      }
    }

    const toggleDialog = () => {
      displayDialog.value= !displayDialog.value
    }

    const confirmDelete = (employeeId) => {
      console.log(employee.value)
      displayDeleteConfirmation.value = !displayDeleteConfirmation.value
    }

    onMounted(() => {
      fetchEmployees()
    })

    return {
      employees,
      employee,
      fetchEmployees,
      displayDialog,
      buttonClick,
      formTitle,
      toggleDialog,
      confirmDelete,
      displayDeleteConfirmation
    };
  },

  components: { 
    EmployeeForm
  }
}
</script>