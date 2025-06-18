<template>
  <v-card outlined class="h-100 d-flex flex-column">
    <v-card-title class="text-h6">
      {{ item.title }}
    </v-card-title>
    <v-card-text class="flex-grow-1">
      {{ item.description }}
    </v-card-text>
    <v-card-actions>
      <v-btn text small :to="{ name: 'movie-detail', params: { id: item.id } }"> See more </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  defineProps({
    item: {
      type: Object,
      required: true,
    },
  })
</script>
