/**
 * Write a function which accepts two parameters: an array of positive integers
 * and a positive integer. The function should return the minimal length of a
 * contiguous subarray of which the sum is greater than or equal to the integer
 * passed to the function. If there isn't one, return 0 instead.
 * 
 * Pattern: Sliding Window Pattern
 */

/* My solution */
function minSubArrayLen(arr, num) {
    let window = 2;
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] >= num) {
            return 1;
        }

        let sum = 0;
        for(let j = 0; j < window; j++) {
            sum += arr[i + j];
            if(sum >= num) {
                return window;
            }

            if(window === j + 1) {
                window++;
                j = 0

                if(window === arr.length - 1) {
                    window = 2;
                    break;
                }
            }
        }
    }
    return 0;
}

function minSubArraySum(nums, sum) {
    let total = 0;
    let start = 0;
    let end = 0;
    let minLen = Infinity;

    while(start < nums.length) {
        // If current window doesn't add up to the given sum, move window to the right.
        if(total < sum && end < nums.length) {
            total += nums[end];
            end++;
        }
        // If current window adds up to at least the sum given, then we can shrink the window.
        else if(total >= sum) {
            minLen = Math.min(minLen, end - start);
            total -= nums[start];
            start++;
        }
        else {
            break;
        }
    }
    return minLen === Infinity? 0 : minLen;
}

console.log(minSubArrayLen([2, 3, 1, 2, 4, 3], 7)); // 2, [4,3] is the smallest sub array.
console.log(minSubArrayLen([2, 1, 6, 5, 4], 9)); // 2, [5,4] os the smallest subarray.
console.log(minSubArrayLen([3, 1, 7, 11, 2, 9, 8, 21, 62, 33, 19], 52)); // 1, 62 is greater than 52   
console.log(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 39)); // 3
console.log(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 55)); // 5
console.log(minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11)); // 2
console.log(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 95)); // 0