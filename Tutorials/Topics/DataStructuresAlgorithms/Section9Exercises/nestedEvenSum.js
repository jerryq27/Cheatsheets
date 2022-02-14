function nestedEvenSum(obj) {
    // add whatever parameters you deem necessary - good luck!
    let sum = 0;

    function helper(data) {
        if(!data) return;
        let val = Object.values(data)[0];
    
        if(typeof(val) === "number") {
            console.log(`Key: ${Object.keys(data)[0]}, Val: ${val}`);
            if(val % 2 === 0) {
                sum += val;
            }
            helper(Object.values(data)[1]);
        }
        else {
            console.log(`Key: ${Object.keys(data)[0]}, Val: ${Object.toString(val)}`);
            helper(Object.keys(data)[0]);
        }
    }
    helper(obj);
    return sum;
}
  
  
var obj1 = {
    outer: 2,
    obj: {
        inner: 2,
        otherObj: {
            superInner: 2,
            notANumber: true,
            alsoNotANumber: "yup"
        }
    }
}

var obj2 = {
    a: 2,
    b: {b: 2, bb: {b: 3, bb: {b: 2}}},
    c: {c: {c: 2}, cc: 'ball', ccc: 5},
    d: 1,
    e: {e: {e: 2}, ee: 'car'}
};

console.log(nestedEvenSum(obj1)); // 6
console.log(nestedEvenSum(obj2)); // 10

/* Solution */
// function nestedEvenSum (obj, sum=0) {
//     for (var key in obj) {
//         if (typeof obj[key] === 'object'){
//             sum += nestedEvenSum(obj[key]);
//         } else if (typeof obj[key] === 'number' && obj[key] % 2 === 0){
//             sum += obj[key];
//         }
//     }
//     return sum;
// }