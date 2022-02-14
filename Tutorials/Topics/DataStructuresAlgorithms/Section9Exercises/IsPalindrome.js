// isPalindrome('awesome') // false
// isPalindrome('foobar') // false
// isPalindrome('tacocat') // true
// isPalindrome('amanaplanacanalpanama') // true
// isPalindrome('amanaplanacanalpandemonium') // false

function isPalindrome(str) {
    // add whatever parameters you deem necessary - good luck!
    if(str.length === 0) {
        return false;
    }

    let start = 0;
    let end = str.length - 1;

    for(let i = 0; i < end; i++) {
        // console.log("comparing '" + str[start] + "' and '" + str[end] + "'");
        if(start >= end) break;
        if(str[start] !== str[end]) return false;
        
        start++;
        end--;
    }
    return true;
}

function isPalindromeR(str) {
    if(str.length === 0 || str.length === 1) return true;

    let start = 0;
    let end = str.length;
    if(str[start] === str[end-1]) {
        // console.log("comparing '" + str[start] + "' and '" + str[end-1] + "'");
        return isPalindromeR(str.substring(start+1, end-1));
    }
    else {
        return false;
    }
}

console.log(isPalindromeR('awesome')); // false
console.log(isPalindromeR('foobar')); // false
console.log(isPalindromeR('tacocat')); // true
console.log(isPalindromeR('amanaplanacanalpanama')); // true
console.log(isPalindromeR('amanaplanacanalpandemonium')); // false