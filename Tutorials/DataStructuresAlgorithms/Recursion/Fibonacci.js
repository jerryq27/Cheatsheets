/**
 * Write a function that accepts a number and returns the nth number
 * in the Fibonacci sequence.
 */

function fib(n) {
    if(n <= 2) return 1;

    let prev = 1;
    let curr = 2;

    let count = 3;
    let solution = 0;

    function helper(p, c) {
        if(count === n) return;
        
        count++;
        solution = p + c;
        helper(c, p + c);
    }
    helper(prev, curr);
    return solution;
}

// 1 1 2 3 5 8 13

console.log(fib(4));
console.log(fib(10));
console.log(fib(28));
console.log(fib(35));