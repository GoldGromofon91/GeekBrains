"use strict"

window.onload = function () {
    console.log('DOM ready');
    $('.basket_record').on('change', "input[type='number']", function (event) {
        console.log(event.target);
        let countItem = event.target.value;
        let elementPK = event.target.name;
        console.log('id- ', elementPK, 'Count- ',countItem)
        //TODO
    });
}