<template>
<v-container>
  <v-row
    align="center"
    justify="end"
  >
    <v-col
      cols="12"
      md="4"
    >
      <v-text-field
        prepend-inner-icon="mdi-magnify"
        label="Search employees"
        hide-details
        density="compact"
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
    :employee="data.employee"
    :cardTitle="formTitle" 
    @eventSubmitEmployeeForm="fetchEmployees"
    @closeDialog="toggleEditDialog"
  />
</v-dialog>

<v-dialog v-model="displayDeleteDialog" style="z-index: 3000;">
  <v-card>
    <v-card-title>{{`Delete employee ${data.employee.nickname}`}}</v-card-title>
    <v-card-text>
        <span>{{`${employee.fullname}`}}</span><br>
        <span><v-icon>mdi-phone</v-icon>{{` ${data.employee.mobile}`}}</span><br>
        <span><v-icon>mdi-email</v-icon>{{` ${data.employee.email}`}}</span><br>
    </v-card-text>
    <v-card-actions>
      <v-btn @click="confirmDeleteEmployee">Yes</v-btn>
      <v-btn @click="toggleDeleteDialog">No</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>
</template>


<script>
import { onMounted, computed, ref, reactive } from 'vue'
import EmployeeForm from './EmployeeForm.vue'
import { getEmployees, deleteEmployee } from './employee'

export default {
  setup() {
    const data = reactive({
      'employees': [],
      'employee': null
    })
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
      if (searchTerm.value.length === 0) {
        return data.employees
      }
      return data.employees.filter(employee => {
        return employee.email.includes(searchTerm.value)
          || employee.fullname.includes(searchTerm.value)
          || employee.mobile.includes(searchTerm.value)
          || employee.nickname.includes(searchTerm.value)
      })
    })

    const toggleEditDialog = () => {
      displayEditForm.value = !displayEditForm.value
    }

    const clickEditEmployee = (chosenOne) => {
      formTitle.value = chosenOne.id ? `Edit ${chosenOne.nickname} information` : 'Add a new employee'
      data.employee = chosenOne 
      toggleEditDialog()
    }

    const toggleDeleteDialog = () => {
      displayDeleteDialog.value = !displayDeleteDialog.value
    }

    const clickDeleteEmployee = (chosenOne) => {
      data.employee = chosenOne
      toggleDeleteDialog()
    }

    const confirmDeleteEmployee = async () => {
      await deleteEmployee(data.employee.id)
      await fetchEmployees()
      toggleDeleteDialog()
    }

    onMounted(() => {
      fetchEmployees()
    })

    return {
      data,

      fetchEmployees,
      searchTerm,
      filteredEmployees,

      formTitle,
      clickEditEmployee,
      displayEditForm,
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
body .v-overlay-container .v-dialog .v-overlay__content {
  max-height: 100%;
}
</style>