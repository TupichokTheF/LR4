<template>
    <goHome></goHome>
    <div class = "container-fluid">
        <div class = "row">
            <div class = "col-xl-9 text-start" style = "margin-top: 60px; margin-left: 100px">
                <h2>
                    <b>Редактирование записи по атаке</b>
                </h2>
            </div>
        </div>
        <div class = "row">
            <div class = "col-xl-9" style = "margin-top: 20px; margin-left: 60px">
                <textarea class="form-control" v-model="nameOfIncident" id="textAreaExample1" rows="4" style = "width: 500px;" placeholder="Введите название инцидента">{{ this.nameOfIncident }}</textarea>
                <textarea class="form-control" v-model="Description" id="textAreaExample1" rows="4" style = "width: 500px;" placeholder="Введите описание инцидента">{{ this.Description }}</textarea>
                <div class="col-auto" style = "margin-top: 20px; margin-left: 45px;">
                  <select v-model = "Source" class = "form-select" style = "width: 190px;">
                    <option value="all">Укажите источник</option>
                    <option value="Сотрудники">Сотрудники</option>
                    <option value="Технические сбои">Технические сбои</option>
                    <option value="Вредоносное ПО">Вредоносное ПО</option>
                    <option value="Хакерская атака">Хакерская атака</option>
                    <option value="Поломка оборудования">Поломка оборудования</option>
                  </select>
                </div>
            </div>
            <div class="col-xl-6 dropdown" style = "margin-left: 105px; margin-top: 20px">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                    {{ this.Status }}
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                    <div v-if="Status == 'Решен'">
                        <li><a class="dropdown-item" @click="Status='В процессе решения'">В процессе решения</a></li>
                    </div>
                    <div v-if="Status == 'В процессе решения'">
                        <li><a class="dropdown-item" @click="Status='Решен'">Решен</a></li>
                    </div>
                </ul>
            </div>
        </div>
        <div class = "row">
            <div class = "col-xl-6 text-start" style = "margin-top: 20px; margin-left: 105px">
                <button type = "submit" @click="editAttack()" class = "btn btn-primary fw-bold text-uppercase" style = "width: 100px; margin-top: 25px;">edit</button>
            </div>
        </div>
    </div>
    <div v-if="ER">
        <h5 class = "addError">{{ ER }}</h5>
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
        nameOfIncident: null,
        Description: null,
        Source: "all",
        Status: null,
        Attack: null,
        Author: null,
        ER: null,
      }
    },

    methods: {
      
        async editAttack() {

            await axios.put('http://localhost:8000/api/updateNote/' + this.$route.params.id, {
                nameOfIncident: this.nameOfIncident,
                Description: this.Description,
                Source: this.Source,
                Status: this.Status,
                Attack: this.Attack,
                Author: this.Author
            }, {
            headers: {
                Authorization: "Bearer " + localStorage.getItem('access_token'),
            }
            }).then(response => (this.info = response.data)).catch(error => (this.ER = error.response.data))

            
        }
    },

    async beforeMount() {

        this.checkAuth();

        await axios.put('http://localhost:8000/api/updateNote/' + this.$route.params.id, {}, {
        headers: {
            Authorization: "Bearer " + localStorage.getItem('access_token'),
        }
        }).then(response => (this.info = response.data)).catch(error => (this.ER = error.response.data))

        if ( this.ER.detail != null) {
            router.push('/404');
            return;
        }

        this.ER = null;

        await axios.get('http://localhost:8000/api/updateNote/' + this.$route.params.id,
        ).then(response => (this.info = response.data)).catch(error => (this.ER = error.response.data))

        if ( this.ER != null ) {
            router.push('/404');
        }

        this.nameOfIncident = this.info.nameOfIncident;
        this.Description = this.info.Description;
        this.Source = this.info.Source;
        this.Attack = this.info.Attack;
        this.Status = this.info.Status;
        this.Author = this.info.Author;
        
        return;
    },

  };
</script>

<style>
</style>