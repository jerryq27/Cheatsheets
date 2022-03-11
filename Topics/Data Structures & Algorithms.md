# Data Structures & Algorithms

Data Structures and algorithms in programming are essential for efficient
problem solving.

## Basics

### Big O Notation

Big O Notation is a system used to denote the efficiency of an algorithm based
on the growth of inputs. This system allows for the discussion of code
performance and trade-offs between various solutions to a problem.

Notations from best to worst performance:

**O(1)** (Constant)

```code
loop(n) {
    print(Min(n, 5))
}
```

**O(log n)** (Logarithmic)

**O(n)** (Linear)

```code
loop(n) {
    print(n)
}
```

**O(n log n)** ()

**O(n^2)** (Quadratic)

**O(2^n)** ()

**O(n!)** ()

#### Time Complexity

Time complexity is measuring algorithms based on their runtime.

Algorithm runtimes can be measured in a few ways, most importantly:

1. Time in seconds
    * Pros
        1. Easy comparison between two algorithms by showing how much time each
        took to complete
    * Cons
        1. Different machines will display different times
        1. The same machine will display different times
        1. Speed measurements lose precision for really fast algorithms

1. Number of Operations
    * Pros
        1. More consistent since we are counting the number of computer
        operations which is more constant between machines than time.

A few things to keep in mind in determining which notation to use:

* Some operations are constant
  * Arithmetic operations
  * Variable assignment
  * Accesing array elements by index or value by key
* Loop operations are measured by the length of the loop times the number of
operations within the loop

#### Space Complexity

Space complexity is measuring algorithms based on how much memory requirments.

Space can be measured by the memory required by both the inputs and operations,
or by just the operations. Measuring by operations only is known as
_auxiliary space complexity_.

A few things to keep in mind in determining which notation to use:

* Some space allocation is constant
  * Most primitive data types
* String space is measured by the length of the string
* Collections are also measured by the length of the collection

#### Constant

Notation: O(1)

#### Logarithmic

Notation O(log n)

To understand Logarithmic notation, we must definte logarithms. Logarithms are
basically the inverse of exponents:

log2(VALUE) = EXPONENT : 2^EXPONENT = VALUE

In other words log2(NUMBER) is the number of times NUMBER van be divided by 2
before it is less than or equal to one.

In Logarithmic notation, log2 is commonly used, so the 2 is ommitted.

#### Linear

Notation: O(n)

#### Quadratic

Notation: O(n^2)

### Problem Solving

To solve whiteboard interview problems or problems on sites like LeetCode,
it's helpful to remember these steps:

1. Understand the problem
1. Explore concrete examples
1. Break it down
1. Solve (Simplify?)
1. Look back and refactor

#### Understanding The Problem

Helpful questions to see if you understand the problem:

1. Can you restate the problem in your own words?
1. What are the inputs that go into the problem?
1. What are the outputs that should come from the solution to the problem?
1. Can the outputs be determined from the inputs? In other words, do I have
enough information to solve the problem?
1. How should you label the important pieces of data that are a part of the
problem? What matters?

Example Problem: Write a function that returns the sum of 2 numbers.

1. "Add two numbers and return the solution"
1. Are these whole numbers? Floating points? Large numbers?
1. Same as 2
1. What to do in the case of 1 input? More than two inputs? What if the data is
invalid?
1. The numbers parameters and the solution from the addition.

#### Explore Concrete Examples

Coming up with examples can help you understand the problem better. Examples also
provide sanity checks to verify that your solution works the way it should:

1. Start with simple examples
1. Progress to more complex examples
1. Explore examples with empty inputs
1. Explore examples with invalid inputs

Example Problem: Write a function that takes a string and returns the count of
each character in the string:

```code
1. charCount("aaaa") // Output: {a: 4}
   charCount("hello") // Output: {h: 1, e: 1, l: 2, o: 1}

2. charCount("my phone number is 12341234")
   charCount("Harry, hello!")
    // Are we including spaces? Numbers? Special characters?
    // Is the count case sensitive?
3. charCount()
   charCount("")
   // What should we return?
4. charCount(1)
   charCount(true)
   // How to we handle these inputs?
```

#### Break It Down

Break down the problem and write those steps you need to take to solve it.
This forces you to think about the code you're going to write before writing it
and will help you catch conceptual issues or misunderstandings before diving in.

> In interviews, be vocal about how you are breaking things down and what steps
you are formulating.

Example Problem: Write a function that takes a string and returns the count of
each character in the string:

```code
// Interviewer stated only alphanumeric characters and capitals are treated as
// lowercase

function charCount(str) {
    // Create empty key-value collection
    // Loop over the lowercased string for each character
        // if character is an existing key in collection, increment count
        // if not, add the chracter to the collection as a key and set value to 1
        // if character is something else (space, special) don't do anything
    
    // Return an key-value collection list of each character with their counts.
}
```

#### Solve (Simplify?)

Now, attempt to solve the problem, if you can't, solve a simpler problem.

If you need to simplify, find the core difficulty of what you're trying to do,
temporarily ignore it and then write a simplified solution then incorporate
that difficulty back in.

Example Problem: Write a function that takes a string and returns the count of
each character in the string:

```code
// Possible difficult parts for the implementation:
// 1. Implementing the loop (Start with creating the key-value collection!)
// 2. Creating the collection (Start with looping over the string and printing 
// each character!)

function charCount(str) {

}
```

#### Look Back & Refactor

This is the step that makes you improve as a programmer. Most finish when
something just works, but looking back to try an improve the code
(efficiency, readability, etc.):

1. Can you check the result?
1. Can you get to the result differently?
1. Can you understand it at a glance?
1. Can you use the result or method for some other problem?
1. Can you improve the performance of your solution?
1. Can you think of other ways to refactor?
1. How have others solved this problem?

### Common Patterns

When solving problems you will come across certain patterns. Learning to
recognize these patterns will help you come up a solution to the problem.

#### Frequency Counter Pattern

This pattern deals with collecting data and frequencies of things occuring.
Usually this pattern is O(n) vs the easier solution which is O(n^2). When dealing
with multiple pieces of data and needing to compare them, it's usually this
pattern.

Example Problem: Write a function called **same**, which accepts two arrays.
This function should return true if every value in the array has a corresponding
value squared in the second array. The frequency of values must be the same.

**Concrete Examples:**

```code
same([1,2,3], [4,1,9]) // true
same([1,2,3], [1,9]) // false
same([1,2,3], [4,4,1]) // false
```

Naive solution (Uses nested loops):

```js
// O(n^2)
function same(arr1, arr2) {
    if(arr1.length !== arr2.length) {
        return false;
    }
    for(let i = 0; i < arr1.length; i++) {
        // indexOf() is a for loop, so O(n^2)
        // Other Naive solutions might define another for loop here.
        let correctIndex = arr2.indexOf(arr1[i] ** 2);
        if(correctIndex === -1) {
            return false;
        }
        // Splice adds/remove items from an array.
        arr2.splice(correctIndex, 1);
    }
    return true;
}
```

Input size(1000): 1000x1000=1,000,000 iterations.

Refactored solution (No nested loops):

```js
// O(n)

function same(arr1, arr2) {
    if(arr1.length !== arr2.length) {
        return false;
    }

    let freqCounter1 = {};
    let freqCounter2 = {};
    for(let val of arr1) {
        // Sets a key equal to itself + 1 if it exists or creates a new key
        // and sets the value to 0 + 1 if it doesn't.
        freqCounter1[val] = (freqCounter1[val] || 0) + 1;
    }
    for(let val of arr2) {
        freqCounter[val] = (freqCounter[val] || 0) + 1;
    }

    for(let key in freqCounter1) {
        // Is the square of the key absent from the second array?
        if(!(key ** 2) in freqCounter2) {
            return false;
        }
        // Are the squared frequency and non squared frequency different?
        if(freqCounter2[key ** 2] !== freqCounter1[key]) {
            return false;
        }
    }
    return true;
}
```

Input size(1000): 1000x3=3000 iterations.

Example Problem 2: Given two strings, write a function to determine if the second
string is an anagram of the first.

Anagram: a word, phrase, or name formed by rearranging the letters of another.
_cinema_ is an anagram of _iceman_.

**Concrete Examples:**

```code
validAnagram('','') // true
validAnagram('aaz','zza') // false
validAnagram('anagram','nagaram') // true
validAnagram('rat','car') // false
validAnagram('texttwisttime','timetwisttext') // true
```

Solution 1:

```js
function validAnagram(str1, str2) {
    if(str1.length !== str2.length) {
        return false;
    }

    let charCounter1 = {};
    let charCounter2 = {};

    for(let char of str1) {
        charCounter1[char] = (charCounter1[char] || 0) + 1;
    }
    for(let char of str2) {
        charCounter2[char] = (charCounter2[char] || 0) + 1;
    }

    for(let key in charCounter1) {
        if(!(key in charCounter2)) {
            return false;
        }
    }
    for(let key in charCounter1) {
        if(charCounter1[key] !== charCounter2[key]) {
            return false;
        }
    }
    return true;
}
```

Solution 2:

```js
function validAnagram(str1, str2) {
    if(str1.length !== str2.length) {
        return false;
    }

    let charCounter1 = {};
    let charCounter2 = {};

    for(let i = 0; i < str1.length; i++) {
        let char = str1[i];
        charCounter1[char]? charCounter1[char] += 1 : charCounter1[char] = 1;
    }
    for(let i = 0; I < str2.length; i++) {
        let char = str2[char];
        // If letter can't be found or is 0, not an anagram.
        if(!str1[char]) {
            return false;
        }
        else {
            str1[char] -= 1;
        }
    }
    return true;
}
```

> Note: Avoid nested loops whenever possible! Having multiple loops is still
O(n), but one nested loop turns the solution to O(n^2).

#### Multiple Pointers Pattern

This pattern involves creating pointers or values that correspond to an index
position and moves towards the beggining, middle, or end based on a certain
condition. Efficient for solving problems with minial space complexity as well.

Example Problem: Write a function called **sumZero** which accepts a _sorted_
array of integers. The function should find the first pair where the sum is 0.
Return an array that include both the value that sum to zero or undefined if a
pair does not exist.

**Concrete Examples:**

```code
sumZero([-3,-2,-1,0,1,2,3]) // [-3,3]
sumZero([-2,0,1,3]) // undefined
sumZero([1,2,3]) // undefined
```

Naive Solution (Nested loops):

```js
function sumZero(arr) {
    for(let i = 0; i < arr.length; i++) {
        for(let j = 0; i < arr.length; j++) {
            if(arr[i] + arr[j] === 0) {
                return [ arr[i], arr[j] ];
            }
        }
    }
}
```

Refactored Solution (Using Pointers):

```js
let left = 0;
let right = arr.length -1;
while(left < right) {
    let sum = arr[left] + arr[right];
    if(sum === 0) {
        return [ arr[left], arr[right] ];
    }
    // Since the list is sorted, we can assume if the sum is greater than 0
    // the right number is too big, so move down one.
    else if(sum > 0) {
        right--;
    }
    // The left number is too low, so move up one.
    else {
        left++;
    }
}
```

Example Problem 2: Implement a function called **countUniqueValues** which
accepts a sorted array, and count the unique value in the array. There can be
negative numbers in the array, but it will always be sorted.

**Concrete Examples:**

```code
countUniqueValues([1,1,1,1,1,2]) // 2
countUniqueValues([1,2,3,4,4,4,7,7,12,12,13]) // 7
countUniqueValues([]) // 0
countUniqueValues([-2,-1,-1,0,1]) // 4
```

Solution 1 (My solution! :D):

```js
function countUniqueValues(arr) {
    if(arr.length === 0) {
        return 0;
    }
    
    let count = 0;
    let start = 0;

    for(let i = 0; i < arr.length; i++) {
        if(arr[start] === arr[start + 1]) {
            start += 1;
        }
        else if(arr[start] !== arr[start + 1]) {
            start += 1;
            count += 1;
        }
    }
    return count;
}
```

Solution 2:

```js
function countUniqueValues(arr) {
    let i = 0;
    for(let j = 1; j < arr.length; j++) {
        if(arr[i] !== arr[j]) {
            i++;
            // Altering the array this way insures that whereever i ends up
            // Will be the index of the last unique value.
            // Useful if we need the unique values since we can slice the array
            // up to i.
            arr[i] = arr[j];
        }
    }
    return i + 1;
}
```

#### Sliding Window Pattern

This pattern involves creating a _window_ (subset) which can be a sub array or
a single value. Depending on a certain condition, the window either increases or
closes (and a new window is created). Useful for keeping track of a subset of
data in an array/string, etc.

Example Problem: Write a function called **maxSubarraySum** which accepts an
array of integers and a number called n. The function should calculate the
maximum sum of n consecutive elements in the array.

Naive Solution (Nested loops):

```js
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
```

Refactored Solution:

```js
function maxSubarraySum(arr, num) {
    let maxSum = 0;
    let tempSum = 0;
    if(arr.length < num) {
        return null;
    }

    for(let i = 0; i < num; i++) {
        maxSum += arr[i];
    }
    tempSum = maxSum;
    for(let i = num; i < arr.length; i++) {
        // The sliding window! We don't need to re-add the next 'n" numbers.
        // We just subtract the first one, and add the next number
        // Hench, a sliding window.
        tempSum = tempSum - arr[i - num] + arr[i];
        maxSum = Mat.max(maxSum, tempSum);
    }
    return maxSum;
}
```

#### Divide & Conquer Pattern

This pattern involves dividing a data set into smaller chunks and then repeating
a process with a subset of data. This pattern can greatly decrease time
complexity.

Examples: Quick Sort, Merge Sort, etc.

Example Problem: Given a _sorted_ array of integers, write a function called
**search**, that accepts a value and returns the index where the value passed
to the function is located. If the value is not found, return -1.

**Concrete Examples:**

```code
search([1,2,3,4,5,6], 4) // 3
search([1,2,3,4,5,6], 6) // 5
search([1,2,3,4,5,6], 11) // -1
```

Naive Solution (Linear search):

```js
// O(n)
function search(arr, val) {
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] === val) {
            return i;
        }
    }
    return -1;
}
```

Refactored Solution (Divide and Conquer algorithm)

Since it is sorted: [Binary Search]

## Recursion

Recursion is a process (function) that calls itself.

Behind the scenes, functions have to be called in a certain order, when the code
is processed it uses a **Call Stack** data sctructure to track the order of
function calls. When a function is called it's placed (pushed) on top of the call
stack, and when the function ends or the **return** keyword is encountered, the
function is removed (popped) from the call stack.

Recursive functions have two essential parts:

1. The base case, in other words, the condition when the recursion ends
1. Different (reduced) input

Mistakes when creating recursive functions:

1. No base case (or it's wrong)
1. The input isn't being reduced (or changed)

These will usually result in a _stack overflow_!

Simple Recursive function:

```js
function countDown(num) {
    if(num <= 0) {
        console.log('Done.')
        return;
    }
    console.log(num);
    num--;
    countDown(num);
}
```

Recursive function 2:

```js
/**
 * num = 3
 * return 3 + sumRange(2) // waiting on sumRange...
 *      return 2 + sumRange(1) // Waiting on sumRange...
 *          return 1 // Done!, sumRange(1) = 1, sumRange(2) = 3, answer = 3 + 3!
 */
function sumRange(num) {
    if(num === 1) return 1;

    return num + sumRange(num - 1);
}
```

Factorial:

```js
// Iteratively
function iterativeFactorial(num) {
    let total = 1;
    for(let i = num; i > 1; i--) {
        total *= i;
    }
    return total;
}

// Recursively
function recursiveFactorial(num) {
    if(num === 1) {
        return num;
    }
    return num * recursiveFactorial(num - 1); 
}
```

### Helper Method Recursion

Helper Method Recursion functions are recursive functions defined and called within
another non-recursive function:

```code
outerFunc() {
    recursiveFunc(input) {
        recursiveFunc(input-1)
    }

    recursiveFunc(input)
}
```

Example:

```js
// Helper Method Recursion
function collectOdds(nums) {
    let result = [];

    function helper(input) {
        if(input.length === 0) {
            return;
        }

        if(input[0] % 2 !== 0) {
            result.push(input[0]);
        }

        helper(input.slice(1));
    }
    helper(nums);

    return result;
}

/** Pure Recursion
 * collectOdds([1, 2, 3])
 *      [1].concat(collectOdds([2, 3]))
 *          [].concat(collectOdds([3]))
 *              [3].concat(collectOdds([]))
 *                  Done! answer: [1, 3]
 * result array gets reassigned every time, it allows us to concatenate into
 * nothing or an odd number.
 */ 
function collectOdds(nums) {
    let result = [];

    if(nums.length === 0) {
        return result;
    }

    if(nums[0] % 2 !== 0) {
        result.push(nums[0]);
    }

    result = result.concat(collectOdds(nums.slice(1)));
    return result;
}
```

> Note: If using arrays or strings in a pure recursive function, using methods
like slice(), concat(), substr(), or the (...) spreader operator lets you create
copies of the immutable type so you don't need to mutate it. To copy objects, use
Object.assign() or (...).

## Searching Algorithms

### Linear Search

The simplest searching algorithm. It looks at every element in the
array and checks if it's the value being searched for.

JavaScript uses linear search with the following functions:

* `indexOf()`
* `includes()`
* `find()`
* `findIndex()`

Steps:

1. Loop through the array.
1. Check each value if it's the one we're searching for.
1. Return the value/index/boolean to represent if it's found or not found.

```js
function linearSearch(arr, val) {
    for(let i  = 0; i < arr.length; i++) {
        if(arr[i] === val) return i;
    }
    return -1;
}
```

Time Complexity: Best Case - O(1), Worst Case - O(n)

### Binary Search

Binary search is much faster than Linear Search, best case scenario, it eliminates
half of the remaining elements rather than one at a time. However, Binary Search
only works on _sorted_ arrays!

Steps:

1. Note the start, end, and middle point of the array.
1. Check if the value is greater than or less than the mid's index value.
1. Update start or end point based on the previous condition.
1. Recalculate the mid point based on the new start or end point.
1. Repeat steps 2-4 until a value is found or if start is greater than the end.

```js
function binarySearch(arr, val) {
    // let leftPtr = 0;
    // let rightPtr = arr.length - 1;
    // let midPtr = arr.length/2;

    // while(true) {
    //     if(arr[midPtr] === val) return midPtr;
    //     else if(arr[midPtr] < val) {
    //         leftPtr = midPtr;
    //         midPtr = (leftPtr + rightPtr)/2;
    //     }
    //     else if(arr[midPtr] > val) {
    //         rightPtr = midPtr;
    //         midPtr = (leftPtr + rightPtr)/2;
    //     }
    //     else if(rightPtr === midPtr || leftPtr === midPtr) return -1;
    // }

    /* Solution */
    
    let start = 0;
    let end = arr.length - 1;
    let mid = Math.floor((start + end)/2);

    while(arr[mid] !== val) {
        if(val < arr[mid]) {
            end = mid - 1; // We already checked mid, so adjust by 1
        }
        else start = mid + 1;
        
        mid = Math.floor((start + end)/2);
        if(start > end) return -1;
    }
    return mid;
}
```

Time Complexity: Best Case - O(1), Worst Case - O(log n)

### Naive String Search

Used for finding substrings within strings.

```js
// function naiveStringSearch(str, substr) {
//     let counter = 0;
    
//     for(let i = 0; i < str.length; i++) {
//         if(str[i] === substr[0]) {
//             let j = 0;
//             while(j < substr.length) {
//                 if(str[i + j] === substr[j]) {
//                     j++;
//                     if(j === substr.length - 1) counter++;
//                 }
//                 else {
//                     break;
//                 }
//             }
//             counter++;
//         }
//     }
//     return counter;
// }

/* Solution */

function naiveStringSearch(long, short) {
    let count = 0;

    for(let i = 0; i < long.length; i++) {
        for(let j = 0; j < short.length; j++) {
            if(short[j] !== long[i + j]) break;
            if(j === short.length - 1) count++;
        }
    }

    return count;
}
naiveStringSearch("lorie loled", "lol")
```

### KMP String Search

## Sorting Algorithms

### Elementary Sorting Algorithms

Also known as _quadratic sorting algorithms_ since their time complexity is
quadratic, or O(n^2).

#### Bubble Sort

This algorithm goes through the array the same number of times
as the ammount of elements in the array and sorting them one by one.

Time Complexity: **O(n^2)**

Steps (Naive):

1. Create a nested for loop.
1. Compare the inner loop value with the next value in the inner loop.
1. Swap if the first is less than the second.

```js
function bubbleSort(arr) {
    for(let i = 0; i < arr.length; i++) {
        for(let j = 0; j < arr.length; j++) {
            if(arr[j] < arr[j+1]) {
                // Swap
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr;
}
```

This solution works, however, it makes too many unnecessary comparisons and goes
beyond the end of the array. The array should 'shrink' as the values are sorted.

Steps:

1. Create a nested for loop.
1. Set outer loop equal to the array length and decrement;
1. Set inner loop equal to outer loop's variable minus 1.
1. Compare the inner loop value with the next value in the inner loop.
1. Swap if the first is less than the second.

```js
function bubbleSort(arr) {
    for(let i = arr.length; i > 0; i--) {
        for(let j = 0; j < i - 1; j++) {
            if(arr[j] > arr[j+1]) {
                // Swap
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr;
}
```

This solution is better, however it still does too much checking, especially
if an array has already been sorted. It keeps going until both loops complete,
which is wasteful on an already sorted array.

Steps (Optimized):

1. Create a nested for loop.
1. Create a boolean to track if array has been sorted.
1. Set outer loop equal to the array length and decrement;
1. Set boolean equal to true.
1. Set inner loop equal to outer loop's variable minus 1.
1. Compare the inner loop value with the next value in the inner loop.
1. Swap if the first is less than the second.
1. Set boolean equal to false since a swap was made.
1. If a swap wasn't made in the inner loop, break out of the outer loop.

```js
function bubbleSort(arr) {
    let sorted; // Optimization.
    for(let i = arr.length; i > 0; i--) {
        sorted = true;
        for(let j = 0; j < i - 1; j++) {
            if(arr[j] > arr[j+1]) {
                // Swap
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                sorted = false;
            }
        }
        if(sorted) break;
    }
    return arr;
}
```

#### Selection Sort

Selection sort works by selecting the first element and setting it as the
"minimum". Then as you go through the list, you compare if the next element is
smaller. If it is, you replace it as the smallest until you reach the end. Once
the list has been traversed, you place the value lableed as smallest in the front.

Time Complexity: **O(n^2)**

Steps:

1. Mark first value as the minimum and save the index
1. Compare it to next value, is a new one the minimum? Replace saved index, otherwise move to the next value.
1. Keep repeating step 2 until the entire array has been traversed.
1. Swap the min value at the saved index with the first element in the array.
1. The first value can now be ignored since it's sorted. Mark the next value as the minimum and save the index
1. Repeat steps 2-4 until the entire array has been traversed and the array is sorted!

```js
function selectionSort(arr) {
    for(let i = 0; i < arr.length; i++) {
        let lowest = i;
        for(let j = (i+1); j < arr.length; j++) {
            if(arr[j] < arr[lowest]) {
                lowest = j;
            }
        }
        if(i !== lowest) {
            // Swap
            let temp = arr[i];
            arr[i] = arr[lowest];
            arr[lowest] = temp;
        }
    }
    return arr;
}
```

#### Insertion Sort

Insertion sort works by keeping track of a list and adding elements from
an unsorted list. When these lists are added to the tracked list, they are
placed in the appropriate sorted position until all elements in the unsorted
list have been added.

Time Complexity: **O(n^2)**

### Advance Sorting Algorithms

#### Merge Sort

Merge sort takes a divide and conquer approach to sorting. It takes advantage
of the fact the arrays of size 0 or 1 are already sorted. Merge sort takes a
list of items and divides in into two lists, and keeps on dividing until there
are only _sorted_ lists with just one item. Then, each single item list is merged
into another single item list, and sorted in the process using one comparison. This
is repeated with the new sorted 2 item lists. Since they are already sorted,
only **2** comparisons are needed to merge those 4 items into a sorted list.
This process continues until the whole list is sorted.

Time Complexity: **O(n log n)**

Steps:

1. Break array into halves until you have arrays that are empty or one element.
1. Merge those smaller arrays until the array is back to a full array.
1. Once it's been merged together, return the merged array.

```js
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

mergeSort([10,34,15,5,8,100,27]);
```

#### Quick Sort

Like Merge Sort, Quick Sort takes advantage of the fact the arrays
of size 0 or 1 are already sorted. With Quick Sort a value is selected as
the _pivot_, then all the values less than the pivot are moved to the left
and all the values greater are moved to the right. It can then be assumed
that the pivot is in the right spot. This process is then repeated by using
Quick Sort on a pivot for the left and right sides.

Time Complexity: **O(n log n)**

Steps:

1. Pick a value to be the pivot (It doesn't matter which one)
1. Place all the values less than the pivot on the left, and values greater on the right.
1. The pivot is now in the correct spot.
1. Repeat this process by selecting a pivot on the right and left until the list is sorted.

```js
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
```

#### Radix Sort

## Data Structures

### Collections

#### Arrays

Ordered collection of values. Best used when order matters.

Insertion: O(1)/O(n) Constant if inserting at the end, insertion at the
    beginning is linear since it requires re-indexing
Removal: O(1)/O(n) Constant if removing at the end, removing at the
    beginning is linear since it requires re-indexing
Searching: O(n)
Access: O(1)

#### Hashmaps

Unordered collection of key-value pairs. Best used when order
doesn't matter, very efficient storage.

Insertion: O(1)
Removal: O(1)
Searching: O(n)
Access: O(1)
