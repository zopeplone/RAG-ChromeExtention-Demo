<script setup>
import { onMounted, ref, watchEffect } from 'vue'
onMounted(() => {

})
const activeName = ref('chat')
const know = ref(null)
watchEffect(() => {
  if (activeName.value === 'knowledge') {
    know.value.getKnowledge()
  }
})

</script>
<template>
  <div class="main">
    <el-tabs v-model="activeName" >
      <el-tab-pane label="聊天" name="chat">
        <ChatPage></ChatPage>
      </el-tab-pane>
      <el-tab-pane label="知识库" name="knowledge">
        <KnowledgeManage ref="know"></KnowledgeManage>
      </el-tab-pane>
    </el-tabs>
  </div>


</template>


<style lang="scss" scoped>
.main{
  width: 100%;
  min-height: 100vh;
  background-color: #f5f6fa;
  
}
:deep(.el-tabs__nav-wrap) {
  padding: 0 30px !important;
}
</style>