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
const pageUser = {
    settingCatalog: {
        workEnviroment: '.catalog_goods',
        itemConteiner: '.item_goods',
        buttonBuyGoods: '.button_items',
    },

    settingsBin: {
        binBlockText: '.block_bin',
        elementBinOl: '.ol_block_bin',
        elementBinLi: '.li_block_bin',
        binBlockCost: '.block_result_price',
    },


    initWorkBlock() {
        document.querySelectorAll(this.settingCatalog.buttonBuyGoods).forEach(
            element => {
                console.log(element);
            addEventListener('click', event => {
                this.checkClickUser(event)
            })
        });
    },
    checkClickUser(event) {
        if(event.target.tagName !== 'BUTTON') return;
        this.getParam(event);

    },

    getParam(event) {
        console.log(event.target)
    },
};
pageUser.initWorkBlock()