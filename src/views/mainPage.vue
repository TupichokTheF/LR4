<template>
  <section class = "homePage">
    <div class = "container-fluid" style = "margin-top: 50px; margin-bottom: 100px; border-bottom: 6px solid #eee; padding-bottom: 5px;">
      <div class="row text-center">
        <h1 class = "col-xl-6">SPA-кибербезопасность</h1>
        <div class = "col-xl-6" style = "margin-top: 10px;">
          <div v-if = "token" class = "d-flex justify-content-end">
            <h4 style = "margin-top: 10px">Hi, {{ login }}!</h4>
            <button type = "submit" @click="logout()" class = "btn btn-primary fw-bold text-uppercase" style = "width: 100px; margin-left: 30px;">Logout</button>
          </div>
          <div v-else class = "d-flex justify-content-end">
            <button type = "submit" @click="signIn()" class = "btn btn-primary fw-bold text-uppercase" style = "width: 100px; margin-left: 30px;">Sign in</button>
          </div>
        </div>
      </div>
    </div>
    <div class = "container-fluid">
      <div class = "row text-center">
        <h1 class = "col-auto">
          <b>Мониторинг инцидентов сайта</b>
        </h1>
        <div class="col-auto" style = "margin-top: 10px; ">
          <select v-model = "status" class = "form-select">
            <option value="all">Фильтр по статусу</option>
            <option value="Решен">Решен</option>
            <option value="В процессе решения">В процессе решения</option>
          </select>
        </div>
        <div class="col-auto" style = "margin-top: 10px; ">
          <select v-model = "attack" class = "form-select">
            <option value="all">Фильтр по атаке</option>
            <option value="Фишинг">Фишинг</option>
            <option value="DDoS-атака">DDoS-атака</option>
            <option value="MITM-атака">MITM-атака</option>
            <option value="SQL-инъекция">SQL-инъекция</option>
            <option value="XSS">XSS</option>
          </select>
        </div>
        <div class = "col-auto" style = "margin-top: 10px">
          <button type = "submit" @click="takeIncidents()" class = "btn btn-primary fw-bold text-uppercase" style = "width: 130px; margin-right: 20px">Применить</button>
        </div>
        <div class = "col-auto" style = "margin-top: 10px">
          <button type = "submit" @click="reset()" class = "btn btn-danger fw-bold text-uppercase" style = "width: 130px; margin-right: 20px">Сбросить</button>
        </div>
      </div>
    </div>
    <div class = "container-fluid" style = "margin-top: 30px; margin-left: 10px;">
      <div class = "row text-center" style = "text-decoration: none; color: inherit; font-size: 2em; border-bottom: 6px solid #eee; padding-bottom: 5px;">
        <div class = "col-xl-3">
          Название инцидента
        </div>
        <div class = "col-xl-2">
          Дата инцидента
        </div>
        <div class = "col-xl-3">
          Источник инцидента
        </div>
        <div class = "col-xl-2">
          Название атаки
        </div>
        <div class = "col-xl-2">
          Статус инцидента
        </div>
      </div>
    </div>
    <div v-if="Incidents.length">
      {{ Inci }}
    <div v-for="Incident in Incidents" :key="Incident.id" style = "margin-top: 30px">
      <div class = "container-fluid">
        <div class = "row text-center" style = "text-decoration: none; color: inherit; font-size: 2em; border-bottom: 6px solid #eee; padding-bottom: 5px; ">
          <div class = "col-xl-3">
            <router-link class = "text-center" style = "text-decoration: none; color: inherit; " :to="{ path: '/detail/' + Incident.id}">
              {{ Incident.nameOfIncident }}
            </router-link>
          </div>
          <div class = "col-xl-2">
            {{ Incident.Date }}
          </div>
          <div class = "col-xl-3">
            {{ Incident.Source }}
          </div>
          <div class = "col-xl-2">
            {{ Incident.Attack }}
          </div>
          <div class = "col-xl-2">
            {{ Incident.Status }}
          </div>
        </div>
      </div>
    </div>
    </div>
    <div class="justify-content-center text-center" style = "display: flex; gap: 10px; margin-top: 20px">
      <nav aria-label="Page navigation example" style = "display: flex; gap: 10px;">
          <ul class="pagination">
            <li class="page-item">
              <button type = "submit" @click="reduceOne(); takeIncidents()" class="page-link">
                Previous
              </button>
            </li>
            <li class="page-item" v-for="page in ( Math.floor(pages / 2) + (pages % 2 != 0) )">
              <button type = "submit" v-if="page < 6" @click="currentPage = page; takeIncidents()" class="page-link">
                {{ page }}
              </button>
            </li>
            <li class="page-item">
              <button type = "submit" @click="addOne(); takeIncidents(); showToast()" class="page-link">
                Next
              </button>
            </li>
          </ul>
      </nav>
    </div>
    <div class = "container-fluid">
      <div class = "row text-center">
        <div class = "col-xl-12 text-end" style = "margin-top: 40px;">
          <div v-if="token">
            <button type = "submit" @click="toAdd()" class = "btn btn-primary fw-bold text-uppercase" style = "width: 100px; margin-right: 20px">+ ADD</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';
import router from '../Router';
import { authMixin } from '../mixins/auth';
import 'vue3-toastify/dist/index.css'
import { toast } from 'vue3-toastify';
  export default {
    name: "mainPage",
    mixins: [authMixin],

    data() {
      return {
        status: 'all',
        attack: 'all',
        login: '',
        token: null,
        info: null,
        ER: null,
        Incidents: [],
        currentPage: 1,
        pages: null,
      }
    },

    methods: {

      addOne() {

        if ( this.currentPage * 2 / this.pages < 1.3 ) {
          this.currentPage += 1;
        }
        else {
          toast('hi', {
            autoclose: 1000
          })
        }
      },

      reduceOne() {
        if ( this.currentPage * 2 > 1 ) {
          this.currentPage -= 1;
        }
      },

      async logout() {

        await axios.post('http://localhost:8000/api/logout', {}, {
          refresh: localStorage.getItem('refresh_token'),
        }).then(response => (this.info = response.data)).catch(error => (this.ER = error.response.data))

        if ( this.info != null) {
          localStorage.clear();
          this.token = null;
          return;
        }
      },

      signIn() {

        router.push('authorization');
        return;
      },

      async toAdd() {

        router.push('addAttack');
        return;
      },

      async takeIncidents() {
        await axios.get('http://localhost:8000/api/home', {
        params: {
          offset: 2 * (this.currentPage - 1),
          Limit: 2,
          status_filter: this.status,
          attack_filter: this.attack
        }
        }).then(response => (this.Incidents = response.data.results, this.pages = response.data.count)).catch(error => (this.ER = error.response.data))
      },

      async reset () {
        this.status = 'all'
        this.attack = 'all'

        await this.takeIncidents()
      },

    },

    async mounted() {

      this.login = localStorage.getItem('login');

      await this.takeIncidents()
      
      this.checkAuth();
    },

    
  }
</script>

<style>

</style>
  