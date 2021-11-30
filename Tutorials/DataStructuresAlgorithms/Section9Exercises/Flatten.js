function flatten(arr) {
    // add whatever parameters you deem necessary - good luck!
    let flatArr = [];

    function helper(nums) {
        for(let i = 0; i < nums.length; i++) {
            if(Array.isArray(nums[i])) {
                helper(nums[i]);
            }
            else {
                flatArr.push(nums[i]);
            }
        }
    }
    helper(arr);
    console.log(flatArr);
    return flatArr;
  }
  
  flatten([1, 2, 3, [4, 5] ]) // [1, 2, 3, 4, 5]
  flatten([1, [2, [3, 4], [[5]]]]) // [1, 2, 3, 4, 5]
  flatten([[1],[2],[3]]) // [1,2,3]
  flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) // [1,2,3