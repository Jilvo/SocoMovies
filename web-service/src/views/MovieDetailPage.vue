<template>
  <v-app>
    <Header />

    <v-main>
      <v-container>
        <v-btn text small to="/">← Go Home</v-btn>

        <v-skeleton-loader v-if="loading" type="image, heading, text" />

        <v-alert type="error" v-else-if="error"> Error: {{ error.message }} </v-alert>

        <v-card v-else max-width="600" class="mx-auto">
          <!-- Header + actions -->
          <v-card-title class="d-flex justify-space-between">
            <span>{{ movie.title }}</span>
            <div class="d-flex">
              <v-btn text small color="primary" @click="editMovie" class="me-2">
                Update Movie
              </v-btn>
              <v-btn text small color="error" @click="deleteMovie"> Delete Movie </v-btn>
            </div>
          </v-card-title>

          <!-- Description and cast -->
          <v-card-text>{{ movie.description }}</v-card-text>
          <v-card-subtitle class="mt-4 text-subtitle-1"> Cast </v-card-subtitle>
          <div class="d-flex flex-wrap px-4">
            <v-chip v-for="actor in movie.actors" :key="actor.id" class="ma-1" outlined small>
              {{ actor.first_name }} {{ actor.last_name }}
            </v-chip>
          </div>

          <!-- Average rating -->
          <div class="px-4 my-4">
            <v-card-subtitle class="text-subtitle-1"> Average Rating </v-card-subtitle>
            <v-rating v-model="movie.average_rating" readonly length="5" size="20" />
          </div>

          <!-- Reviews -->
          <v-divider />
          <v-card-actions>
            <v-btn  variant="outlined" color="primary" @click="createReview"> Add Review </v-btn>
          </v-card-actions>

          <v-list two-line>
            <v-list-item v-for="review in movie.reviews" :key="review.id" class="align-start">
              <v-list-item-content>
                <div class="d-flex align-center mb-1">
                  <v-rating v-model="review.rating" readonly small length="5" class="me-2" />
                  <span class="text-caption grey--text">
                    {{ formatDate(review.created_at) }}
                  </span>
                </div>
                <v-list-item-subtitle>
                  {{ review.comment }}
                </v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-action class="d-flex align-center">
                <v-btn text small color="error" @click="deleteReview"> Delete Review </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list>
          <UpdateMovieDialogComponent
         v-model:dialog="showUpdateDialog"
         :movie="movie"
         @updated="fetchMovie"
       />
          <CreateReviewDialogComponent
            v-model:dialog="showReviewDialog"
            :movieId="movie.id"
            :movieTitle="movie.title"
            @submitted="onReviewSubmitted"
          />
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  import Header from '../components/Header.vue'
  import CreateReviewDialogComponent from '../components/CreateReviewDialogComponent.vue'
  import UpdateMovieDialogComponent from '../components/UpdateMovieDialogComponent.vue'
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'

  const props = defineProps({ id: String })
  const router = useRouter()

  const movie = ref(null)
  const loading = ref(true)
  const error = ref(null)
  const showReviewDialog = ref(false)
  const showUpdateDialog = ref(false)

  onMounted(fetchMovie)

  async function fetchMovie() {
    loading.value = true
    try {
      const res = await fetch(`http://localhost:8000/api/movies/${props.id}/`)
      if (!res.ok) throw new Error(`Error ${res.status}`)
      movie.value = await res.json()
    } catch (e) {
      error.value = e
    } finally {
      loading.value = false
    }
  }

  function editMovie() {
    console.log('Edit movie clicked')
    showUpdateDialog.value = true
  }

  async function deleteMovie() {
    if (!confirm('Are you sure you want to permanently delete this movie?')) return
    const res = await fetch(`http://localhost:8000/api/movies/${props.id}/`, { method: 'DELETE' })
    if (res.ok) router.push('/')
    else alert(`Delete failed: ${res.status}`)
  }

  function createReview() {
    console.log('Create review clicked')
    showReviewDialog.value = true
  }

  async function deleteReview(reviewId) {
    if (!confirm('Are you sure you want to delete this review?')) return
    const res = await fetch(`http://localhost:8000/api/reviews/${reviewId}/`, { method: 'DELETE' })
    if (res.ok) {
      movie.value.reviews = movie.value.reviews.filter((r) => r.id !== reviewId)
    } else {
      alert(`Delete review failed: ${res.status}`)
    }
  }

  function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    })
  }
</script>

<style scoped>
  .me-2 {
    margin-right: 8px;
  }
</style>
