<template>
    <h1>Create an account</h1>
    <p><input type="text" placeholder="Email" v-model="email"></p>
    <p><input type="password" placeholder="Password" v-model="password"></p>
    <p><button @click="register">Submit</button></p>
</template>

<script setup>
    import {ref} from "@vue/reactivity";
    import { useRouter } from 'vue-router';
    import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
    const email = ref('');
    const password = ref('');
    const router = useRouter();
    const register = () => {
        const auth = getAuth();
        createUserWithEmailAndPassword(auth, email.value, password.value)
            .then(() => {
                console.log('Successfully registered!');
                router.push('/');
            })
            .catch(error => {
                console.log(error.code);
                alert(error.message);
            })
    }
</script>