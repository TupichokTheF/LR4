import { createRouter, createWebHashHistory } from 'vue-router'
import NotFound from './views/NotFound.vue'
import Authorization from "./views/Authorization.vue"
import Registration from "./views/Registration.vue"
import mainPage from "./views/mainPage.vue"
import AddAttack from './views/AddAttack.vue'
import detail from './views/detail.vue'
import edit from './views/edit.vue'

const routes = [
  { path: '/registration', component: Registration, name: 'registration' },
  { path: '/authorization', component: Authorization, name: 'authorization'},
  { path: '/addAttack', component: AddAttack, name: 'AddAttack'},
  { path: '/detail/:id', component: detail, name: "detailView" }, 
  { path: '/edit/:id', component: edit, name: "editView" }, 
  { path: '/', component: mainPage, name: 'home' },
  { path: '/404', component: NotFound, name: 'error' },
  { path: '/:catchAll(.*)', redirect: '/404' },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router;