function capitalizeWords(arr) {
    // add whatever parameters you deem necessary - good luck!
    let caps = [];
    function helper(wrds) {
        if(wrds.length === 0) return;

        caps.push(wrds[0].toUpperCase());
        helper(wrds.slice(1));
    }
    helper(arr)
    return caps;
}
  
let words = ['i', 'am', 'learning', 'recursion'];
capitalizeWords(words); // ['I', 'AM', 'LEARNING', 'RECURSION']
