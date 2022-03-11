/** First step to implementing merge sort.
 * This function should be able to merge two sorted arrays whose sizes
 * can vary from each other into a single sorted array.
 * 
 * 1. Create an empty array to hold the merged array.
 * 2. Create two counters for each list (i and j)
 * 3. Iterate through both lists then sort and add the elements to the merge array.
 * 4. When one list has reached the end, since the remainder is already sorted, add it to the end of the merge array.
 * @param {*} arr1 
 * @param {*} arr2 
 */
function myMerge(arr1, arr2) {
    let mergeArr = [];

    let smallest = arr1.length < arr2.length? arr1.length : arr2.length;
    let count = 0;
    while(count < smallest) {
        if(arr1[count] < arr2[count]) {
            mergeArr.push(arr1[count], arr2[count]);
        }
        else {
            mergeArr.push(arr2[count], arr1[count]);
        }
        count++;
    }
    // Add the remainder;
    if(arr1.length < arr2.length) {
        // mergeArr = mergeArr.concat(arr2.slice(count, arr2.length));
        while(count < arr2.length) {
            mergeArr.push(arr2[count]);
            count++;
        }  
    }
    else {
        // mergeArr = mergeArr.concat(arr1.slice(count, arr1.length));
        while(count < arr1.length) {
            mergeArr.push(arr1[count]);
            count++;
        }  
    }
    console.log(mergeArr);
}

function merge(arr1, arr2) {
    let results = [];
    let i = 0;
    let j = 0;

    while(i < arr1.length && j < arr2.length) {
        if(arr2[j] > arr1[i]) {
            results.push(arr1[i]);
            i++;
        }
        else {
            results.push(arr2[j]);
            j++;
        }
    }
    // Add the remainder;
    while(i < arr1.length) {
        results.push(arr1[i]);
        i++;
    }
    while(j < arr2.length) {
        results.push(arr2[j]);
        j++;
    }
    console.log(results);
}

/** Second step to implementing merge sort.
 * Break array into halves until you have arrays that are empty or one element.
 * Merge those smaller arrays until the array is back to a full array.
 * Once it's been merged together, return the merged array.
 * 
 * @param {*} arr 
 */
function myMergeSort(arr) {
    // Couldn't figure this one out..
    let sortedArr = [];

    function helper(arr1, arr2) {
        if(arr1.length <= 1 && arr2.length <= 1) return;

        helper(arr1.slice(0, arr1.length/2), arr1.slice(arr1.length/2, arr1.length));
        helper(arr2.slice(0, arr2.length/2), arr2.slice(arr2.length/2, arr2.length));
        console.log(arr1, arr2);
    }

    helper(arr.slice(0, arr.length/2), arr.slice(arr.length/2, arr.length))
}

/** How this code works:
 * mergeSort(10,24,76,73)@1
 * 'left' is first, it needs to be resolved to a value.
 *   mergeSort([10,24])@2
 *   mergeSort([10])@3 return [10].
 *   Now that we have a value, we pop off back into mergeSort()@2 with @3 resolved.
 *   'right' has to be resolved now
 *   mergeSort([24])@3 return [24]
 *   Now that we have a value, we pop off back into mergeSort()@2 with @3 resolved.
 *   return merge([10], [24])
 *   Merge both the left and right.
 * 
 * Now we pop off of mergeSort()@2 with the 'left' value resolved: [10, 24]
 * 'right' is second, it needs to be resolved to a value.
 *   mergeSort([76,73])@2
 *   mergeSort([76])@3 return [76]
 *   We have a value for 'left' pop off back into mergeSort()@2 with @3 resolved.
 *   mergeSort([73])@3
 *   We have a value for 'right' pop off back into mergeSort()@2 with @3 resolved.
 *   return merge([76], [73])
 *   Merge both left and right
 * 
 * Now that the recursive stack trace has been resolved, we pop off back into mergeSort()@1
 * return merge([10, 24], [73, 76]);
 * Merge and return the sorted array.
 * @param {*} arr 
 * @returns 
 */
function mergeSort(arr) {
    // Base Case
    if(arr.length <= 1) return arr;
    let midpoint = Math.floor(arr.length/2);
    // This will keep reducing the left into one element by adding mergeSort() onto the call stack with reduced left.
    let left = mergeSort(arr.slice(0, midpoint));
    // This has to wait for left to reach one element, then it does the same for the right side.
    let right = mergeSort(arr.slice(midpoint)); // Not specifying an endpoint assumes the end of the array.

    // This return has to wait until the call stacks have been resolved (First call, left and right have 1 element).
    return merge(left, right);
}


// console.time("myMerge");
// myMerge([1,10,50], [2,14,99,100]);
// console.timeEnd("myMerge");

// console.time("merge");
// merge([1,10,50], [2,14,99,100]);
// console.timeEnd("merge");

myMergeSort([10,34,15,5,8,100,27]);
