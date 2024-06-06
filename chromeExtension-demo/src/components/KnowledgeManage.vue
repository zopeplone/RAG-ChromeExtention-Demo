<script setup>
import { onMounted,ref } from 'vue';
import { getKnowledgeFromLocal } from '@/api/knowledge'
const knowData = ref([])
onMounted(async ()=>{
  knowData.value = await getKnowledgeFromLocal()
  knowData.value = knowData.value.reverse()
  // chrome.storage.onChanged.addListener(
  //   async()=>{
  //     knowData.value = await getKnowledgeFromLocal()
  //   }
  // )
})
</script>
<template>
  <div class="know">
    <h1>
      知识库
    </h1>
    <el-input prefix-icon="search" placeholder="搜索知识库内容">
    </el-input>
    <el-scrollbar>
      <div class="know-box">
          <div class="know-box-item" v-for="item in knowData" :key="item">
            <el-text line-clamp="2">
              {{ item }}
            </el-text>
            <div></div>
            <el-tag>页面添加</el-tag>
          </div>
      </div>
    </el-scrollbar>
  </div>
</template>


<style lang="scss" scoped>
.know{
  padding: 2px 15px;
  h1{
    text-align: center;
    color: #147ad6;
    margin: 5px 0;
  }
  &-box{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    height: 310px;
    margin-top: 15px;
    &-item{
      width: 410px;
      border-radius: 10px;
      height: 80px;
      background-color: #fff;
      padding: 3px 5px;
      .el-text{
        font-size: 17px;
        color: #363636;
        font-weight: 600;
      }
      .el-tag{

        margin-top: auto;
      }

    }
  }
}
:deep(.el-input__wrapper){
  border-radius: 20px !important;
}

</style>