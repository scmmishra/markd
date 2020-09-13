import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import './assets/style.css';
import call from './assets/call';
import VueStringFilter from 'vue-string-filter';
import PortalVue from 'portal-vue'
import VueTippy, { TippyComponent } from "vue-tippy";
import Unicon from 'vue-unicons';
import { uniExternalLinkAlt, uniTrashAlt, uniTimes } from 'vue-unicons/src/icons'

Unicon.add([uniExternalLinkAlt, uniTrashAlt, uniTimes])
Vue.use(Unicon)

Vue.use(VueTippy, {
	directive: "tippy", // => v-tippy
	flipDuration: 0,
	arrow: true,
	animation: 'scale',
	popperOptions: {
		// modifiers: {
		// 	preventOverflow: {
		// 		enabled: false
		// 	}
		// }
	}
});

Vue.component("tippy", TippyComponent);

Vue.use(PortalVue)

Vue.use(VueStringFilter);
Vue.prototype.$call = call;
Vue.config.productionTip = false

Vue.prototype.$eventHub = new Vue(); // Global event bus


new Vue({
	router,
	render: h => h(App)
}).$mount('#app')
