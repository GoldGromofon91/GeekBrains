const API_URL = "goods.json";
const vue = new Vue({
    el: "#app",
    data:{
        items:[],
        itemsInBin:[],
        filteredItems:[],
        search:'',
        isVisibleCart: false,
    },
    methods: {
        getObject (errorCallback,successCallback) {
            let xhrObject;
            if (window.XMLHttpRequest) {
                xhrObject = new XMLHttpRequest();
            } else if (window.ActiveXObject) {
                xhrObject = new ActiveXObject('Microsoft.XMLHTTP');
            }

            xhrObject.onreadystatechange = function () {
                if (xhrObject.readyState === 4) {
                    if(xhrObject.status === 200) {
                        successCallback(JSON.parse(xhrObject.responseText));
                    } else if (xhrObject.status >= 400) {
                        errorCallback('Error download data');
                    }
                }
            }
            xhrObject.open('GET', API_URL, true);
            xhrObject.send();
        },

        getObjPromise() {
            return new Promise((resolve, reject) =>{
                this.getObject(reject,resolve);
            });
        },
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
            const id = +event.target.dataset.id;
            const item = this.filteredItems.find((elem)=> elem.id_product === id);
            this.itemsInBin.push(item);
        },
        removeItemHandler(event){
            if(event.target.tagName !=='BUTTON') return;
            const id = +event.target.dataset.id;
            const index = this.itemsInBin.findIndex((el)=> el.id_product === id);
            this.itemsInBin.splice(index,1);
        }
    },
    mounted(){
        this.getObjPromise()
            .then(data => {
                this.items = data;
                this.filteredItems = data;
            })
            .catch(err=> {
                console.log(err);
            })
    }
})
