'use strict'
/*
 * 1. Создать функцию, генерирующую шахматную доску. 
 * При этом можно использовать любые html-теги по своему желанию. 
 * Доска должна быть разлинована соответствующим образом, 
 * т.е. чередовать черные и белые ячейки. 
 * Строки должны нумероваться числами от 1 до 8, 
 * столбцы – латинскими буквами A, B, C, D, E, F, G, H.

    2*. Заполнить созданную таблицу буквами, отвечающими за шахматную фигуру, 
    например К – король, Ф – ферзь и т.п.,
 */
function generatorTable(){
    const content = document.querySelector('.content')
    const word = ['A','B','C','D','E','F','G','H']

    for (let i = 0 ; i < 10; i++){
        for (let j = 0; j < 10; j++){
            const celda = document.createElement('div')
            celda.style.height='50px';
            celda.style.width='50px';
            celda.style.border = '1px solid black';

            (j % 2 == 1 && i % 2 == 1) || (j % 2 == 0 && i%2 == 0) ? celda.style.backgroundColor = 'black' : celda.style.backgroundColor = 'white'
            
            if (i === 0 && j < 10){
                celda.style.backgroundColor = '#6f4e37';
                if (1 <= j && j < 9) {
                    celda.textContent = j;
                }
            }else if (i === 9 && j < 10){
                celda.style.backgroundColor = '#6f4e37';
                if (1 <= j && j < 9) {
                    celda.textContent = j;
                }
            }else if(i < 10 && j === 0){
                celda.style.backgroundColor = '#6f4e37';
                if (0 <=i && i < 9) {
                    celda.textContent = word[i-1]
                }
            }else if(i < 10 && j === 9){
                celda.style.backgroundColor = '#6f4e37';
                if (0 <=i && i < 9) {
                    celda.textContent = word[i-1]
                }
            }
            content.appendChild(celda)
        }
    }
};

generatorTable();

/* 3. Сделать генерацию корзины динамической: верстка корзины не должна находиться в HTML-структуре.
 *  Там должен быть только div, в который будет вставляться корзина, сгенерированная на базе JS: */

const bin={
    items:[],
    price:[],
    resultCost:0,
    
    
    Cost(user_items){
        this.items = []
        this.price = []
        for(let i = 0; i < user_items.length; i++) {
            this.items.push(user_items[i][0]);
            this.price.push(user_items[i][1]);
        };
        for (let i =0; i < this.price.length; i++){
            this.resultCost += this.price[i];
        };
    },
    
    Render(){
        const content= document.querySelector('.bin_1');
        const block = document.createElement('div');
        const pTag = document.createElement('p');
        if (this.items.length !== 0 ){
            pTag.textContent = `В корзине: ${this.items.length} элемента(ов), на сумму ${this.resultCost}`;
        }else{
            pTag.textContent = 'Корзина пуста';
        }
        block.appendChild(pTag)
        content.appendChild(block);
    },
}

let user1 = bin;
let user2 = {...bin};
let user3 = {...bin};
user1.Cost([['prod_1',23500],['prod_2',11300],['prod_3',11230]]);
user2.Cost([['prod_1',23500],['prod_2',11300],['prod_3',11230],['prod_4',10000]]);
user1.Render();
user2.Render();
user3.Render();
/**
 * 4*. Сделать так, чтобы товары в каталоге выводились при помощи JS:
 */
function Render_bin2(products){
    const bin_2 = document.querySelector('.bin_2')
    product.forEach((elem) =>{
        const block = document.createElement('div')
        block.style.width= '80px';
        block.style.height= '80px';
        block.style.border = '1px solid black';
        block.style.backgroundColor = 'white';
        const h4TagBlock = document.createElement('h4')
        const pTagBlock = document.createElement('p')
        h4TagBlock.textContent = elem[0];
        pTagBlock.textContent = elem[1];
        block.appendChild(h4TagBlock);
        block.appendChild(pTagBlock)
        bin_2.appendChild(block)
    })


};
 const product = [['Good1', 15000],['Good2',13000],['Good3',10000],['Good4',20000]]

Render_bin2(product)
