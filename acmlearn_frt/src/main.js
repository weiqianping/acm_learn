import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';
import 'element-plus/dist/index.css';
import ElementPlus from 'element-plus';

const app=createApp(App);
app.use(Toast).use(ElementPlus).use(router).mount('#app');
