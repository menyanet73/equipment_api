<template>
    <form class="sign-up" @submit.prevent="formSubmit">
        <div class="form-group">
            <label for="username">Username:</label>
            <input
                id="username"
                type="text"
                class="form-control"
                v-model.trim="form.username"
            />
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input
                id="password"
                type="password"
                class="form-control"
                v-model.trim="form.password"
            />
        </div>
        <button type="submit">Регистрация</button>
    </form>
</template>

<script>
import { validationMixin } from 'vuelidate'
export default {
    mixins: [validationMixin],
    name: 'SignUp',
    data() {
        return {
            mode: 'signUp',
            form: {
                username: 'your_username',
                password: 'your_password',
            },
            errors: []
        }
    },
    methods: {
        usernameInput(value) {
            this.form.username = value
            },
        passwordInput(value) {
            this.form.password = value
            },
        formSubmit() {
            this.signUp()
        },
        async signUp() {
            const res = await fetch('http://127.0.0.1:8000/api/user/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'applications/json',
                    'Access-Control-Allow-Origin': '*',
                },
                credentials: 'include',
                body: JSON.stringify({
                    username: this.form.username,
                    password: this.form.password,
                }),
                
            })
            console.log(res)
        }

        },
    // validations: {
    //     form: {
    //         username: {
    //             simpleValidator(value) {
    //                 console.log(value)
    //                 return value.length > 4
    //             }
    //         }
    //     }
    // },
}

</script>