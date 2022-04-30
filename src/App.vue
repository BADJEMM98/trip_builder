<template>
  <div>
    <nav>
      <router-link to="/">Home</router-link>
      <span v-if="isLoggedIn">
        <router-link to="/dashboard">Dashboard</router-link>
      </span>
      <span v-if="isLoggedIn">
        <button @click="signOutCallback">Logout</button>
      </span>
      <span v-else>
        <router-link to="/register">Register</router-link>
        <router-link to="/sign-in">Login</router-link>
      </span>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
import { getAuth, onAuthStateChanged, signOut } from "@firebase/auth";
import { ref } from "@vue/reactivity";
import { useRouter } from "vue-router";
  const router = useRouter();
  const isLoggedIn = ref(true);
  const auth = getAuth();
  onAuthStateChanged(auth, function(user) {
    if (user) {
      isLoggedIn.value = true;
    } else {
      isLoggedIn.value = false;
      }
  });
  
  const signOutCallback = () => {
    signOut(auth);
    router.push('/');
  }
</script>