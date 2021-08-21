function isPalindrome(str) {
    if(!str) return;

    console.log(str);
    if(str[0] !== str[str.length - 1]) {
        return false;
    }
    else if(str.length === 2 && str[0] === str[str.length - 1]) {
        return true;
    }
    else if(str.length === 1) {
        return true;
    }
    else {
        isPalindrome(str.slice(1, str.length - 1));
    }
}

// console.log(isPalindrome('awesome')); // false
// console.log(isPalindrome('foobar')); // false
console.log(isPalindrome('tacocat')); // true
// console.log(isPalindrome('amanaplanacanalpanama')); // true
// console.log(isPalindrome('amanaplanacanalpandemonium')); // false