<template>
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
      lazy-validation
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
              :rules="[v => /[0-9]{9,10}/.test(v) || 'Mobile phone is invalid']"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field 
              label="Email" 
              :rules="[v => /.+@.+\..+/.test(v) || 'Email is invalid']"
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

  setup(props, context) {
    const employeeData = ref({})
    const valid = ref(false)
    const formRef = ref(null)

    onMounted(() => {
      setData()
    })

    const onSubmit = async () => {
      valid.value  = (await formRef.value.validate()).valid
      if (!valid) {
        return
      }
      if (employeeData.value.id === undefined) {
        await createEmployee(employeeData.value)
      } else {
        await editEmployee(props.employee.id, employeeData.value)
      }
      setData()
      context.emit('closeDialog')
      context.emit('eventSubmitEmployeeForm')
    }

    const setData = () => {
      const incomingData = JSON.parse(JSON.stringify(props.employee))
      if (incomingData.id === undefined) {
        employeeData.value ={
          'activestatus': true
        }
      } else {
        employeeData.value = {...JSON.parse(JSON.stringify(props.employee))}
      }
    }

    return {
      employeeData,
      onSubmit,
      formRef,
      valid
    }
  },
}
</script>