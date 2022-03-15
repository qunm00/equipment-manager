<template>
    <v-app>
        <v-app-bar>
            <v-app-bar-title>
                <router-link class="menu-button" to ="/">Dashboard</router-link>
            </v-app-bar-title>

            <v-app-bar-title>
                <router-link class="menu-button" to ="/equipment">Equipment</router-link>
            </v-app-bar-title>

            <v-app-bar-title>
                <router-link class="menu-button" to ="/employees">Employees</router-link>
            </v-app-bar-title>
        </v-app-bar>

        <v-main>
            <v-container fluid>
                <router-view></router-view>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
</script>

<style scoped>
.menu-button {
    text-decoration: none;
    color: inherit;
}
</style>
