# Data Structures & Algorithms

Data Structures and algorithms in programming are essential for efficient
problem solving.

## Basics

### Big O Notation

Big O Notation is a system used to denote the efficiency of an algorithm based
on the growth of inputs. This system allows for the discussion of code
performance and trade-offs between various solutions to a problem.

O(n)

```code
loop(n) {
    print(n)
}
```

Constant: O(1)

```code
loop(n) {
    print(Min(n, 5))
}
```

O(n^2)

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

Notation O(log(n))

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

## Collections

### Arrays

Ordered collection of values. Best used when order matters.

Insertion: O(1)/O(n) Constant if inserting at the end, insertion at the
    beginning is linear since it requires re-indexing
Removal: O(1)/O(n) Constant if removing at the end, removing at the
    beginning is linear since it requires re-indexing
Searching: O(n)
Access: O(1)

### Hashmaps

Unordered collection of key-value pairs. Best used when order
doesn't matter, very efficient storage.

Insertion: O(1)
Removal: O(1)
Searching: O(n)
Access: O(1)

## Recursion

Recursion is a process (function) that calls itself.

Behind the scenes, functions have to be called in a certain order, when the code
is processed it uses a **Call Stack** data sctructure to track the order of
function calls. When a function is called it's placed (pushed) on top of the call
stack, and when the function ends or the **return** keyword is encountered, the
function is removed (popped) from the call stack.
