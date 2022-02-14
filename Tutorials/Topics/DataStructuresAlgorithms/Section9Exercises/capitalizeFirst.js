function capitalizeFirst(arr) {
    // add whatever parameters you deem necessary - good luck!
    for(let i = 0; i < arr.length; i++) {
        arr[i] = arr[i][0].toUpperCase() + arr[i].slice(1, arr[i].length);
    }
    console.log(arr);
}

function capitalizeFirstR(arr) {
    let caps = [];

    function helper(strs) {
        if(strs.length === 0) {
            return;
        }
        caps.push(strs[0][0].toUpperCase() + strs[0].slice(1, strs[0].length));
        helper(strs.slice(1));
    }
    helper(arr);
    return caps;
}
  
capitalizeFirstR(['car','taco','banana']); // ['Car','Taco','Banana']