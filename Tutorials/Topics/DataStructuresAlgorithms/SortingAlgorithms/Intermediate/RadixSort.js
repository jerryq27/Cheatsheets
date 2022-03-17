/**
 * This function grabs the digit specified.
 * @param {*} num 
 * @param {*} place 
 * @returns the specified digit.
 */
function getDigit(num, place) {
    // return Math.floor(num / Math.pow(10, place)) % 10;

    // Works with negative numbers using Math.abs().
    return Math.floor(Math.abs(num) / Math.pow(10, place)) % 10;
}

/**
 * Returns the number of digits in a number.
 * @param {*} num 
 */
function digitCount(num) {
    if(num === 0) return 1;

    // Log10 = 10 to what power gives us "num"?
    return Math.floor(Math.log10(Math.abs(num))) + 1;
}

/**
 * Finds the number with the most digits and returns that count.
 * @param {*} nums 
 * @returns the number of digits in the largest number literal.
 */
function mostDigits(nums) {
    let largest = 0;
    for(let i = 0; i < nums.length; i++) {
        let dCount = digitCount(nums[i]);
        largest = largest < dCount? dCount : largest;
    }
    return largest;
}

function myRadixSort(arr) {
    let iterations = mostDigits(arr);
    
    for(let k = 0; k < iterations; k++) {
        // Place numbers into groups.
        let group = Array(10).fill(null);

        for(let i = 0; i < arr.length; i++) {
            let digit = getDigit(arr[i], k); // 1004
            if(!group[digit]) {
                group[digit] = Array();
            }
            group[digit].push(arr[i]);
        }
        // Reset array.
        arr = [];
        for(let i = 0; i < group.length; i++) {
            if(group[i]) {
                arr = arr.concat(group[i])
            }
        }
    }
    console.log(arr);
}

function radixSort(arr) {
    let maxDigitCount = mostDigits(arr);

    for(let k = 0; k < maxDigitCount; k++) {
        let digitBuckets = Array.from({ length: 10 }, () => []);
        for(let i = 0; i < arr.length; i++) {
            let digit = getDigit(arr[i], k);
            digitBuckets[digit].push(arr[i]);
        }
        arr = [].concat(...digitBuckets);
    }
    console.log(arr);
}

console.time("first");
console.timeEnd("first");

console.time("radixSort");
radixSort([23,345,5467,12,2345,9852]);
console.timeEnd("radixSort");

console.time("myRadixSort");
myRadixSort([23,345,5467,12,2345,9852]);
console.timeEnd("myRadixSort");

