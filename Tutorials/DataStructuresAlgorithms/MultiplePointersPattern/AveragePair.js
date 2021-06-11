/**
 * Given a sorted array of integers and a target average, determine
 * if there is a pair of values in the array where the average of the pair
 * equals the target average. There may be more than one pair that matches
 * the average target.
 * 
 * Pattern: Multiple Pointers Pattern
 */

/* My solution */
function averagePair(nums, target) {
    if(nums.length === 0 || (nums.length === 1 && nums[0] !== target)) {
        return false;
    }
    
    let start = 0;
    let next = 1;

    while(start < nums.length) {
        if(start === next || (nums[start] + nums[next]) < target) {
            next++;
            if(next === nums.length) {
                start++;
                next = 0;
            }
            continue;
        }
        else if((nums[start] + nums[next])/2 === target) {
            return true;
        }
        else {
            next++;
        }

        if(next === nums.length) {
            start++;
            next = 0;
        }
    }
    return false;
}

/* Multiple Pointers solution */
function averagePair(nums, target) {
    let start = 0;
    let end = nums.length - 1;

    while(start < end) {
        let average = (nums[start] + nums[end])/2
        if(average === target) {
            return true;
        }
        else if(average < target) {
            start++;
        }
        else {
            end--;
        }
    }
    return false;
}

console.log(averagePair([1, 2, 3], 2.5)); // true
console.log(averagePair([1, 3, 3, 5, 6, 7, 10, 12, 19], 8)); // true
console.log(averagePair([-1, 0, 3, 4, 5, 6], 4.1)); // false
console.log(averagePair([], 4)); // false