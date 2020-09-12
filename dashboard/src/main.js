import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import './assets/style.css';
import call from './assets/call';
import VueStringFilter from 'vue-string-filter';
import PortalVue from 'portal-vue'

Vue.use(PortalVue)

Vue.use(VueStringFilter);
Vue.prototype.$call = call;
Vue.config.productionTip = false

new Vue({
	router,
	render: h => h(App)
}).$mount('#app')
