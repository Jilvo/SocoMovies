import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from 'vite-plugin-vuetify'

export default defineConfig({
  plugins: [vue(), vuetify()],
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use 'vuetify/styles' as *;`,
      },
    },
  },
  server: {
  host: '0.0.0.0',
  port: 5173
}
})
