function stringifyNumbers(o) {
    let newObj = {...o};
    let ref = {};

    function helper(data) {
        for(let key in data) {
            if(typeof(data[key]) === 'object') {
                ref = newObj[key];
                stringifyNumbers(data[key]);
            }
            else if(typeof(data[key]) === 'number') {
                if(key in newObj) {
                    newObj[key] = data[key].toString();
                }
                else {
                    ref[key] = data[key].toString();
                }
            }
        }
    }
    helper(o);
    return newObj;
}


let obj = {
    num: 1,
    test: [],
    data: {
        val: 4,
        info: {
            isRight: true,
            random: 66
        }
    }
}


// stringifyNumbers(obj)
console.log(stringifyNumbers(obj));
console.log(obj);

/*
{
    num: "1",
    test: [],
    data: {
        val: "4",
        info: {
            isRight: true,
            random: "66"
        }
    }
}
*/

/* Solution */
// function stringifyNumbers(obj) {
//     var newObj = {};
//     for (var key in obj) {
//       if (typeof obj[key] === 'number') {
//         newObj[key] = obj[key].toString();
//       } else if (typeof obj[key] === 'object' && !Array.isArray(obj[key])) {
//         newObj[key] = stringifyNumbers(obj[key]);
//       } else {
//         newObj[key] = obj[key];
//       }
//     }
//     return newObj;
//   }