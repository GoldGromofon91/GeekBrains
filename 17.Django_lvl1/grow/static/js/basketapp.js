"use strict"

window.onload = function () {
    $('.basket_record').on('change', "input[type='number']", function (event) {
        let elItemCount = event.target.value;
        let elItemPK = event.target.name;
        $.ajax({
            url: "/basket/edit/" + elItemPK + "/" + elItemCount + "/",
            success: function (data_obj) {
                if (data_obj.status) {
                    $('.basket_summary').html(data_obj.basket_summary);
                    $('.product_cost').html(data_obj.basket_cost);
                }
            },
        });
    });
}