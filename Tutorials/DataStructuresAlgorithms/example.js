function maxSubarraySum(arr, num) {
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

// set pointer to the start and next value
// define a max, and sum
// loop and check if values are equal, if they are, increment next
// if they arent, set start to new value and increment counter
