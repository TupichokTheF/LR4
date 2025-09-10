import { createApp } from 'vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import './style.css'
import App from './App.vue'
import router from './Router.js'
import VueSweetalert2 from 'vue-sweetalert2';
import VueToastr from "vue-toastr";

createApp(App).use(router).use(VueSweetalert2).mount('#app')
