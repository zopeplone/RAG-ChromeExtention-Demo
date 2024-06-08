<script setup>
const props = defineProps({
  isUser:{
    type:Boolean,
    default:false
  },
  text:{
    type:String,
    default:''
  },
  loading:{
    type:Boolean,
    default:false
  }
})
</script>
<template>
  <div class="item" :style="{flexDirection:props.isUser?'row-reverse':'row'}">
    <el-avatar size="small" :icon="props.isUser?'UserFilled':'HelpFilled'" />
    <div class="item-content">
      {{ text }}
      <span class="loading" v-show="loading">
        <div></div>
        <div></div>
        <div></div>
      </span>
    </div>
  </div>
</template>


<style lang="scss" scoped>
.item{
  display: flex;
  gap: 5px;
  flex-shrink: 0;
  margin: 10px 0;
  .el-avatar{
    font-size: 15px;
    align-self: flex-start;
  }
  &-content{
    padding: 5px 10px;
    max-width: 340px;
    border-radius: 10px;
    font-size: 13px;
    background-color: #fff;
    color: #363636;

  }
}
.loading{
  display: flex;
  gap: 5px;
  margin-top: 5px;
  div{
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background-color: #147ad6;
    animation: loading 1s infinite;
  }
}
@keyframes loading{
  0%{
    transform: translateY(0);
  }
  50%{
    transform: translateY(-5px);
  }
  100%{
    transform: translateY(0);
  }
}
</style>