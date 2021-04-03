<template>
<div>
  <ul>
    <li>
      <h4>{{title}} - {{price}}</h4>
      <button  v-bind:data-id="id">Удалить</button>
    </li>
  </ul>
</div>
</template>

<script>
export default {
  name: "Bin.vue",
  props:['id','title','price'],
}
</script>

<style scoped>

</style>
