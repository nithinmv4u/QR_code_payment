import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import MerchantPage from '@/views/MerchantPage'
import BuyerPage from '@/views/BuyerPage'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path:'/merchant', name:'MerchantPage', component: MerchantPage},
        {path:'/buyer', name:'BuyerPage', component: BuyerPage}
    ]
  })  

createApp(App).use(router).mount('#app')
