import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { initializeApp } from "firebase/app";

const firebaseConfig = {
    apiKey: "AIzaSyCwhUfI8jbcPP35W7ZOVFfS_SYmjQ17oEk",
    authDomain: "trip-builder-auth.firebaseapp.com",
    projectId: "trip-builder-auth",
    storageBucket: "trip-builder-auth.appspot.com",
    messagingSenderId: "1012453386503",
    appId: "1:1012453386503:web:5614b3201a40afd3e0bda2"
};

initializeApp(firebaseConfig);

const app = createApp(App);
app.use(router)
app.mount('#app');
