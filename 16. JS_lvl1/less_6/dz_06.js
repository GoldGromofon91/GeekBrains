/**
 * 1. Доработать модуль корзины.
    a. Добавлять в объект корзины выбранные товары по клику на кнопке «Купить» без перезагрузки страницы
    b. Привязать к событию покупки товара пересчет корзины и обновление ее внешнего вида
    2 *У товара может быть несколько изображений. Нужно:
    a. Реализовать функционал показа полноразмерных картинок товара в модальном окне
    b. Реализовать функционал перехода между картинками внутри модального окна ("листалка")
 */

"use strict";

/**
 *  Что нужно сделать!!!:
 * 1. у нас есть страница с готовыми блоками. нужно на элемент содержащий блоки  получить событие
 * 2. проверить что событие именно кнопка "купить" в блоке товара
 * 3.Создать два блока в блоке div под такую разметку
 * 4. заполнить блоки в таком положении № Наименование | 
                                        № Наименование | Итого: Всего товаров в корзине ... на сумму... 

    
*/
const catalogUser = {
    settingCatalog: {
        workEnviroment: '.catalog_goods',
        itemConteiner: 'item_goods',
        buttonBuyGoods: 'button_items',
    },
    userBin:{},
    dataObj: [
        {
            idGoods: 123,
            imgSrc: 'img/goods.png',
            nameGoods: 'Goods1',
            priceGoods: 23500,
            quantity: 2,
        },
        {
            idGoods: 133,
            imgSrc: 'img/goods.png',
            nameGoods: 'Goods2',
            priceGoods: 24500,
            quantity: 3,
        },
        {
            idGoods: 111,
            imgSrc: 'img/goods.png',
            nameGoods: 'Goods4',
            priceGoods: 1500,
            quantity: 1,
        },
        {
            idGoods: 112,
            imgSrc: 'img/goods.png',
            nameGoods: 'Goods10',
            priceGoods: 24500,
            quantity: 3,
        },
        {
            idGoods: 141,
            imgSrc: 'img/goods.png',
            nameGoods: 'Goods3',
            priceGoods: 5500,
            quantity: 1,
        }],

    initCatalog(userBin) {
        this.userBin = userBin;
        this.dataObj.forEach(obj => {
            this.renderElement(obj);
        })
        this.userBin.initBin(this.dataObj);
        this.clickHandler();
    },

    renderElement(obj) {
        const parentBlockGoods = document.querySelector(this.settingCatalog.workEnviroment);
        return parentBlockGoods.insertAdjacentHTML('beforeend',
            `<div class="${this.settingCatalog.itemConteiner}">
                    <img src="${obj['imgSrc']}" alt="">
                    <h4>${obj['nameGoods']}</h4>
                    <p>${obj['priceGoods']}</p>
                    <button class="${this.settingCatalog.buttonBuyGoods}" data-id_product="${obj['idGoods']}">Buy</button>
                  </div>`);
    },

    clickHandler() {
        const workBlock = document.querySelector(this.settingCatalog.workEnviroment);
        workBlock.addEventListener('click', event => this.addToBin(event));
    },

    addToBin(event) {
        if (!event.target.classList.contains(this.settingCatalog.buttonBuyGoods)) return;
        const id_prod = +event.target.dataset.id_product;
        this.userBin.addToBasket(id_prod);
    },
}
const binUser ={
    settingsBin: {
        parentBlock: '.bin',
        binBlockText: 'block_bin',
        imgBinSrc: 'img/shop.png',
        elementBinOl: 'ol_block_bin',
        elementBinLi: 'li_block_bin',
        binBlockCost: 'block_result_price',
    },
    catalogList: [],
    binElement: [],

    initBin(catalogUser) {
        this.catalogList = catalogUser;
        console.log(this.catalogList);
        this.renderBin();
    },

    renderBin() {
        if (this.binElement.length > 0) {
            this.renderFullBin();
        }else {
            this.renderEmptyBin();
        }
    },

    renderEmptyBin() {
        document.querySelector(`.${this.settingsBin.binBlockText}`).insertAdjacentHTML('beforeend',
            `<p>Cart is empty</p>`);
        document.querySelector(`.${this.settingsBin.binBlockCost}`).insertAdjacentHTML('beforeend',
            `<img src="${this.settingsBin.imgBinSrc}" alt="">
             <p>Result Cost: 0 </p>`)
    },

    renderFullBin() {
        const blockBinText = document.querySelector(`.${this.settingsBin.binBlockText}`);
        blockBinText.innerHTML = '';

        const blockBinCost = document.querySelector(`.${this.settingsBin.binBlockCost}`);
        blockBinCost.innerHTML = '';

        this.binElement.forEach(item => {
            blockBinText.insertAdjacentHTML('beforeend', this.renderCartItem(item));
        });
        blockBinCost.insertAdjacentHTML('beforeend',
            `<img src="${this.settingsBin.imgBinSrc}" alt="">
             <p>Result Cost: ${this.getResultCost()} </p>`)
    },

    renderCartItem(item) {
        return `<p>${item.nameGoods} ${item.priceGoods}</p>`;
    },

    getResultCost(id_product) {
        let result = 0;
        console.log(this.binElement)
        this.binElement.forEach(element => {result+= element.priceGoods})
        return result;

    },
    addToBasket(id_product) {
        const product = this.findProduct(id_product);
        if (product) {
            this.binElement.push({...product});
            this.renderBin();
        }else {
            alert('Ошибка добавления!');
        }
    },

    findProduct(id_product) {
        return this.catalogList.find(product => product.idGoods === id_product);
    },
}

catalogUser.initCatalog(binUser)

