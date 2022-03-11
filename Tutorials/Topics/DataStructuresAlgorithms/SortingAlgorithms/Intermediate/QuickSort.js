/** First step to implementing Quick Sort.
 * 
 * 1. Choose a pivot within the given array.
 * 2. The values of the array should be rearranged so that values less than the pivot are on the left and values greater are on the right.
 * 3. Order doesn't matter, and the array can be returned as such.
 * @param {*} arr 
 */
function myPivot(arr) {
    let pivot = arr[0];

    let pivotIndex = 0;
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] < pivot) {
            pivotIndex++;
            // Swap
            let temp = arr[pivotIndex];
            arr[pivotIndex] = arr[i];
            arr[i] = temp;
        }
    }
    // Final Swap
    let temp = arr[pivotIndex];
    arr[pivotIndex] = arr[0];
    arr[0] = temp;

    // console.log(arr);
    return pivotIndex;
}

function pivot(arr, start=0, end=arr.length + 1) {
    let pivot = arr[start];
    let swapIndex = start;

    for(let i = start + 1; i < arr.length; i++) {
        if(pivot > arr[i]) {
            swapIndex++;
            // Swap
            let temp = arr[swapIndex];
            arr[swapIndex] = arr[i];
            arr[i] = temp;
        }
    }
    let temp = arr[swapIndex];
    arr[swapIndex] = arr[start];
    arr[start] = temp;
    // console.log(arr);
    return swapIndex;
}

function quickSort(arr, left=0, right=arr.length - 1) {
    // Base case for recursion.
    if(left < right) {
        let pivotIndex = pivot(arr, left, right);
    
        // Left side
        quickSort(arr, left, pivotIndex - 1)
        // Right side
        quickSort(arr, pivotIndex + 1, right);
    }
    return arr;
}

console.time("first");
console.timeEnd("first");

// console.time("pivot");
// pivot([4,8,2,1,5,7,6,3]);
// console.timeEnd("pivot");

// console.time("myPivot");
// myPivot([4,8,2,1,5,7,6,3]);
// console.timeEnd("myPivot");

console.time("quickSort");
console.log(quickSort([100,-2,5,7,28,54,3,84,9]));
console.timeEnd("quickSort");
