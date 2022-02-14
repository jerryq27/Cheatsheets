function factorial(num) {
    if(num === 0) return 1;
    if(num === 1) return num;

    return num *= factorial(num - 1);
}

console.log(factorial(1));
console.log(factorial(2));
console.log(factorial(4));
console.log(factorial(7));