<template>
    <div>
    <h1>Login to your account</h1>
    <p><input type="text" placeholder="Email" v-model="email" /></p>
    <p><input type="password" placeholder="Password" v-model="password" /></p>
    <p><button @click="signIn">Submit</button></p>
    </div>
</template>

<script setup>
    import { ref } from "@vue/reactivity";
    import { useRouter } from "vue-router";
    import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
    const email = ref("");
    const password = ref("");
    const router = useRouter();
    const signIn = () => {
    const auth = getAuth();
        signInWithEmailAndPassword(auth, email.value, password.value).then(() => {
            console.log("Successfully logged in!");
            router.push('/');
        })
        .catch(error => {
            let errMsg="";
            switch (error.code) {
                case 'auth/invalid-email':
                    errMsg = 'Invalid email'
                    break
                case 'auth/user-not-found':
                    errMsg = 'No account with that email was found'
                    break
                case 'auth/wrong-password':
                    errMsg = 'Incorrect password'
                    break
                default:
                    errMsg = 'Email or password was incorrect'
                    break
            }
            alert(errMsg);
        });
    };
</script>