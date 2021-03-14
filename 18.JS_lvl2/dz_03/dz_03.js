class apiGetObject {
    constructor() {
        this.API_URL = "goods.json";
    }

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
                    errorCallback();
                }
            }
        }

        xhrObject.open('GET', this.API_URL, true);
        xhrObject.send();
    }

    getObjPromise() {
        return new Promise((resolve, reject) =>{
            this.getObject(reject,resolve)
        });
    }
}

class ItemToBuy {
    constructor(title,price,short_desc,id) {
        this.itemTitle = title;
        this.itemPrice = price;
        this.shortDescription = short_desc;
        this.itemId = id;
    }

    generateHTML() {
        return `<div class="item"><div class="item_img"><img src="img/goods.png" alt="">
                </div><div class="item_h4">${this.itemTitle}</div><div>${this.itemPrice}
                </div><div class="item_p">${this.shortDescription}</div>`;
    }

    getCost() {
        return this.itemPrice;
    }
}

class GenerateItem {
    constructor() {
        this.apiObject = new apiGetObject();
        this.itemEnviroment = document.querySelector('.item_list');
        this.binListEnviroment = document.querySelector('.ol');
        this.binCostEnviroment = document.querySelector('.total_cost')
        this.items = [];
        this.itemsInBin = [];
        this.cost = 0;

        let itemPromise = this.apiObject.getObjPromise()
        itemPromise
            .then((data) => {this.successCallback(data)})
            .catch(()=>{this.errorCallback()})
    }

    successCallback(data) {
        data.forEach((obj) => {
            let {product_name,price,short_desc,id_product} = obj;
            this.items.push(new ItemToBuy(product_name,price,short_desc,id_product));
        });
        this.renderItem();
    }

    errorCallback() {
        this.binCostEnviroment.insertAdjacentHTML('beforeend',`<p>error</p>`);
    }

    buyItem (id) {
        const product = this.findProductForId(id);
        if (product){
            this.itemsInBin.push({...product});
            this.renderBinItem();
        } else {
            alert('Ошибка покупки');
        }
    }

    deleteItem(id){
        console.log(this.itemsInBin.length)
        if (this.findProductForId(id)) {
            const index = this.itemsInBin.indexOf(this.itemsInBin.find(el=>el.itemId===id))
            this.itemsInBin.splice(index,1)
            this.renderBinItem();
        }
    }

    getLi() {
        this.itemsInBin.forEach((el)=>console.log(el));
    }

    findProductForId(id_prod) {
        return this.items.find(obj => obj.itemId === id_prod);
    }

    renderItem() {
        this.itemEnviroment.textContent = '';
        this.items.forEach((element) => {
            this.itemEnviroment.insertAdjacentHTML('beforeend',element.generateHTML());
        });
    }

    renderBinItem() {
        this.binCostEnviroment.text_content='';
        this.binListEnviroment.text_content='';
        this.cost = 0;
        this.itemsInBin.forEach((element) => {
            this.binListEnviroment.insertAdjacentHTML('beforeend',`<li class="li">${element.itemTitle}</li>`);
            this.cost += element.itemPrice;
        });
        this.binCostEnviroment.insertAdjacentHTML('beforeend',`<p>Total price: ${this.cost}</p>`);
        this.binCostEnviroment.insertAdjacentHTML('afterbegin',`<p>Total product count: ${this.itemsInBin.length}</p>`);
    }
}

const $start = new GenerateItem()
//Якобы "Событие клик"
setTimeout(()=>$start.buyItem(1),1000);
setTimeout(()=>$start.buyItem(2),1000);
setTimeout(()=>$start.deleteItem(1),10000);
setTimeout(()=>$start.getLi(),10000);