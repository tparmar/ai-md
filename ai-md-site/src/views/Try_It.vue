<template>
  <n-space vertical>
    <n-h3>
      Symptoms
    </n-h3>
    <div v-if="options" >
        <n-transfer
          ref="transfer"
          v-model:value="value"
          virtual-scroll
          :options="options"
          filterable
        />
      </div>
      <!-- <p>Symptoms: {{ value }}</p> -->
      <n-button id = "submit-options" type="primary" @click="predictDisease(value)">
        Submit
      </n-button>
      <n-data-table
        ref="table"
        remote
        :columns="columns"
        :data="disease_data"
        :max-height="250"
        virtual-scroll
      />
  </n-space>
</template>

<script setup>
import { h, computed, onMounted, ref, reactive, watchEffect  } from 'vue';
import { NTransfer } from 'naive-ui';
import  { useSymptomStore }  from '../stores/Symptoms';
import { NScrollbar } from 'naive-ui';
import { NSpin } from 'naive-ui';
import { NButton } from 'naive-ui';
import { NDataTable, NSpace, NCard, NLayout, NLayoutContent, NProgress, NH3 } from 'naive-ui';

const store = useSymptomStore()


const getSymptoms = computed(() => {
  return store.getSymptoms
})
const symptoms = computed(() => {
  return store.symptoms
})

const getDiseases = computed(() => {
  return store.getDiseases
})


const predictDisease = computed(() => {
  return store.predictDisease
})

onMounted(() => {
  store.fetchSymptoms();
})

function createValues() {
  return Array.from({ length: 0 }).map((v, i) => i);
}

const options = computed(() => {
    var symptom_options = []
    console.log(getSymptoms.value)
    for (let symptom in getSymptoms.value) {
      symptom_options.push({label: symptom, value: symptom})
    }
    return symptom_options
})
const value = ref(createValues())

// watchEffect(() => console.log(JSON.parse(JSON.stringify(options.value))))

const columns = [
  {
    title: 'Disease',
    key: 'disease'
  },
  {
    title: 'Probability',
    key: 'probability',
    render (row) {
      return h(
            NProgress,
            {
              type: 'line',
              status: 'info',
              percentage: (row.probability * 100.0).toPrecision(2),
              indicatorPlacement: 'inside'
            }
          )
      }
  },
]

var disease_data = computed(() => {
    var arr = []
    for (var disease in getDiseases.value) {
      arr.push({key: disease, disease: disease, probability: getDiseases.value[disease]})
      console.log(typeof getDiseases.value[disease])
    }
    console.log((arr))
    return arr
})
</script>
