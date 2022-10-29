import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { inject } from 'vue'

import App from './App.vue'
import router from './router'

// import './assets/main.scss'

const app = createApp(App)

app.use(createPinia())
app.provide('axios', app.config.globalProperties.axios)  // provide 'axios'
app.use(router, VueAxios, axios)

app.mount('#app')

export default {
    name: 'Comp',
    setup() {
      const axios: any = inject('axios')  // inject axios
  
      const getList = (): void => {
        axios
          .get('http://127.0.0.1:5000/get-symptoms/')
          .then((response: { data: any }) => {
            console.log(response.data)
          });
      };
  
      return { getList }
    }
  }


// Want to use async/await? Add the `async` keyword to your outer function/method.
async function getUser() {
  try {
    const response = await axios.get('/user?ID=12345');
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}
