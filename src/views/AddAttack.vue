<template>
  <goHome></goHome>
  <div v-if="isAuth()"></div>
    <div class = "container-fluid">
        <div class = "row">
            <div class = "col-xl-9 text-start" style = "margin-top: 60px; margin-left: 100px">
                <h2>
                    <b>Создание записи по атаке</b>
                </h2>
            </div>
        </div>
        <div class = "row">
            <div class = "col-xl-9" style = "margin-top: 20px; margin-left: 60px">
                <textarea class="form-control" v-model="title" id="textAreaExample1" rows="4" style = "width: 500px;" placeholder="Введите название инцидента"></textarea>
                <textarea class="form-control" v-model="description" id="textAreaExample1" rows="4" style = "width: 500px;" placeholder="Введите описание инцидента"></textarea>
                <div class="col-auto" style = "margin-top: 20px; margin-left: 45px;">
                  <select v-model = "source" class = "form-select" style = "width: 190px;">
                    <option value="all">Укажите источник</option>
                    <option value="Сотрудники">Сотрудники</option>
                    <option value="Технические сбои">Технические сбои</option>
                    <option value="Вредоносное ПО">Вредоносное ПО</option>
                    <option value="Хакерская атака">Хакерская атака</option>
                    <option value="Поломка оборудования">Поломка оборудования</option>
                  </select>
                </div>
                <div class="col-auto" style = "margin-top: 20px; margin-left: 45px;">
                  <select v-model = "attack" class = "form-select" style = "width: 190px;">
                    <option value="all">Укажите атаку</option>
                    <option value="Фишинг">Фишинг</option>
                    <option value="DDoS-атака">DDoS-атака</option>
                    <option value="MITM-атака">MITM-атака</option>
                    <option value="SQL-инъекция">SQL-инъекция</option>
                    <option value="XSS">XSS</option>
                  </select>
                </div>
            </div>
            <div class="col-xl-9 dropdown" style = "margin-left: 105px; margin-top: 20px">
              <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                {{ this.status }}
              </button>
              <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                <li><a class="dropdown-item" @click="status='Решен'">Решен</a></li>
                <li><a class="dropdown-item" @click="status='В процессе решения'">В процессе решения</a></li>
              </ul>
            </div>
            <div class = "col-xl-4 text-start" style = "margin-top: 20px; margin-left: 105px">
                <button type = "submit" @click="addAttack()" class = "btn btn-primary fw-bold text-uppercase" style = "width: 100px; margin-top: 25px;">Add</button>
            </div>
        </div>
        <div class = "row">
        </div>
    </div>
    <div v-if="ER" style = "position: absolute; top: 110px; left: 120px;">
      {{ er_message }}
    </div>
</template>

<script>
import goHome from "./goHome.vue"
import router from "../Router.js"
import axios from "axios";
import { authMixin } from "../mixins/auth.js";
  export default {
    name: "auth",
    mixins: [authMixin,],
    components: {
      goHome
    },

    data() {
      return {
        title: '',
        description: '',
        source: 'all',
        status: 'Укажите статус',
        attack: 'all',
        token: null,
        ER: null,
        er_message: ""
      }
    },

    methods: {
      isAuth() {
        if ( this.token == false ) {
            router.push('/404');
        }
      },

      async addAttack() {

        if ( this.status == 'Укажите статус' | this.source == "all" | this.attack == "all" ) {
          this.ER = true;
          this.er_message = "Неверно указаны данные!"
          return;
        }

        await axios.post('http://localhost:8000/api/createNote', {
            nameOfIncident: this.title,
            Description: this.description,
            Source: this.source,
            Attack: this.attack,
            Status: this.status 
        }, 
        {
        headers: {
          Authorization: "Bearer " + localStorage.getItem('access_token'),
        }
        }).then(response => (this.info = response.data)).catch(error => (this.ER = error.response.data))
      }
    },

    async beforeMount() {

        await this.checkAuth();
    },
  }
</script>

<style>
</style>