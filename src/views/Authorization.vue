<template>
    <section class="authorization">
      <div class = "container">
          <div class = "col text-center">
            <p class = "statusErrors text-start">
              <div v-if = "ER">
                {{ ER.error }}
              </div>
            </p>
            <h2 style = "margin-top: 5px;  margin-bottom: 15px;">Sign in</h2>
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="login-image bi bi-person-fill" viewBox="0 0 16 16">
              <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
            </svg>
            <div class="row">
              <input type = "text" v-model = "login" class = 'form-control' placeholder="Login" />
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="auth-pass-image bi bi-lock-fill" viewBox="0 0 16 16">
              <path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"/>
            </svg>
            <div class="row">
              <input type = "password" v-model = "password" class = 'form-control' placeholder="Password" />
            </div>
          </div>
          <p style = "margin-top: 30px; margin-left: 15px;">Ещё нет аккаунта? <router-link to="/registration">Зарегистрироваться</router-link></p>
          <button type = "submit" @click="validate()" class = "btn btn-primary fw-bold text-uppercase" style = "width: 200px; margin-top: 10px; margin-left: 10px;">Sign in</button>
        </div>
    </section>
</template>

<script>
import router from "../Router.js"
import axios from "axios";
const pattern= /^[a-zA-Z0-9]+$/
  export default {
    name: "auth",

    data() {
      return {
        password: '',
        ER: '',
        login: '',
        info: null,
      }
    },

    methods: {
      async validate() {

        if ( this.login == "" | this.password == "" ) {
          this.ER = "Не все поля заполнены!";
          return;
        }

        if ( !pattern.test(this.login) | !pattern.test(this.password) ) {
          return;
        }

        await axios.post('http://localhost:8000/api/auth', {
          username: this.login,
          password: this.password
        }).then(response => (this.info = response.data)).catch(error => (this.ER = error.response.data))

        if ( this.info != null ) {
          localStorage.setItem('access_token', this.info.access);
          localStorage.setItem('refresh_token', this.info.refresh);
          localStorage.setItem('login', this.login);
          router.push({name: 'home'});
        }

        return;
      }
    },

  }
</script>

<style>
</style>