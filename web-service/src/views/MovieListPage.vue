<template>
  <v-app>
    <Header />

    <v-main>
      <v-container fluid>
        <v-row class="mb-8" justify="center">
          <v-col cols="12" md="8">
            <h1 class="text-h4 text-center">All Movies</h1>
          </v-col>
        </v-row>

        <v-row justify="center" class="mb-6">
          <v-col cols="12" class="text-center" v-if="loading">
            <v-progress-circular indeterminate size="48" />
          </v-col>
          <v-col cols="12" v-else-if="error">
            <v-alert type="error" dense> Error : {{ error.message }} </v-alert>
          </v-col>
        </v-row>

        <v-row dense v-if="!loading && !error && items.length">
          <v-col v-for="item in items" :key="item.id" cols="12" sm="6" md="4" lg="3">
            <v-card outlined class="h-100 d-flex flex-column">
              <v-card-title class="text-h6">
                {{ item.title }}
              </v-card-title>
              <v-card-text class="flex-grow-1">
                {{ item.description }}
              </v-card-text>
              <v-card-actions>
                <v-btn text small :to="{ name: 'movie-detail', params: { id: item.id } }">
                  See more
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>

        <v-row justify="center" v-if="!loading && items.length === 0">
          <v-col cols="12">
            <v-alert type="info" dense>No movies found.</v-alert>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  import Header from '../components/Header.vue'
  import { ref, onMounted } from 'vue'

  const items = ref([])
  const loading = ref(true)
  const error = ref(null)

  onMounted(fetchAll)

  async function fetchAll() {
    loading.value = true
    try {
      const res = await fetch('http://localhost:8000/api/movies/')
      if (!res.ok) throw new Error(`Erreur ${res.status}`)
      const data = await res.json()
      items.value = Array.isArray(data) ? data : data.results || []
    } catch (e) {
      error.value = e
    } finally {
      loading.value = false
    }
  }
</script>

<style scoped>
  .home-page {
    min-height: 100vh;
  }
</style>
