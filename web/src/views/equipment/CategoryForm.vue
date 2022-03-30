<template>
  <Alert :displayAlert="displayAlert">
    {{ validationMessage }}
  </Alert>
  <v-container>
    <v-card>
      <v-card-header>
        <v-card-title>
          Add a new category
        </v-card-title>

        <v-card-avatar>
          <v-btn
            @click="toggleCategoryDialog"
            append-icon="mdi-window-close"
            variant="text"
            size="xs"
          ></v-btn>
        </v-card-avatar>
      </v-card-header>

      <v-form 
        @submit.prevent="submitNewCategory"
      >
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="New category"
                v-model="newCategory"
                :rules="[v => !!v || 'Category is required']"
                required
              >
              </v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" align="right">
              <v-btn type="submit">Submit</v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import Alert from '../../components/Alert.vue';
import {
  createCategory
} from './category'
const emits = defineEmits(['closeCategoryDialog', 'fetchCategories', 'focusEditForm'])

const newCategory = ref(null)
const validationMessage = ref(null)
const displayAlert = ref(false)

const submitNewCategory = async () => {
  try {
    await createCategory(newCategory.value)
    emits('fetchCategories')
    toggleCategoryDialog()
  } catch (error) {
    validationMessage.value = (await error.json()).detail
    displayAlert.value = true
    setTimeout(() => {
      displayAlert.value = false
    }, 2000)
  }
}
const toggleCategoryDialog = () => {
  emits('closeCategoryDialog')
  emits('focusEditForm')
}
</script>