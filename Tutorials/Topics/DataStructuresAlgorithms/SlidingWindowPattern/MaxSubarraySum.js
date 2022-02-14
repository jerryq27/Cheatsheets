
/** 
 * Write a function called **maxSubarraySum** which accepts an
 * array of integers and a number called n. The function should
 * calculate the maximum sum of n consecutive elements in the array.
 * 
 * Pattern: Sliding Window Pattern
 */

// set pointer to the start and next value
// define a max, and sum
// loop and check if values are equal, if they are, increment next
// if they arent, set start to new value and increment counter
function maxSubarraySum2(arr, num) {
    if(num > arr.length) {
        return null;
    }

    // if there is an array of negative numbers, starting at 0 wouldn't make sense.
    let max = -Infinity;
    // Only going to a certain part of the loop. Once we reach the point
    // Where we can't add "num" digits, we stop.
    for(let i = 0; i < arr.length - num + 1; i++) {
        let temp = 0;
        for(let j = 0; j < num; j++) {
            // j is only going up to num
            // so adding j to i loops through "num" digits.
            temp += arr[i + j];
        }
        if(temp > max) {
            max = temp;
        }
    }
    return max;
}

/* My solution */
function maxSubarraySum(arr, num) {
    if(arr.length < num) {
        return null;
    }

    let max = -Infinity;
    for(let i = 0; i < arr.length - num + 1; i++) {

        let sum = 0;
        for(let j = 0; j < num; j++) {
            sum += arr[i + j];
        }

        max = sum > max? sum : max;
    }
    return max;
}
    

console.log(maxSubarraySum([100, 200, 300, 400], 2)); // 700
console.log(maxSubarraySum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)); // 39
console.log(maxSubarraySum([-3, 4, 0, -2, 6, -1], 2)); // 5
console.log(maxSubarraySum([3, -2, 7, -4, 1, -1, 4, -2, 1], 2)); // 5
console.log(maxSubarraySum([2, 3], 3)); // null