<template>
<v-app>
  <v-app-bar
    app
    color="blue-grey"
  >
    <v-app-bar-nav-icon
      v-show="lgAndUp ? false : true"
      @click.stop="toggleNavDrawer"
    ></v-app-bar-nav-icon>
    <v-spacer></v-spacer>
    <v-spacer></v-spacer>
    <v-text-field
      prepend-inner-icon="mdi-magnify"
      filled
      hide-details
      label="Search employee"
    >
    </v-text-field>
  </v-app-bar>

  <v-navigation-drawer 
    app
    v-model="showNavDrawer"
  >
    <v-list>
      <v-list-item title="Dashboard" :to="{ name: 'Dashboard' }"></v-list-item>
      <v-list-item title="Equipment" :to="{ name: 'Equipment' }"></v-list-item>
      <v-list-item title="Employees" :to="{ name: 'Employees' }"></v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-main>
    <v-container fluid>
      <router-view></router-view>
    </v-container>
  </v-main>

  <v-footer app></v-footer>
</v-app>
</template>

<script>
import { useDisplay } from 'vuetify'
import { ref } from 'vue'

export default {
  setup() {
    const { lgAndUp } = useDisplay()
    const showNavDrawer = ref(lgAndUp.value)
    const toggleNavDrawer = () => {
      showNavDrawer.value = !showNavDrawer.value
    }
    return {
      lgAndUp,
      showNavDrawer,
      toggleNavDrawer
    }
  }
}
</script>