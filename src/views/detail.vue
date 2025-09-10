<template>
    <goHome></goHome>
    <div class = "container">
        <div class = "row text-center">
            <h2 class = "col-xl-9 text-start" style = "margin-top: 80px;">Подробная информация об атаке</h2>
            <div class = col-xl-10>
                <div class = "d-flex justify-content-start" style = "margin-top: 20px;">
                    <h3>
                        <b>{{ this.nameOfIncident }}</b>
                    </h3>
                    <h5 style = "margin-top: 7px; margin-left: 20px;">
                        {{ this.Author }}, {{ this.date }}
                    </h5>
                </div>
            </div>
            <h3 class = "col-xl-9 text-start" style = "margin-top: 30px;">
                {{ this.Description }}
            </h3>
        </div>
        <div class = "row" style = "margin-top: 10px;">
            <h3 class = "col-xl-6 text-start">
                Источник: {{ this.Source }}
            </h3>
        </div>
        <div class = "row">
            <h3 class = "col-xl-6 text-start">
                Статус: {{ this.Status }}
            </h3>
        </div>
    </div>
    <div v-if="IsAuthor" class = "container">
        <div class = "row">
            <div class = "d-flex justify-content-start" style = "margin-top: 20px;">
                <div class = "col-xl-4">
                    <button type = "submit" @click="editAttack()" class = "btn btn-primary fw-bold text-uppercase" style = "width: 100px; margin-right: 20px">Edit</button>
                    <button type = "submit" @click="deleteAttack()" class = "btn btn-danger fw-bold text-uppercase" style = "width: 100px">Delete</button>
                </div>
            </div>
        </div>
    </div>
    <router-view></router-view>
</template>

<script>
import router from "../Router.js"
import goHome from './goHome.vue'
import axios from "axios";
import { authMixin } from "../mixins/auth.js";
  export default {
    name: "auth",
    mixins: [authMixin],
    components: {
        goHome
    },
    data() {
      return {
        nameOfIncident: '',
        Description: '',
        Source: '',
        Author: '',
        Status: '',
        IsAuthor: null,
        date: null,
        ER: null,
      }
    },

    methods: {
      async deleteAttack() {

        await axios.delete('http://localhost:8000/api/updateNote/' + this.$route.params.id, {
        headers: {
            Authorization: "Bearer " + localStorage.getItem('access_token'),
        }
        }).then(response => (this.info = response.data)).catch(error => (this.ER = error.response.data));

        router.push({name: 'home'});
      },

      editAttack() {
        router.push({path: '/edit/' + this.$route.params.id });
        return;
      },

    },

    async beforeMount() {

        this.checkAuth();

        await axios.get('http://localhost:8000/api/updateNote/' + this.$route.params.id,
        ).then(response => (this.info = response.data)).catch(error => (this.ER = error.response.data))

        if ( this.ER != null ) {
            router.push('/404');
        }

        if ( this.info != null) {
          this.nameOfIncident = this.info.nameOfIncident;
          this.Description = this.info.Description;
          this.Source = this.info.Source;
          this.Status = this.info.Status;
          this.date = this.info.Date;
          this.Author = this.info.Author;
        }
        
        await axios.put('http://localhost:8000/api/updateNote/' + this.$route.params.id, {}, {
        headers: {
            Authorization: "Bearer " + localStorage.getItem('access_token'),
        }
        }).then(response => (this.info = response.data)).catch(error => (this.ER = error.response.data))

        if ( this.ER.detail == null) {
            this.IsAuthor = true;
            return;
        }
    },

  }
</script>

<style>
</style>