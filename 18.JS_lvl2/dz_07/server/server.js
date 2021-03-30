const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');
const $port = 8080;

const servApp = express();

servApp.use(express.static('./public'));
servApp.use(bodyParser.json());

servApp.listen($port,()=>{
    console.log(`server listen ${$port}`)
});

servApp.get('/itemList', (req, res) => {
    fs.readFile('./server/goods.json', 'utf-8', (err, data) => {
        if(!err) {
            res.end(data);
        } else {
            console.log(err);
        }
    })
});

servApp.get('/userCart', (req, res) => {
    fs.readFile('./server/cartgoods.json', 'utf-8', (err, data) => {
        if(!err) {
            res.end(data);
        } else {
            console.log(err);
        }
    })
});


servApp.post('/addItem',bodyParser.json(),(req, res) => {
    fs.readFile('./server/cartgoods.json','utf-8',(err,data)=>{
        const cart = JSON.parse(data);
        const item = req.body;
        cart.push(item)

        fs.writeFile('./server/cartgoods.json', JSON.stringify(cart),(err)=>{
            console.log('File is writing');
        })
    })
})

servApp.post('/delItem',bodyParser.json(),(req, res) => {
    fs.readFile('./server/cartgoods.json','utf-8',(err,data)=>{
        const cart = JSON.parse(data);
        const itemToDel = req.body;
        cart.splice(cart.findIndex((el)=>el.id_product == itemToDel.id_product),1)

        fs.writeFile('./server/cartgoods.json', JSON.stringify(cart),(err)=>{
            console.log(`Objects with id -${itemToDel.id_product}, title-${itemToDel.product_name} deleted`);
        });
    });
})

servApp.post('/addItemStat',bodyParser.json(),(req, res) => {
    fs.readFile('./stats.json','utf-8',(err,data)=>{
        const logUser = JSON.parse(data);
        const item = req.body;
        const date = new Date();

        logUser.push(`id- ${item.id_product}, title - ${item.product_name}, add in -  ${date}`)
        fs.writeFile('./stats.json', JSON.stringify(logUser),(err)=>{
            console.log('File is writing');
        })
    })
})

servApp.post('/removeItemStat',bodyParser.json(),(req, res) => {
    fs.readFile('./stats.json','utf-8',(err,data)=>{
        const logUser = JSON.parse(data);
        const item = req.body;
        const date = new Date();

        logUser.push(`id- ${item.id_product}, title - ${item.product_name}, remove in -  ${date}`)
        fs.writeFile('./stats.json', JSON.stringify(logUser),(err)=>{
            console.log('File is writing');
        })
    })
})