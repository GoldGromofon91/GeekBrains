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
            idGoods: 123,
            imgSrc: 'img/goods.png',
            nameGoods: 'Goods3',
            priceGoods: 5500,
            quantity: 1,
        }],

    initCatalog() {
        this.dataObj.forEach(obj => {
            this.renderElement(obj);
        })
        binUser.init();
    },

    renderElement(obj) {
        const parentBlockGoods = document.querySelector(this.settingCatalog.workEnviroment);
        return parentBlockGoods.insertAdjacentHTML('beforeend',
            `<div class="${this.settingCatalog.itemConteiner}">
                    <img src="${obj['imgSrc']}" alt="">
                    <h4>${obj['nameGoods']}</h4>
                    <p>${obj['priceGoods']}</p>
                    <button class="${this.settingCatalog.buttonBuyGoods}">Buy</button>
                  </div>`);
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
        binElement: [],
    },


    init() {
        this.renderBin();
    },


    renderBin() {
        const parentBinBlock = document.querySelector(this.settingsBin.parentBlock);
        return parentBinBlock.insertAdjacentHTML('beforeend',
            `<div class="${this.settingsBin.binBlockText}">
                      <ol class="${this.settingsBin.elementBinOl}">
                          <li class="${this.settingsBin.elementBinLi}"></li>
                      </ol>
                  </div>
                  <div class="${this.settingsBin.binBlockCost}">
                      <img src="${this.settingsBin.imgBinSrc}" alt="">
                      <p></p>
                  </div>`);
    },
}
//

//     initWorkBlock() {
//         document.querySelectorAll(this.settingCatalog.buttonBuyGoods).forEach(
//             element => {
//                 // console.log(element);
//             element.addEventListener('click', event => {
//                 this.checkClickUser(event)
//             })
//         });
//     },
//     checkClickUser(event) {
//         if(event.target.tagName !== 'BUTTON') return;
//         this.getParam(event);
//
//     },
//
//     getParam(event) {
//         console.log(event)
//     },
// };
catalogUser.initCatalog()
