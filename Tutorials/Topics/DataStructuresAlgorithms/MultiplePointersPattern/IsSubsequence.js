/**
 * Write a function that takes in two strings and checks whether the characters
 * in the first string for a subsequence in the second string. In other words,
 * the function should check whether the characters in the first string appear
 * somewhere in the second string, without their order changing.
 * 
 * Pattern: Multiple Pointers Pattern
 */

/* My solution */
function isSubsequence(subStr, fullStr) {
    if(subStr.length === 0 || fullStr.length === 0) return false;

    let subCounter = 0;
    let fullCounter = 0;

    let solutionCounter = 0;

    while(fullCounter < fullStr.length) {
        if(subStr[subCounter] === fullStr[fullCounter]) {
            solutionCounter++;
            subCounter++;
        }
        fullCounter++;
        
        if(subStr.length === solutionCounter) {
            return true;
        }
    }
    return false;
}

/* Multiple Pointers solution */
function isSubsequence(subStr, fullStr) {
    if(!subStr) {
        return true;
    }

    let i = 0;
    let j = 0;

    while(j < fullStr.length) {
        if(fullStr[j] === subStr[i]) {
            i++;
        }
        if(i === subStr.length) {
            return true;
        }
        j++;
    }
    return false;
}

console.log(isSubsequence('hello', 'hello world')); // true
console.log(isSubsequence('sing', 'sting')); // true
console.log(isSubsequence('abc', 'abracadabra')); // true
console.log(isSubsequence('abc', 'acb')); // false (order matters)