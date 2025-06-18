<template>
  <v-dialog v-model="dialog" max-width="600">
    <v-card>
      <v-card-title>Update Movie - {{ movie.title }}</v-card-title>
      <v-card-text>
        <v-form ref="form">
          <v-text-field v-model="updatedMovie.title" label="Title" required />

          <v-textarea v-model="updatedMovie.description" label="Description" required />

          <v-select
            v-model="updatedMovie.actors"
            :items="availableActors"
            item-title="full_name"
            item-value="id"
            label="Actors"
            multiple
            chips
          />
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer />
        <v-btn text @click="close">Cancel</v-btn>
        <v-btn color="primary" text @click="submit">Update</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
  import { ref, watch, defineProps, defineEmits, onMounted } from 'vue'

  const emit = defineEmits(['update:dialog', 'updated'])
  const props = defineProps({
    dialog: { type: Boolean, required: true },
    movie: { type: Object, required: true },
  })

  const dialog = ref(props.dialog)
  const updatedMovie = ref({ ...props.movie, actors: props.movie.actors.map((actor) => actor.id) })

  const availableActors = ref([])

  watch(
    () => props.dialog,
    (val) => (dialog.value = val)
  )

  onMounted(fetchActors)

  async function fetchActors() {
    const res = await fetch('http://localhost:8000/api/actors/')
    const data = await res.json()
    availableActors.value = data.results.map((actor) => ({
      id: actor.id,
      full_name: `${actor.first_name} ${actor.last_name}`,
    }))
    console.log(availableActors.value)
  }

  function close() {
    dialog.value = false
  }

  async function submit() {
    console.log(updatedMovie.value)
    await fetch(`http://localhost:8000/api/movies/${props.movie.id}/`, {
      method: 'PUT',
      body: JSON.stringify(updatedMovie.value),
      headers: { 'Content-Type': 'application/json' },
    })
    emit('updated')
    dialog.value = false
  }
</script>
