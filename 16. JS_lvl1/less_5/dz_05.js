"use strict";
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
function generatorTable() {
  const content = document.querySelector(".content");
  const word = ["A", "B", "C", "D", "E", "F", "G", "H"];

  for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
      const celda = document.createElement("div");
      celda.style.height = "50px";
      celda.style.width = "50px";
      celda.style.border = "1px solid black";

      (j % 2 == 1 && i % 2 == 1) || (j % 2 == 0 && i % 2 == 0)
        ? (celda.style.backgroundColor = "black")
        : (celda.style.backgroundColor = "white");

      if (i === 0 && j < 10) {
        celda.style.backgroundColor = "#6f4e37";
        if (1 <= j && j < 9) {
          celda.textContent = j;
        }
      } else if (i === 9 && j < 10) {
        celda.style.backgroundColor = "#6f4e37";
        if (1 <= j && j < 9) {
          celda.textContent = j;
        }
      } else if (i < 10 && j === 0) {
        celda.style.backgroundColor = "#6f4e37";
        if (0 <= i && i < 9) {
          celda.textContent = word[i - 1];
        }
      } else if (i < 10 && j === 9) {
        celda.style.backgroundColor = "#6f4e37";
        if (0 <= i && i < 9) {
          celda.textContent = word[i - 1];
        }
      }
      content.appendChild(celda);
    }
  }
}

generatorTable();

/* 3. Сделать генерацию корзины динамической: верстка корзины не должна находиться в HTML-структуре.
 *  Там должен быть только div, в который будет вставляться корзина, сгенерированная на базе JS: */

const data_obj = [
  ["prod_1", 23500],
  ["prod_2", 23500],
  ["prod_3", 23500],
  ["prod_5", 23500],
  ["prod_6", 11300],
  ["prod_7", 11230],
  ["prod_8", 10000],
];
const bin = {
  costGoods(user_items) {
    let res = 0;
    for (let i = 0; i < user_items.length; i++) {
      res += user_items[i][1];
    }
    return res;
  },

  renderGoods(data) {
    let bin_2 = document.querySelector(".bin_1");
    data.length > 0
      ? bin_2.insertAdjacentHTML(
          "afterbegin",
          `<div><p>В корзине ${data.length} товаров(а), на сумму ${this.costGoods(data)}</p></div>`
          )
      : bin_2.insertAdjacentHTML(
          "afterbegin",
          `<div><p>В корзине пусто</p></div>`
        );
  },
};

bin.renderGoods(data_obj);

/**
 * 4*. Сделать так, чтобы товары в каталоге выводились при помощи JS:
 */
function renderBin2(products) {
  const bin_2 = document.querySelector(".bin_2");
  product.forEach((elem) => {
    bin_2.insertAdjacentHTML(
      "beforeend",
      `<div><h4>${elem[0]}</h4><p>${elem[1]}</p></div>`
    );
  });
}

const product = [
  ["Good1", 15000],
  ["Good2", 13000],
  ["Good3", 10000],
  ["Good4", 20000],
];

renderBin2(product);
