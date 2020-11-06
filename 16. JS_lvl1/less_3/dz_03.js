'use strict';
// Задание 1
// 1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.
// n>1 - простое если делится только на себя и единицу без остатка
const numb = 100;
let n = 2;
let arr = [];
while (n <= numb){
    // console.log('n' +n);
    let i = 2;
    let res_prime = 2;
    // console.log('i'+ i);
    // console.log('res'+res_prime)
    while(n % i !==0){
        i +=1;
        res_prime +=1;
    }
    if (res_prime == n){
        arr.push(res_prime)
    }
    n++;
} 
console.log('Task_1');
console.log(arr);

// Задание 2
/**
Hеализовать функционал подсчета стоимости корзины в зависимости от 
находящихся в ней товаров. Товары в корзине хранятся в массиве. Задачи:
a) Организовать такой массив для хранения товаров в корзине;
b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины.
 */
console.log('Task_2');
let bin = [['prod_1',23500],['prod_2',11300],['prod_3',11230]];
let bin_1 = [['prod_1',23500],['prod_2',11300],['prod_3',11230],['prod_4',10000]];
function countBasketPrice(user_bin){
    let result = 0;
    let resSum = 0;
    for (let i =0; i < user_bin.length;i++){
        result +=user_bin[i][1];
    }
    return result;    
}
console.log('User_1_bin: ');
console.log(bin);
console.log('User_2_bin: ');
console.log(bin_1);
console.log('Total cost User_1_bin ' + countBasketPrice(bin));
console.log('Total cost User_2_bin ' + countBasketPrice(bin_1));


// Задание 3
// *Вывести с помощью цикла for числа от 0 до 9, не используя тело цикла.
console.log('Task_3');
function withoutBody(){
    let wbStr ='';
    for (let wb = 0; wb < 10; wbStr+=wb,wb++);
    console.log(wbStr);
}

withoutBody();

// Задание 4
// **Нарисовать пирамиду с помощью console.log, 
// как показано на рисунке, только у вашей пирамиды должно быть 20 рядов, а не 5:
console.log('Task_4');

function treeArray(){
    let treeArr = [];
    let st = 1;
    while (st <= 20){
        treeArr.push('*');
        console.log(treeArr);
        st++;
    }
}

function treeString(){
    let treeStr = '';
    for (let i = 0; i <20;i++){
        for (let j = 0; j<i; j++){
            treeStr+='*';
            console.log(treeStr);
        }
        treeStr+="\n";
        console.log(treeStr);
    }
}
treeArray();
// treeString();  реализация через строку, правда не сообразил как лучше сделать вывод результирующий