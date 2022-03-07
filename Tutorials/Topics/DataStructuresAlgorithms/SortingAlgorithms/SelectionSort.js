/**
 * Steps:
 * 1. Mark first value as the minimum and save the index
 * 2. Compare it to next value, is a new one the minimum? Replace saved index, otherwise move to the next value.
 * 3. Keep repeating step 2 until the entire array has been traversed.
 * 4. Swap the min value at the saved index with the first element in the array.
 * 5. The first value can now be ignored since it's sorted. Mark the next value as the minimum and save the index
 * 6. Repeat steps 2-4 until the entire array has been traversed and the array is sorted!
 * @param {*} arr 
 */
function mySelectionSort(arr) {
    let minIndex = 0;
    let doSwap = false;

    for(let i = 0; i < arr.length; i++) {
        for(let j = (i + 1); j < arr.length; j++) {
            // console.log(`Comparing ${arr[minIndex]} with ${arr[j]}`)
            if(arr[j] < arr[minIndex]) {
                minIndex = j;
                doSwap = true;
            }
        }
        if(doSwap) {
            // console.log(`Swapping "${arr[i]}" with "${arr[minIndex]}"`);
            let valToSwap = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = valToSwap;
            doSwap = false;
        }
    }
    return arr;
}

function selectionSort(arr) {
    for(let i = 0; i < arr.length; i++) {
        let lowest = i;
        for(let j = (i+1); j < arr.length; j++) {
            if(arr[j] < arr[lowest]) {
                lowest = j;
            }
        }
        if(i !== lowest) {
            let temp = arr[i];
            arr[i] = arr[lowest];
            arr[lowest] = temp;
        }
    }
    return arr;
}

let testarr = [34,22,10,19,17];

console.log(mySelectionSort(testarr));
console.log(selectionSort(testarr));