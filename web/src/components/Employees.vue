<template>
    <div id="container">
        <div id="sidebar">
            <Categories />
        </div>
        <div id="content">
            <v-list>
                <v-list-item
                    v-for="user in users"
                    :key="user.id"
                >
                    <v-list-item-content>
                        <v-list-item-header>
                            {{ user.username }}
                        </v-list-item-header>
                        <v-list-item-subtitle>
                            {{ user.name }}
                        </v-list-item-subtitle>
                    </v-list-item-content>

                    <v-icon>mdi-message-text</v-icon>
                </v-list-item>
            </v-list>
        </div>
    </div>
</template>

<script setup>
    import Categories from './Categories.vue'
    import { ref, watchEffect } from 'vue'

    const API_URL = 'https://jsonplaceholder.typicode.com/users'

    const users = ref(null)

    watchEffect(async () => {
        users.value = await(await fetch(API_URL)).json()
    })
</script>

<style scoped>
#container {
    display: flex;
}
</style>