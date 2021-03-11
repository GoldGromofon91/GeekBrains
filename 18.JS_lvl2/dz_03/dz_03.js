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
            // console.log(xhrObject.responseText);
            if (xhrObject.readyState === 4) {
                if(xhrObject.status === 200) {
                    successCallback(JSON.parse(xhrObject.responseText));
                } else if (xhrObject.status > 400) {
                    errorCallback();
                }
            }
        }

        xhrObject.open('GET', this.API_URL, true);
        xhrObject.send();
    }
}

class ItemToBuy {
    constructor(title,price,short_desc) {
        this.itemTitle = title;
        this.itemPrice = price;
        this.shortDescription = short_desc;
    }

    generateHTML() {
        return `<div class="item"><div class="item_img"><img src="img/goods.png" alt="">
                </div><div class="item_h4">${this.itemTitle}</div><div>${this.itemPrice}
                </div><div class="item_p">${this.shortDescription}</div>`
    }

    getLi() {
        return `<li class="li">${this.itemTitle}</li>`
    }

    getCost() {
        return this.itemPrice
    }
}

class GenerateItem {
    constructor() {
        this.apiObject = new apiGetObject();
        this.itemEnviroment = document.querySelector('.item_list');
        this.binListEnviroment = document.querySelector('.ol');
        this.binCostEnviroment = document.querySelector('.total_cost');
        this.items = [];
        this.cost = 0;
        this.apiObject.getObject(this.errorCallback.bind(this),this.successCallback.bind(this));
    }

    successCallback(data) {
        this.items = data.map(({product_name,price,short_desc}) => new ItemToBuy(product_name,price,short_desc));
        this.renderItem();
    }

    errorCallback() {
        this.binCostEnviroment.insertAdjacentHTML('beforeend',`<p>error</p>`);
    }


    renderItem() {
        this.itemEnviroment.textContent = '';
        this.items.forEach((element) => {
            this.itemEnviroment.insertAdjacentHTML('beforeend',element.generateHTML())
            this.binListEnviroment.insertAdjacentHTML('beforeend',element.getLi())
            this.cost += element.itemPrice
        });
        this.binCostEnviroment.insertAdjacentHTML('beforeend',`<p>Total price: ${this.cost}</p>`);
        this.binCostEnviroment.insertAdjacentHTML('afterbegin',`<p>Total product count: ${this.items.length}</p>`);
    }
}



const $start = new GenerateItem()


