<template>
    <v-list>
        <v-list-item>
            <!-- <v-list-item-icon>
                <v-icon>mdi-devices</v-icon>
            </v-list-item-icon> -->
            <v-list-item-title>Loại thiết bị</v-list-item-title>
        </v-list-item>

        <v-list-group
            :value="true"
            prepend-icon="mdi-computer"
        >
            <template v-slot:activator>
                <v-icon>devices</v-icon>
                <v-list-item-title>Máy tính</v-list-item-title>
            </template>

            <v-list-group
                :value="true"
                no-action
                sub-group
            >

            </v-list-group>
        </v-list-group>
    </v-list>
</template>


<script>
export default {
}
</script>