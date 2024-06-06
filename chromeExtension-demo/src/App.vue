<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
onMounted(() => {
  console.log('App.vue mounted')
  router.push('/home')
})
</script>

<template>

  <RouterView />
</template>

<style scoped>

</style>
