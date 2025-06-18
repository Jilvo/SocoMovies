<template>
  <v-dialog v-model="dialog" max-width="500">
    <v-card>
      <v-card-title>Add a Review to {{ movieTitle }}</v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid">
          <v-rating v-model="newReview.rating" length="5" required />
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn text @click="close">Cancel</v-btn>
        <v-btn text @click="submit">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
  import { ref, watch, defineEmits, defineProps } from 'vue'

  const emit = defineEmits(['update:dialog', 'submitted'])
  const props = defineProps({
    dialog: { type: Boolean, required: true },
    movieTitle: { type: String, required: true },
    movieId: { type: String, required: true },
  })

  const dialog = ref(props.dialog)
  watch(
    () => props.dialog,
    (v) => (dialog.value = v)
  )
  watch(dialog, (v) => emit('update:dialog', v))

  const newReview = ref({ rating: 0, movie: props.movieId })

  function close() {
    dialog.value = false
  }

  async function submit() {
    console.log(JSON.stringify(newReview.value))
    await fetch(`http://127.0.0.1:8000/api/reviews/`, {
      method: 'POST',
      body: JSON.stringify(newReview.value),
      headers: { 'Content-Type': 'application/json' },
    })
    emit('submitted')
    dialog.value = false
  }
</script>
