// const API_URL = "goods.json";

Vue.component('item-goods',{
    template:'<div class="item"><div class="item_img"><img src="img/goods.png" alt=""></div> <div class="item_h4">{{title}}</div><div>{{short_desc}}</div><div class="item_p">{{price}}</div><button type="button" v-bind:data-id="id">Купить</button></div>',
    props:['id','title','short_desc','price'],
});

Vue.component('err',{
    template:`<h4><slot></slot></h4>`,
});

Vue.component('bin',{
    template:`<div><ul><li><h4>{{title}} - {{price}}</h4><button  v-bind:data-id="id">Удалить</button></li></ul></div>`,
    props:['id','title','price'],
});



const vue = new Vue({
    el: "#app",
    data:{
        items:[],
        itemsInBin:[],
        filteredItems:[],
        search:'',
        isVisibleCart: false,
        noError: true,
        errorString:'',
    },
    methods: {
        searchItemHandler() {
            if(this.search === '') {
                this.filteredItems = this.items;
            }
            const reg = new RegExp(this.search,'gi');
            this.filteredItems = this.items.filter((elem)=>reg.test(elem.product_name));
        },
        showUserCart() {
            this.isVisibleCart = !this.isVisibleCart;
        },
        buyItemHandler(event){
            if(event.target.tagName !=='BUTTON') return;
            const id = event.target.dataset.id;
            const item = this.filteredItems.find((elem)=> elem.id_product == id);

            fetch('/addItem', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(item)
            });
            fetch('/addItemStat');

            this.itemsInBin.push(item);
        },
        removeItemHandler(event){
            if(event.target.tagName !=='BUTTON') return;
            const id = event.target.dataset.id;
            const index = this.itemsInBin.findIndex((el)=> el.id_product == id);
            const item = this.filteredItems.find((elem)=> elem.id_product == id);

            fetch('/delItem', {
                method: 'POST',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify(item),
            });


            this.itemsInBin.splice(index,1);

        }
    },
    mounted(){
        fetch('/itemList')
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                this.items = data;
                this.filteredItems = data;
            })
            .catch(err=> {
                this.noError = !this.noError;
                this.errorString += err;
            });

        fetch('/userCart')
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                this.itemsInBin = data
            })
            .catch(err=> {
                this.errorString += err;
            });
    }
})
