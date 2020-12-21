'use strict';

//Задание №1
/** Написать функцию, преобразующую число в объект. 
 * Передавая на вход число от 0 до 999, мы должны 
 * получить на выходе объект, в котором в соответствующих 
 * свойствах описаны единицы, десятки и сотни. 
 * Например, для числа 245 мы должны получить следующий 
 * объект: {‘единицы’: 5, ‘десятки’: 4, ‘сотни’: 2}. 
 * Если число превышает 999, необходимо выдать 
 * соответствующее сообщение с помощью console.log 
 * и вернуть пустой объект.*/

 function SplittingNumber(){
     let usrNumb = prompt('Введите число от 0 до 999: ');
     let unit=0;
     let doz=0;
     let hund=0;
     switch(usrNumb.length) {
         case 1:
             unit = +usrNumb;
             break;
        case 2:
            unit = Math.floor(+usrNumb % 10);
            doz = Math.floor(+usrNumb / 10 % 10);
            break;
        case 3:
            unit = Math.floor(+usrNumb % 10);
            doz = Math.floor(+usrNumb / 10 % 10);
            hund = Math.floor(+usrNumb /100 % 10);
            break;
        default:
            alert('Введите число от 0 до 999')
     }
    return {
        units: unit,
        dozens: doz,
        hundreds: hund,
    }
 }
 let numb = SplittingNumber();
 console.log(numb);

 // Задание 2
/**
 * Для игры, реализованной на уроке, реализовать ограничение 
 * по полю
 */

const settings = {
    rowsCount: 10,
    colsCount: 10,
    startPositionX: 5,
    startPositionY: 5,
};
const player = {
    x: null,
    y: null,

    init(startX, startY) {
        this.x = startX;
        this.y = startY;
    },

    move(nextPoint) {
        this.x = nextPoint.x;
        this.y = nextPoint.y;
    },

    NextStepPosition(direction) {
        const nextPosition = {
            x: this.x,
            y: this.y,
        };

        switch (direction) {
          case 2:
            nextPosition.y++;
            break;
          case 4:
            nextPosition.x--;
            break;
          case 6:
            nextPosition.x++;
            break;
          case 8:
            nextPosition.y--;
            break;
        }
        return nextPosition;
      },
    };

const game = {
    settings,
    player,
        
    run() {
        this.player.init(this.settings.startPositionX, this.settings.startPositionY);

        while (true) {
            this.render();
            const direction = this.getDirection();
            if (direction === -1) {
                alert('До свидания.');
            return;
            }
        
            const nextPoint = this.player.NextStepPosition(direction);
            if (this.checkNextPlayerStep(nextPoint)) {
                this.player.move(nextPoint);
            }else{
                alert('Граница поля!')
            }
        }
      },
    
    render() {
        let map = "";
        for (let row = 0; row < this.settings.rowsCount; row++) {
            for (let col = 0; col < this.settings.colsCount; col++) {
                if (this.player.y === row && this.player.x === col) {
                    map += 'o ';
                } else {
                    map += 'x ';
                }
            }
            map += '\n';
        }

        console.clear();
        console.log(map);
      },

    getDirection() {
        const availableDirections = [-1, 2, 4, 6, 8,];
        while (true) {
          let direction = parseInt(prompt('Введите числa 2,4,6,8 для перемещения\nВведите -1 для выхода.'));
          if (!availableDirections.includes(direction)) {
            alert('Для перемещения необходимо ввести одно из чисел: 2,4,6,8');
            continue;
          }

          return direction;
        }
      },

    checkNextPlayerStep(nextPoint) {
        return nextPoint.x >= 0 &&
          nextPoint.x < this.settings.colsCount &&
          nextPoint.y >= 0 &&
          nextPoint.y < this.settings.rowsCount;
      },
    };

game.run();

// Задание 3
/**
 * 3.1. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими объектами можно заменить их элементы?
3.2. Реализуйте такие объекты.
3.3. Перенести функционал подсчета корзины на объектно-ориентированную базу.
 */

const bin={
    items:[],
    price:[],
    resultCost:0,

    Cost(user_items){
        for(let i = 0; i < user_items.length; i++) {
            this.items.push(user_items[i][0]);
            this.price.push(user_items[i][1]);
        };
        for (let i =0; i < this.price.length; i++){
            this.resultCost += this.price[i];
        };
    },
};

let user1 = bin;
let user2 = {...bin};
user1.Cost([['prod_1',23500],['prod_2',11300],['prod_3',11230]]);
console.log(user1.resultCost);
user2.Cost([['prod_1',23500],['prod_2',11300],['prod_3',11230],['prod_4',10000]]);
console.log(user2.resultCost);
