let re = /^"|(\s)"|"(\s)|"$/gm;
let $1 = "asdasdasdsd aren't dsdsda123sdzxc";
let $2 = "isn't, i'm not,dasdasd";
let newstr = $1.replace(re,"'");
let newstr2 = $2.replace(re,"'");
console.log(newstr);
console.log(newstr2);


