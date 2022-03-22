<template>
<v-container fluid>
  <v-row>
    <v-col
      cols="12"
      md="3"
    >
        <v-card 
          class="mx-auto"
        >
          <v-list>
            <v-list-subheader>Thiết bị</v-list-subheader>
            <v-list-item prepend-icon="mdi-laptop" title="Máy tính" value="Máy tính"></v-list-item>
            <v-list-item prepend-icon="mdi-monitor" title="Màn hình" value="Màn hình"></v-list-item>
            <v-list-item prepend-icon="mdi-mouse" title="Chuột" value="Chuột"></v-list-item>
            <v-list-item prepend-icon="mdi-keyboard" title="Bàn phím" value="Bàn phím"></v-list-item>
          </v-list>
        </v-card>
    </v-col>

    <v-col
      cols="12"
      md="9"
    >
      <div>

        <p>
          v-spacer is a basic yet versatile spacing component used to distribute remaining width in-between a parents child components. 
          When placing a single v-spacer before or after the child components, the components will push to the right and left of its container.
          When more than one v-spacer’s are used between multiple components, the remaining width is evenly distributed between each spacer.
        </p>
      </div>
    </v-col>
  </v-row>

</v-container>
</template>

<script setup>
</script>
