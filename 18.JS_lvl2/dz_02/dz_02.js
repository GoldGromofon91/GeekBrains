class dbObject {
    constructor() {
    }

    getDb (){
        return [
            {title:'Goods1', price:111100,short_desc:'Lorem ipsum'},
            {title:'Goods2', price:3300,short_desc:'Lorem ipsum'},
            {title:'Goods3', price:12312312,short_desc:'Lorem ipsum'},
            // {title:'Goods4', price:123123445,short_desc:'Lorem ipsum'},
            // {title:'Goods5', price:454545,short_desc:'Lorem ipsum'},
            // {title:'Goods6', price:6565656,short_desc:'Lorem ipsum'},
            // {title:'Goods7', price:6565656,short_desc:'Lorem ipsum'},
        ];
    }
}

class ItemToBuy {
    constructor(title,price,short_desc) {
        this.itemTitle = title;
        this.itemPrice = price;
        this.shortDescription = short_desc;
    }

    generateHTML () {
        return `<div class="item"><div class="item_img"><img src="img/goods.png" alt=""></div><div class="item_h4">${this.itemTitle}</div><div>${this.itemPrice}</div><div class="item_p">${this.shortDescription}</div>`
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
        this.dataObjects = new dbObject();
        this.itemEnviroment = document.querySelector('.item_list');
        this.binListEnviroment= document.querySelector('.ol');
        this.binCostEnviroment= document.querySelector('.total_cost');
        this.items = [];
        this.cost=0;
    }

    generateItem(){
        this.items = this.dataObjects.getDb().map(({title,price,short_desc}) => new ItemToBuy(title,price,short_desc));
        this.items.forEach((elemGoods) => {this.cost += elemGoods.getCost()})
    }

    renderItem(){
        this.itemEnviroment.textContent='';
        this.items.forEach((element) => {
            this.itemEnviroment.insertAdjacentHTML('beforeend',element.generateHTML())
            this.binListEnviroment.insertAdjacentHTML('beforeend',element.getLi())
        })
        this.binCostEnviroment.insertAdjacentHTML('beforeend',`<p>Total price: ${this.cost}</p>`)
        this.binCostEnviroment.insertAdjacentHTML('afterbegin',`<p>Total product count: ${this.items.length}</p>`)
    }
}


const $start = new GenerateItem()
$start.generateItem()
$start.renderItem()
