<template>
<div class="item"><div class="item_img">
  <img src="./assets/goods.png" alt=""></div>
  <div class="item_h4">{{title}}</div>
  <div>{{short_desc}}</div>
  <div class="item_p">{{price}}</div>
  <button type="button" v-bind:data-id="id">Купить</button>
</div>
</template>

<script>
export default {
  name: "List.vue",
  props:['id','title','short_desc','price']
}
</script>

<style scoped>

</style>
