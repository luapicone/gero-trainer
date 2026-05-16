import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  server: { open: '/index.html' },
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        pagina1: resolve(__dirname, 'pagina1.html'),
        pagina2: resolve(__dirname, 'pagina2.html'),
        coaching: resolve(__dirname, 'coaching.html'),
      },
    },
  },
});
