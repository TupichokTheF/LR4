<template>
    <section class="registration">
      <div class = "container">
        <div class = "row">
          <div class = "col text-center">
            <h2 style = "margin-top: 5px; margin-bottom: 15px;">Sign up</h2>
            <p class = "statusErrors text-start">
              <div v-if = "ER">
                <div v-if = "ER.username" >{{ "Пользователь с этим логином уже существует!" }}</div>
                <div v-if = "ER.error" >{{ ER.error }}</div>
                <div v-if = "ER.email" >{{ "Некорректный email" }}</div>
              </div>
            </p>
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="login-image bi bi-person-fill" viewBox="0 0 16 16">
              <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
            </svg>
            <div class="row">
              <input type = "text" v-model="login" class = 'form-control' placeholder="Login. Required 6 symbols" />
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="currentColor" class="email-image bi bi-at" viewBox="0 0 16 16">
              <path d="M13.106 7.222c0-2.967-2.249-5.032-5.482-5.032-3.35 0-5.646 2.318-5.646 5.702 0 3.493 2.235 5.708 5.762 5.708.862 0 1.689-.123 2.304-.335v-.862c-.43.199-1.354.328-2.29.328-2.926 0-4.813-1.88-4.813-4.798 0-2.844 1.921-4.881 4.594-4.881 2.735 0 4.608 1.688 4.608 4.156 0 1.682-.554 2.769-1.416 2.769-.492 0-.772-.28-.772-.76V5.206H8.923v.834h-.11c-.266-.595-.881-.964-1.6-.964-1.4 0-2.378 1.162-2.378 2.823 0 1.737.957 2.906 2.379 2.906.8 0 1.415-.39 1.709-1.087h.11c.081.67.703 1.148 1.503 1.148 1.572 0 2.57-1.415 2.57-3.643zm-7.177.704c0-1.197.54-1.907 1.456-1.907.93 0 1.524.738 1.524 1.907S8.308 9.84 7.371 9.84c-.895 0-1.442-.725-1.442-1.914z"/>
            </svg>
            <div class="row">
              <input type = "email" pattern=".+@example\.com" v-model="email" class = 'form-control' placeholder="Email" />
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="reg-pass-image bi bi-lock-fill" viewBox="0 0 16 16">
              <path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"/>
            </svg>
            <div class="row">
              <input type = "password" v-model="password" class = 'form-control' placeholder="Password. Required 6 symbols" />
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" width="27" height="27" fill="currentColor" class="repeat-pass-image bi bi-key-fill" viewBox="0 0 16 16">
              <path d="M3.5 11.5a3.5 3.5 0 1 1 3.163-5H14L15.5 8 14 9.5l-1-1-1 1-1-1-1 1-1-1-1 1H6.663a3.5 3.5 0 0 1-3.163 2zM2.5 9a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
            </svg>
            <div class="row">
              <input type = "password" v-model="repeatPass" class = 'form-control' placeholder="Repeat password" />
            </div>
          </div>
          <p style = "margin-top: 30px; margin-left: 15px;">Уже есть аккаунт? <router-link to="/authorization">Авторизоваться</router-link></p>
          <button type = "submit" @click="validate()" class = "btn btn-primary fw-bold text-uppercase" style = "width: 200px; margin-top: 10px; margin-left: 20px;">Sign up</button>
        </div>
      </div>
    </section>
  </template>
  
<script>
import router from "../Router.js"
import axios from "axios";

  export default {
    name: "registration",
    
    data() {
      return {
        login: '',
        password: '',
        email: '',
        repeatPass: '',
        ER: null,
        info: ''
      }
    },
    methods: {
      async validate() {

        if ( this.login == "" | this.email == "" | this.password == "" | this.repeatPass == "" ) {
          this.ER = {
            error: "Не все поля заполнены!"
          }

          return;
        }

        if ( this.password != this.repeatPass ) {
          this.ER = {
            error: "Пароли не совпадают!"
          }

          return;
        }
        
        await axios.post('http://localhost:8000/api/registration', {
          username: this.login,
          email: this.email,
          password: this.password
        }).then(response => (this.info = "succes")).catch(error => (this.ER = error.response.data))

        if ( this.info == "succes" ) {
          router.push({name: 'authorization'});
        }

        return;
      }, 
    },
  }
</script>

<style>

</style>
  