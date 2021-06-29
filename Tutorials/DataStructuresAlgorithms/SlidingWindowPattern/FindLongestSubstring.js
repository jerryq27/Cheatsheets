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
    let substr = '';
    let teststr = '';

    while(start < str.length) {

        for(let i = start; i < str.length; i++) {
            if(teststr.includes(str[i])) {
                // if(substr === teststr) {
                //     console.log(`str: ${str} substr: ${substr}`)
                //     return substr.length;
                // }
                
                start += 1; //= i;
                substr = teststr.length > substr.length? teststr : substr;
                teststr = '';

                if(i === str.length - 1) {
                    start = -1;
                }
                break;
            }
            else {
                teststr += str[i];
            }
            //console.log(teststr);
        }
        if(start === -1) {
            console.log(`str: ${str} substr: ${substr}`)
            return substr.length;
        }


        // Grab letter in start position
        // is next letter the same
        // add next letter to substring
        // check next letter, does letter not exist in substring?
        // if so, add letter
        // if not, update substr by comparing lengths and increase start




        // console.log(`${start}, ${end}: ${substr}`);
        // if(substr.includes(str[start])) {
        //     start++;
        // }
        // else if(substr.includes(str[end])) {
        //     end--;
        // }
        // else {
        //     break;
        // }

        // substr = str.slice(start, end);
    }
}

function findLongestSubstring2(str) {
    let longest = 0;
    let seen = {};
    let start = 0;
   
    for (let i = 0; i < str.length; i++) {
      let char = str[i];
      if (seen[char]) {
        start = Math.max(start, seen[char]);
      }
      // index - beginning of substring + 1 (to include current in count)
      longest = Math.max(longest, i - start + 1);
      // store the index of the next char so as to not double count
      seen[char] = i + 1;
    }
    return longest;
  }


// console.log(findLongestSubstring('')); // 0
// console.log(findLongestSubstring('rithmschool')); // 7
// console.log(findLongestSubstring('thisisawesome')); // 6
// console.log(findLongestSubstring('thecatinthehat')); // 7
// console.log(findLongestSubstring('bbbbbb')); // 1
// console.log(findLongestSubstring('longestsubstring')); // 8
console.time('findLongestSubstring');
console.log(findLongestSubstring('thisishowwedoit')); // 6
console.timeEnd('findLongestSubstring');

console.time('findLongestSubstring2');
console.log(findLongestSubstring2('thisishowwedoit')); // 6
console.timeEnd('findLongestSubstring2');