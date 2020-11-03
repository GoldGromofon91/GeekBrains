// // Задание №1
var a = 1, b = 1, c, d;
c = ++a; 
alert(c); // Оператор инкримента с префиксной формой - возвращает новое значение A, увелич на 1

d = b++; 
alert(d); // Оператор инкримента с постфиксной формой - увеличивает на ед-цу значение , но возвращает старое значение(до увеличения/уменьшения)

c = (2+ ++a); 
alert(c);      // a = 2, -> ++a = 3-> c = 2 + 3

d = (2+ b++); 
alert(d);   // b = 2-> b++ = 3, но вернет значение до увеличения(2)-> d =4
alert(a);                    // 3
alert(b);                    // 3

// Задание №2
/** 
 * В JS есть строгий приоритет операций, при этом присваивание = возвразает значение.
 * Поэтому сначала выполним операцию присвания с операндом А, затем операцию сложения, затем операцию присваивания
*/
var a = 2;
var x = 1 + (a *= 2); //  x = 1 + (a = a * 2) = 5
alert('x: ' + x)

// Задание №3.
/*
Объявить две целочисленные переменные a и b и задать им произвольные начальные значения. Затем написать скрипт, который работает по следующему принципу:
если a и b положительные, вывести их разность;
если а и b отрицательные, вывести их произведение;
если а и b разных знаков, вывести их сумму; ноль можно считать положительным числом. 
*/

var a = -10;
var b = 45;
var res;
alert('Переменные:\n' + 'a = '+ a +'\t'+'b = '+b)
if (a > 0 && b > 0) {
    res = a - b;
    alert('Разность = ' + res)
} else if ( a < 0 && b < 0) {
    res = a * b;
    alert('Произведение = ' + res)
}else {
    res = a + b;
    alert('Сложение = ' + res)
}

// Задание №4
/*
Присвоить переменной а значение в промежутке [0..15]. 
С помощью оператора switch организовать вывод чисел от a до 15. 
*/

userNumber = + prompt('Введите число от 0...15')
if (isNaN(userNumber)) {
    alert('Ошибка\n Введите число от 0...15');
}else if ( userNumber < 0 || userNumber > 15) {
    alert('Ошибка\n Введите число от 0...15');
}
switch (userNumber){
    case 0:
        console.log(userNumber);
        userNumber +=1;
    case 1:
        console.log(userNumber);
        userNumber +=1;
    case 2:
        console.log(userNumber);
        userNumber +=1;
    case 3:
        console.log(userNumber);
        userNumber +=1;
    case 4:
        console.log(userNumber);
        userNumber +=1;
    case 5:
        console.log(userNumber);
        userNumber +=1;
    case 6:
        console.log(userNumber);
        userNumber +=1;
    case 7:
        console.log(userNumber);
        userNumber +=1;
    case 8:
        console.log(userNumber);
        userNumber +=1;
    case 9:
        console.log(userNumber);
        userNumber +=1;
    case 10:
        console.log(userNumber);
        userNumber +=1;
    case 11:
        console.log(userNumber);
        userNumber +=1;
    case 12:
        console.log(userNumber);
        userNumber +=1;
    case 13:
        console.log(userNumber);
        userNumber +=1;
    case 14:
        console.log(userNumber);
        userNumber +=1;
    case 15:
        console.log(userNumber);
        break;
}

// Задание №5
/*
 * Реализовать основные 4 арифметические операции в виде функций с двумя параметрами. Обязательно использовать оператор return.
 */

 function mySum(num1,num2){
    let res; 
    return res = num1 + num2;
 }

 function myDiff(num1,num2){
    let res; 
    return res = num1 - num2;
 }

 function myPro(num1,num2){
    let res; 
    return res = num1 * num2;
 }

 function myDiv(num1,num2){
    let res;
    if (num2 == 0){
        alert('На ноль делить нельзя');
        return null;
    }else{
        return res = num1 / num2;
    }
 }

 console.log(mySum(2,5))
 console.log(myDiff(2,5))
 console.log(myPro(2,5))
 console.log(myDiv(2,0))

// Задание №6
/*
Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation), 
где arg1, arg2 – значения аргументов, operation – строка с названием операции. 
В зависимости от переданного значения операции выполнить одну из арифметических операций 
(использовать функции из пункта 3) и вернуть полученное значение (использовать switch).
*/

function mathOperation(arg1,arg2,operation = '') {
    let result;
    if (!operation){
        alert('Операция не введена!')
        return null
    }
    console.log('Операция: '+ operation);
    switch (operation.toLowerCase()) {
        case 'сложение':
            result = mySum(arg1,arg2);
            return console.log('Result = ' + result);
        case 'разность':
        case 'вычитание':
            result = myDiff(arg1,arg2);
            return console.log('Result = ' + result);
        case 'умножение':
        case 'произведение':
            result = myPro(arg1,arg2);
            return console.log('Result = ' + result);   
        case 'деление':
            result = myDiv(arg1,arg2);
            return console.log('Result = ' + result);  
        default:
            alert('Неизвестная операция');
            return null;
    }
}

mathOperation(2,5,'сложение');
mathOperation(2,5,'разность');
mathOperation(5,2,'вычитание');
mathOperation(2,5,'умножение');
mathOperation(2,5,'произведение');
mathOperation(5,2,'деление');

//Задание №7
/*
Сравнить null и 0. Попробуйте объяснить результат.
 */
 alert (null == 0 ) // - false
/*
Все дело в особенностях языка  JS и использовании сравнений и строгий равенств и нестрогих равенст ==
При использовании нестрогих равенств nul и undefined не преобразу/тся к нулю, они равны друг другу и не равны ничему другому
*/

// Задание №8
/*
8. *С помощью рекурсии организовать функцию возведения числа в степень. 
Формат: function power(val, pow), где val – заданное число, pow – степень.
*/

function power(val,pow) {
    if (pow == 1){
        return val;
    }else {
        return val * power(val,pow - 1);
    }
}

alert(power(2,8));