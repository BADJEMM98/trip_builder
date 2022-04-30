<template>
    <div v-if="isLoggedIn">
        <h1>Dashboard</h1>
        <h3>This page is for users only</h3>
    </div>
</template>

<script setup>
import { getAuth, onAuthStateChanged } from "@firebase/auth";
import { onBeforeUnmount } from "@vue/runtime-core";
import { ref } from "@vue/reactivity";
import { useRouter } from "vue-router";
    const router = useRouter();
    const isLoggedIn = ref(false);
    const auth = getAuth();
    const authListener = onAuthStateChanged(auth, function(user) {
        if (user) {
            isLoggedIn.value = true;
        }
        else{
            alert('You must be logged in to access this page');
            router.push('/');
        }
    });
    onBeforeUnmount(() => {
        authListener();
    })
</script>