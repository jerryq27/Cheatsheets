function power(baseNum, exp) {
    if(exp === 0) return 1;
    if(exp === 1) return baseNum;

    return baseNum *= power(baseNum, exp - 1);
}

console.log(power(2, 0));
console.log(power(2, 2));
console.log(power(2, 4));
