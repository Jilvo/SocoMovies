import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import MovieDetailPage from '../views/MovieDetailPage.vue'
import MovieListPage from '../views/MovieListPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,
  },
  {
    path: '/all-movies',
    name: 'movie-list',
    component: MovieListPage,
  },
  {
    path: '/movies/:id',
    name: 'movie-detail',
    component: MovieDetailPage,
    props: true,
  },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
