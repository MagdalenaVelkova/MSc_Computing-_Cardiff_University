let sum=0;
inputNumber=window.prompt("Input your number and watch the magic happen..");
while(inputNumber!=0){
    sum=sum+inputNumber%10;
    inputNumber=(inputNumber-inputNumber%10)/10
}

console.log(sum);
