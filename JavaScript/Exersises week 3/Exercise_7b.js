let a = 1;
let b = 2;
let c = 0
for(let i=0;i<500;i++){
if (a%2===0){
    c=c+a
}
if(b%2===0){
    c=c+b
}
a=b+a;
b=b+a; 
}
console.log(c)