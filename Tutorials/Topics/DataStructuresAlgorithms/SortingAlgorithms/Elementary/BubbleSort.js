function bubbleSort(arr) {
    let sorted; // Optimization.
    for(let i = arr.length; i > 0; i--) {
        sorted = true;
        for(let j = 0; j < i - 1; j++) {
            if(arr[j] > arr[j+1]) {
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                sorted = false;
            }
        }
        if(sorted) break;
    }
    console.log(arr);
}

bubbleSort([5, 4, 6, 1, 2]);