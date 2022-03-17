/**
 * Steps:
 * 1. Grab the second elemnt in the list (first is already in the sorted list)
 * 2. Compare and swap if necessary
 * 3. Grab the next element and compare it through the sorted portion (left side)
 * 4. Place in the correct spot and reapeat until all items have been sorted.
 * @param {*} arr 
 */
function myInsertionSort(arr) {
    for(let i = 1; i < arr.length; i++) {
        let leftIndex = i - 1;
        let currIndex = i;

        while(leftIndex >= 0) {
            // console.log(`Comparing ${arr[currIndex]} and ${arr[leftIndex]}`);
            if(arr[currIndex] < arr[leftIndex]) {
                // Swap
                // console.log(`Swapping ${arr[currIndex]} and ${arr[leftIndex]}`);
                // console.log(arr);
                let temp = arr[leftIndex];
                arr[leftIndex] = arr[currIndex];
                arr[currIndex] = temp;

                // Update index due to position swap.
                currIndex = leftIndex;
                leftIndex--;
                // console.log(arr, "\n\n");
            }
            else {
                break;
            }
        }
    }
    console.log(arr);
}

function insertionSort(arr) {
    for(let i = 1; i < arr.length; i++) {
        let currentVal = arr[i];
        let j;
        for(j = (i - 1); (j >= 0 && arr[j] > currentVal); j--) {
            arr[j + 1] = arr[j];
            console.log(arr);
        }
        arr[j + 1] = currentVal;
    }

    console.log(arr);
}
console.time("myInsertionSort");
myInsertionSort([2, 1, 9, 76, 4]);
myInsertionSort([22, 11, 3, 5, 27, 12]);
console.timeEnd("myInsertionSort");

console.time("insertionSort");
insertionSort([2, 1, 9, 76, 4]);
insertionSort([22, 11, 3, 5, 27, 12]);
console.timeEnd("insertionSort");