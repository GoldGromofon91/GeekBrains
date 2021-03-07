class Burger {
    constructor() {
        this.burgerSize = ['big','small'];
        this.burgerType = ['cheese', 'salad','potato'];
        this.burgerPriceCcalObject = {
            burgerSizePriceCcal: {
                big: [100,40],
                small:[50,20],
            },

            burgerTypePriceCcal: {
                cheese: [10,20],
                salad:[20,5],
                potato:[15,10],
            },

            burgerToppingPriceCcal: {
                paprika:[15,0],
                mayonnaise:[20,5],
            }
        }
    }
}

class Shop {
    constructor(usrSize,usrType) {
        this.burger = new Burger();
        this.burgerPrice = 0;
        this.burgerCcal = 0;
        this.userChoiceSize = usrSize;
        this.userChoiceType = usrType;
        this.flag = this.getInit();
        this.topping = '';
    }

    getInit() {
        if(this.burger.burgerSize.includes(this.userChoiceSize) && this.burger.burgerType.includes(this.userChoiceType)){
            console.log('Order is OK');
            this.burgerPrice += this.burger.burgerPriceCcalObject.burgerSizePriceCcal[this.userChoiceSize][0] + this.burger.burgerPriceCcalObject.burgerTypePriceCcal[this.userChoiceType][0];
            this.burgerCcal += this.burger.burgerPriceCcalObject.burgerSizePriceCcal[this.userChoiceSize][1] + this.burger.burgerPriceCcalObject.burgerTypePriceCcal[this.userChoiceType][1];
            return true
        }else {
            console.log('Order is incorrect');
            return false
        }
    }


    getSize() {
        console.log(`Size your hamburger: ${this.userChoiceSize}`)
        return this.userChoiceSize
    }

    getStuffing() {
        console.log(`Your stuffing in  hamburger: ${this.userChoiceType}`)
        return this.userChoiceType
    }

    getToppingList() {
        console.log(`Topping list: ${Object.keys(this.burger.burgerPriceCcalObject.burgerToppingPriceCcal).join(',')}`)
    }

    getMyTopping(){
        console.log(this.topping)
        return this.topping
    }

    getPriceBurger() {
        console.log(`Price your burger: ${this.burgerPrice} P`)
        return this.burgerPrice
    }

    getCcalBurger() {
        console.log(`Ccal your burger: ${this.burgerCcal} cal`)
    }
    addTopping(topping) {
        if (!this.flag) return false;
        if (!this.burger.burgerPriceCcalObject.burgerToppingPriceCcal[topping]) return false;
        this.topping += topping;
        this.burgerPrice += this.burger.burgerPriceCcalObject.burgerToppingPriceCcal[topping][0];
        this.burgerCcal += this.burger.burgerPriceCcalObject.burgerToppingPriceCcal[topping][1];

    }

    removeTopping(topping) {
        this.topping += '';
        this.burgerPrice -= this.burger.burgerPriceCcalObject.burgerToppingPriceCcal[topping][0];
        this.burgerCcal -= this.burger.burgerPriceCcalObject.burgerToppingPriceCcal[topping][1];
    }
}

const $usrBuy1= new Shop('big','cheese');
$usrBuy1.getPriceBurger()
$usrBuy1.getCcalBurger()
$usrBuy1.addTopping('paprika')
$usrBuy1.getPriceBurger()
$usrBuy1.getCcalBurger()
$usrBuy1.getSize()
$usrBuy1.getStuffing()
$usrBuy1.getMyTopping()
$usrBuy1.getToppingList()
$usrBuy1.removeTopping('paprika')
$usrBuy1.getPriceBurger()
$usrBuy1.getCcalBurger()
