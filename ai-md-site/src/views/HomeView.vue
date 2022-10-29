<template>
    <n-space vertical style="padding-top: 20vh">
      <n-space justify="center">
        <n-h1 style="font-size: 5em !important;">
          AI - Medical Diagnosis
        </n-h1>
      </n-space>
      <n-space justify="center">
        <n-h2>
          Predict probability of various diseases using AI
        </n-h2>
      </n-space>
      <n-space justify="center">
        <n-p style="font-size: 1.5em !important;">
          Search and select from over 130 different symptoms for the machine learning model to use and predict diagnosis.
        </n-p>
      </n-space>
      <n-space justify="center">
        <n-button type="primary" size="large" style="font-weight: bold;" @click="$router.push('try-it')">
          Get Started
        </n-button>
      </n-space>
    </n-space>
</template>

<script setup>
import { NImage } from "naive-ui";
import { NCard } from "naive-ui";
import { NButton } from "naive-ui";
import { NLayoutHeader } from "naive-ui";
import { NLayoutContent } from "naive-ui";
import { NLayout } from "naive-ui";
import { NLayoutFooter } from "naive-ui";
import { NLayoutSider } from "naive-ui";
import { NSpace } from "naive-ui";
import { NGradientText } from "naive-ui";
import { NH1, NH2, NH3, NP } from "naive-ui";
</script>