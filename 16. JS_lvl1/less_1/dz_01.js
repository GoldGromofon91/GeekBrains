// Задание №1
let usr_obj = prompt('Введите температуру в C: ');
usr_obj = parseFloat(usr_obj);
if (isNaN(usr_obj)) {
    alert ('Ошибка ввода!\nВведите в формате "36.6"');
} else{
    let temperatureFarengeit = (9 / 5) * usr_obj + 32;
    alert('Температура в F:\n'+ temperatureFarengeit.toFixed(3));
    console.log(temperatureFarengeit.toFixed(3));
}

// Задание №2

let name = 'Василий';
console.log(name);
document.write('name = ' + name + '<br>');
let admin = name;
console.log(admin);
document.write('admin= ' + admin + '<br>');

// Задание №3

document.write('res = ' + (1000 + '108') + ' type res: ' + typeof(1000 + '108')); 
console.log(1000 + '108');