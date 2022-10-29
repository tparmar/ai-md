import { defineStore } from 'pinia'
// Import axios to make HTTP requests
import axios from "axios"
export const useSymptomStore = defineStore("main", {
    state: () => ({
        symptoms: [],
        diseases: [],
    }),
    getters: {
      getSymptoms(state){
          return state.symptoms
        },
      getDiseases(state) {
        return state.diseases
      },
    },
    actions: {
      async fetchSymptoms() {
        try {
          const data = await axios.get('http://localhost:5000/get-symptoms/')
            this.symptoms = data.data
          }
          catch (error) {
            alert(error)
            console.log(error)
        }
      },
      async predictDisease(value) {
        var value_str = ""
        for (let i in value) {
          if (i == 0){
            value_str = value_str + value[i]
          }
          else {
            value_str = value_str + "," + value[i]
          }
        }
        try{
          const data = await axios.post('http://127.0.0.1:5000/predict-diseases/', {
            "symptoms": value_str,
            "diseases": "string"
          })
          this.diseases = data.data["diseases"]
          console.log(this.diseases)
        }
        catch (error) {
          alert(error)
          console.log(error)
        }
      }
    },

})