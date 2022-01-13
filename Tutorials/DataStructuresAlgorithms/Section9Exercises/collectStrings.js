function collectStrings(o) {
    let strs = [];

    function helper(data) {
        if(!data) return;

        for(let key in data) {
            if(typeof(data[key]) === 'string') {
                strs.push(data[key]);
            }
            else if(typeof(data[key]) === 'object') {
                helper(data[key]);
            }
        }
    }
    helper(o);
    return strs;
}

const obj = {
    stuff: "foo",
    data: {
        val: {
            thing: {
                info: "bar",
                moreInfo: {
                    evenMoreInfo: {
                        weMadeIt: "baz"
                    }
                }
            }
        }
    }
}

collectStrings(obj) // ["foo", "bar", "baz"])