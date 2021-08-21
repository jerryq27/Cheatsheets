function productOfArray(arr) {
    let result = 1;

    function helper(nums) {
        if(nums.length === 0) {
            return;
        }

        result *= nums[0];
        helper(nums.slice(1));
    }
    helper(arr);

    return result;
}

console.log(productOfArray([1,2,3])); // 6
console.log(productOfArray([1,2,3,10])); // 60