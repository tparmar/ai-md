<template>
  <n-config-provider :theme="theme">
    <n-space vertical size="large">
      <n-layout class="full-height">
        <n-layout-header bordered>
          <n-space style="padding-top: 2em;">
            <n-icon color="#2080F0" size="40" @click="$router.push('/')" style="cursor: pointer; padding-top: 0.1em; padding-left: 1em;">
              <machine-Learning-model />
            </n-icon>
            <n-button quaternary style="font-weight: bolder;" size="large"  @click="$router.push('/try-it')">
              Try-It
            </n-button>
            <n-button quaternary style="font-weight: bolder;" size="large">
              <a style="text-decoration: none;" href="http://localhost:5000/" target="_blank">API</a>
            </n-button>
            <n-button quaternary style="font-weight: bolder;" size="large"  @click="$router.push('/about')">
              About
            </n-button>
            <!-- <n-space>
              <n-button @click="theme = darkTheme">Dark</n-button>
              <n-button @click="theme = null">Light</n-button>
            </n-space> -->
          </n-space>
        </n-layout-header>
        <n-layout-content content-style="padding-left: 3em;padding-right: 3em;">
          <br>
            <router-view/>
          <br>
        </n-layout-content>
        <n-layout-footer>
          <!-- for future -->
        </n-layout-footer>
      </n-layout>
    </n-space>
  </n-config-provider>
</template>

<script setup>
import { NMenu } from 'naive-ui'
</script>

<script>
import { defineComponent, h, ref } from "vue";
import { NIcon } from "naive-ui";
import { RouterLink } from "vue-router";
import { NButton } from "naive-ui";
import { NSpace } from "naive-ui";
import { darkTheme, NConfigProvider, NH1, NCard, NLayoutContent, NLayout} from "naive-ui";

import {
  BookOutline as BookIcon,
  HomeOutline as HomeIcon,
  AnalyticsOutline as AlIcon
} from "@vicons/ionicons5";

import {
  MachineLearning,
  MachineLearningModel
} from "@vicons/carbon";

function renderIcon(icon) {
  return () => h(NIcon, null, { default: () => h(icon) });
}

const menuOptions = [
  {
    label: () => h(RouterLink, {
      to: {
        path: "/"
      }
    }, { default: () => "Home" }),
    key: "home",
    icon: renderIcon(HomeIcon)
  },
  {
    label: () => h(RouterLink, {
      to: {
        path: "/try-it"
      }
    }, { default: () => "Try-It" }),
    key: "try_it",
    icon: renderIcon(AlIcon)
  },
  {
    label: () => h(RouterLink, {
      to: {
        path: "/about"
      }
    }, { default: () => "About" }),
    key: "about",
    icon: renderIcon(BookIcon)
  }
];

export default defineComponent({
  setup() {
    return {
      activeKey: ref(null),
      menuOptions,
      darkTheme,
      theme: ref(null)
    };
  }
});
</script>
<style scoped>
  .full-height {
    min-height: 100vh;
  }
</style>