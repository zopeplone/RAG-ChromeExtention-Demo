<script setup>
import { computed, onMounted,ref } from 'vue';
import { getKnowledgeFromLocal } from '@/api/knowledge'
const knowData = ref([])
const getKnowledge = async()=>{
  knowData.value = await getKnowledgeFromLocal() || []
  knowData.value = knowData.value.reverse()
}
defineExpose({
  getKnowledge
})
onMounted(async ()=>{
  await getKnowledge()
})
const searchInput = ref('')
const showData = computed(()=>{
  return knowData.value.filter(item=>item.includes(searchInput.value))
})
</script>
<template>
  <div class="know">
    <h1>
      知识库
    </h1>
    <el-input prefix-icon="search" v-model="searchInput" placeholder="搜索知识库内容">
    </el-input>
    <el-scrollbar>
      <div class="know-box">
          <div class="know-box-item" v-for="item in showData" :key="item">
            <el-text line-clamp="2">
              {{ item }}
            </el-text>
            <div class="know-box-item-bottom">
              <el-tag>页面添加</el-tag>
            </div>
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
    margin-top: 15px;
    &-item{
      width: 94%;
      border-radius: 10px;
      height: 80px;
      background-color: #fff;
      padding: 3px 5px;
      position: relative;
      .el-text{
        font-size: 17px;
        color: #363636;
        font-weight: 600;
      }
      &-bottom{
        position: absolute;
        bottom: 4px;
        display: flex;
        align-items: center;
        margin-top: auto;
      }

    }
  }
}
:deep(.el-input__wrapper){
  border-radius: 20px !important;
}

</style>