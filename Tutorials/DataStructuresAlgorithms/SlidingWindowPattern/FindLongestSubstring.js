/**
 * Write a function which accepts a string and returns the length of the longest
 * substring with all distinct characters.
 * 
 * Pattern: Sliding Window Pattern
 */ 

function findLongestSubstring(str) {
    if(str.length === 0) {
        return 0;
    }

    let start = 0;
    let end = 0;

    let substr = '';

    while(start < str.length) {
        if(end < str.length) {
            substr += str[end];
            end++;
        }

        if(str[start] === str[end]) {
            start++;
            substr = substr.slice(1, substr.length);
        }
    }
    return substr.length;
}

console.log(findLongestSubstring('')); // 0
console.log(findLongestSubstring('rithmschool')); // 7
console.log(findLongestSubstring('thisisawesome')); // 6
console.log(findLongestSubstring('thecatinthehat')); // 7
console.log(findLongestSubstring('bbbbbb')); // 1
console.log(findLongestSubstring('longestsubstring')); // 8
console.log(findLongestSubstring('thisishowwedoit')); // 6