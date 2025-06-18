import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import router from './router'
import { createVuetify } from 'vuetify'
import 'vuetify/styles'

createApp(App)
  .use(createPinia())
  .use(router)
  .use(createVuetify())
  .mount('#app')
