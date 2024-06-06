<script setup>
import { onMounted, ref } from 'vue'
onMounted(() => {

})
const activeName = ref('chat')
const handleClick = (name)=>{
  activeName.value = name
}

</script>
<template>
  <div class="main">
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
      <el-tab-pane label="聊天" name="chat">
        <ChatPage></ChatPage>
      </el-tab-pane>
      <el-tab-pane label="知识库" name="knowledge">
        <KnowledgeManage></KnowledgeManage>
      </el-tab-pane>
    </el-tabs>
  </div>


</template>


<style lang="scss" scoped>
.main{
  width: 500px;
  height: 500px;
  background-color: #f5f6fa;
  border: #6a6a6a 1px solid;
  
}
:deep(.el-tabs__nav-wrap) {
  padding: 0 30px !important;
}
</style>