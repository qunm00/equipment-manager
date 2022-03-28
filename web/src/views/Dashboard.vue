<template>
<v-container fill-height>
  <v-row>
    <v-col 
      cols="12"
      lg="5"
    >
      <v-container>
        <v-card>
         <v-card-title><b>Total devices</b></v-card-title>
         <v-card-actions>
           <v-spacer></v-spacer>
           {{ equipmentCount }} devices
         </v-card-actions>
        </v-card>

      </v-container>
      <v-container>
        <v-card>
          <v-card-title><b>Total employees</b></v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            {{ employeesCount }} employees
          </v-card-actions>
        </v-card>
      </v-container>
    </v-col>

    <v-col
      cols="12"
      lg="7"
    >
      <v-card>
        <v-card-title><b>Available devices</b></v-card-title>
          <v-container>
            <v-table>
              <thead>
                <tr>
                  <th class="text-left">
                    Category
                  </th>
                  <th class="text-right">
                    No. of devices
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="category in equipmentAvailabilityCount"
                  :key="category.name"
                >
                  <td>{{ category.name }}</td>
                  <td class="text-right">{{ category.count }}</td>
                </tr>
              </tbody>
            </v-table>
          </v-container>

      </v-card>
    </v-col>
  </v-row>
</v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getEmployeesCount } from './employees/employee'
import { getEquipmentCount, getEquipmentAvailabilityCount } from './equipment/equipment';

const equipmentCount = ref(0)
const employeesCount = ref(0)
const equipmentAvailabilityCount = ref({})

onMounted(async () => {
  equipmentCount.value = await getEquipmentCount()
  employeesCount.value = await getEmployeesCount()
  equipmentAvailabilityCount.value = await getEquipmentAvailabilityCount()
})

const desserts = ref([
  {
    name: 'Frozen Yogurt',
    calories: 159,
  },
  {
    name: 'Ice cream sandwich',
    calories: 237,
  },
  {
    name: 'Eclair',
    calories: 262,
  },
  {
    name: 'Cupcake',
    calories: 305,
  },
  {
    name: 'Gingerbread',
    calories: 356,
  },
  {
    name: 'Jelly bean',
    calories: 375,
  },
  {
    name: 'Lollipop',
    calories: 392,
  },
  {
    name: 'Honeycomb',
    calories: 408,
  },
  {
    name: 'Donut',
    calories: 452,
  },
  {
    name: 'KitKat',
    calories: 518,
  },
])
</script>