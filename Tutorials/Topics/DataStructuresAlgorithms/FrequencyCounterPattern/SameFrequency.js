/**
 * Given two positive integers, find out if the two numbers have the same
 * frequency of digits. 
 * 
 * Pattern: Frequency Counter Pattern
 */
 function sameFrequency(num1, num2) {
    let freq1 = {};
    let freq2 = {};

    let numStr1 = num1.toString();
    let numStr2 = num2.toString();

    for(let char of numStr1) {
        freq1[char] = ((freq1[char]) || 0) + 1;
    }
    for(let char of numStr2) {
        freq2[char] = ((freq2[char]) || 0) + 1;
    }

    for(let key in freq1) {
        if(!(key in freq2)) {
            return false;
        }
    }
    for(let key in freq1) {
        if(freq1[key] !== freq2[key]) {
            return false;
        }
    }
    return true;
}

// console.log(sameFrequency(182, 281));
// console.log(sameFrequency(34, 14));
// console.log(sameFrequency(3589578, 5879385));
// console.log(sameFrequency(22, 222));
