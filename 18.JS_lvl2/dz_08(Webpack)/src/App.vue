<template>
  <div class="conteiner">
    <div class="menu">
      <nav class="navbar navbar-light bg-light" style="justify-content: start;">
        <a href="/"><img src="./assets/icon-hover.png" width="30" height="30" class="d-inline-block align-top" alt=""></a>
        <input type="text" id="search" placeholder="поиск по сайту ..." v-model="search">
        <button class="cart-button" type="button" v-on:click="searchItemHandler">Искать</button>
        <button class="cart-button" type="button" v-on:click="showUserCart">Ваша Корзина</button>
      </nav>
    </div>
    <div v-if="noError" class="content">
      <div class="item_list" v-on:click="buyItemHandler">
        <item-goods
          v-for="good in filteredItems"
          v-bind:id="good.id_product"
          v-bind:title="good.product_name"
          v-bind:short_desc="good.short_desc"
          v-bind:price="good.price"
        ></item-goods>
      </div>
      <div class="bin"  v-if="isVisibleCart" >
        <div v-if="itemsInBin.length>0" v-on:click= "removeItemHandler">
          <bin v-for="item in itemsInBin"
               v-bind:id="item.id_product"
               v-bind:title="item.product_name"
               v-bind:price="item.price"
          >
          </bin>
        </div>
        <div v-else>Нет товаров</div>
      </div>
    </div>
    <div v-else>
      <p>Error data download</p>
    </div>
  </div>
</template>

<script>
  import list from './List';
  import bin from './bin'
  export default {
    name: 'app',
    data() {
      return {
        items: [],
        itemsInBin: [],
        filteredItems: [],
        search: '',
        isVisibleCart: false,
        noError: true,
        errorString: ''
      }
    },
    methods: {
      searchItemHandler() {
        if (this.search === '') {
          this.filteredItems = this.items;
        }
        const reg = new RegExp(this.search, 'gi');
        this.filteredItems = this.items.filter((elem) => reg.test(elem.product_name));
      },
      showUserCart() {
        this.isVisibleCart = !this.isVisibleCart;
      },
      buyItemHandler(event) {
        if (event.target.tagName !== 'BUTTON') return;
        const id = event.target.dataset.id;
        const item = this.filteredItems.find((elem) => elem.id_product == id);
        fetch('/addItem', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(item)
        })

        fetch('/addItemStat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(item)
        })

        this.itemsInBin.push(item);
      },
      removeItemHandler(event) {
        if (event.target.tagName !== 'BUTTON') return;
        const id = event.target.dataset.id;
        const index = this.itemsInBin.findIndex((el) => el.id_product == id);
        const item = this.filteredItems.find((elem) => elem.id_product == id);

        fetch('/delItem', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(item),
        });

        fetch('/removeItemStat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(item)
        });

        this.itemsInBin.splice(index, 1);
      }
    },
    components:{
      'item-goods':list,
      bin:bin,
    },
    mounted() {
      fetch('/itemList')
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.items = data;
          this.filteredItems = data;
        })
        .catch(err => {
          this.noError = !this.noError;
          this.errorString += err;
        });

      fetch('/userCart')
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.itemsInBin = data;
        })
        .catch(err => {
          this.errorString += err;
        });
    }
  }
</script>

<style scoped>
  * {
    margin: 0;
    padding: 0;
  }

  .item_list {
    margin-top: 50px;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
  }
  .item {
    border: 1px solid;
    text-align: center;
    margin-bottom: 20px;
  }

  .bin {
    margin-top: 50px;
    justify-content: space-around;
    display: flex;
  }
</style>
