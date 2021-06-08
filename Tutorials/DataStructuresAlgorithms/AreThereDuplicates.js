/**
 * Implement a function which accepts a variable number of arguments, and checks
 * whether there are any duplicates among the arguments passed in.
 * 
 * Pattern: Frequency Counter Pattern or Multiple Pointers Pattern
 */

/* My solution */
 function areThereDuplicates(...args) {
    if(args.length === 0) {
        return false;
    }

    let countPointer = 0;

    for(let i = 0; i < args.length; i++) {
        if(i !== countPointer) {
            if((countPointer + 1) === args.length) {
                return false;
            }
            else if(args[i] === args[countPointer]) {
                return true;
            }
            else if((i + 1) === args.length) {
                i = 0;
                countPointer++;
            }
        }
    }
}

/* Frequency Counter solution */
function areThereDuplicates(...args) {
    let collection = {};
    for(let val in args) {
        collection[args[val]] = (collection[args[val]] || 0);
    }

    for(let key in collection) {
        if(collection[key] > 1) return true;
    }
    return false;
}

/* Mulitple Pointers solution */
function areThereDuplicates(...args) {
    args.sort((a, b) => a > b);
    
    // Two pointers
    let start = 0;
    let next = 1;
    while(next < args.length) {
        if(args[start] === args[next]) {
            return true;
        }
        start++;
        next++;
    }
    return false;

    // One liner:
    // return new Set(args).size !== args.length;
}

// console.log(areThereDuplicates(1, 2, 3));
// console.log(areThereDuplicates(1, 2, 2));
// console.log(areThereDuplicates('a', 'b', 'b', 'a'));