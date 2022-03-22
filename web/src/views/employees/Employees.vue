<template>
<v-container>
  <v-row>
    <v-spacer></v-spacer>
    <v-btn
      color="primary"
      @click="clickEditEmployee({})"
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
          >
            <v-icon>mdi-pencil</v-icon>
            Edit
          </v-btn>
          <v-btn
            color="error"
            @click="clickDeleteEmployee(employee)"
          >
            <v-icon>mdi-delete</v-icon>
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</v-container>

<v-dialog v-model="displayEditForm" id="edit-form" style="z-index: 3000;"> 
  <EmployeeForm
    :employee="employee"
    :cardTitle="formTitle" 
    @eventSubmitEmployeeForm="fetchEmployees"
    @closeDialog="toggleEditDialog"
  />
</v-dialog>

<v-dialog v-model="displayDeleteDialog" style="z-index: 3000;">
  <v-card>
    <v-card-title>{{`Delete employee ${employee.nickname}`}}</v-card-title>
    <v-card-text>
        <span>{{`${employee.fullname}`}}</span><br>
        <span><v-icon>mdi-phone</v-icon>{{` ${employee.mobile}`}}</span><br>
        <span><v-icon>mdi-email</v-icon>{{` ${employee.email}`}}</span><br>
    </v-card-text>
    <v-card-actions>
      <v-btn @click="confirmDeleteEmployee">Yes</v-btn>
      <v-btn @click="toggleDeleteDialog">No</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>
</template>


<script>
import { onMounted, ref } from 'vue'
import EmployeeForm from './EmployeeForm.vue'
import { getEmployees, deleteEmployee } from './employee'

export default {
  setup() {
    const employees = ref(null)
    const employee = ref({})
    const displayEditForm = ref(false)
    const displayDeleteDialog = ref(false)
    const formTitle = ref('')

    const fetchEmployees = async () => {
      try {
        employees.value = await getEmployees()
      } catch (error) {
        console.log(error)
      }
    }

    const clickEditEmployee = (chosenOne) => {
      formTitle.value = chosenOne.id ? `Edit ${chosenOne.nickname} information` : 'Add a new employee'
      employee.value = chosenOne 
      toggleEditDialog()
    }

    const toggleEditDialog = () => {
      displayEditForm.value = !displayEditForm.value
    }

    const toggleDeleteDialog = () => {
      displayDeleteDialog.value = !displayDeleteDialog.value
    }

    const clickDeleteEmployee = (chosenOne) => {
      employee.value = chosenOne
      toggleDeleteDialog()
    }

    const confirmDeleteEmployee = async () => {
      await deleteEmployee(employee.value.id)
      await fetchEmployees()
      toggleDeleteDialog()
    }

    onMounted(() => {
      fetchEmployees()
    })

    return {
      employees,
      employee,
      fetchEmployees,

      formTitle,
      displayEditForm,
      clickEditEmployee,
      toggleEditDialog,

      clickDeleteEmployee,
      displayDeleteDialog,
      toggleDeleteDialog,
      confirmDeleteEmployee
    };
  },

  components: { 
    EmployeeForm
  }
}
</script>

<style>
/* ::v-deep(.v-dialog .v-overlay__content) {
  max-height: 100%;
}
:deep(.v-dialog .v-overlay__content) {
  max-height: 100%;
}

::v-deep(.v-overlay__content) {
  max-height: 100%;
}

:deep(.v-overlay__content) {
  max-height: 100%;
}

:deep(.v-overlay-container) {
  left: 50px;
} */

body .v-overlay-container .v-dialog .v-overlay__content {
  max-height: 100%;
}
</style>