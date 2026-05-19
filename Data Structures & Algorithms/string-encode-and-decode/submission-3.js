class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */


    encode(strs) {
        let result = "";
        for(let str of strs){
            result += str.length + "#" + str;
        }
        return result;
    }

    // 5#Hello5#world

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
       console.log(str)
       let result = [];
       const n = str.length;
       let i = 0;
       while(i < n){
        let j = i;
        while(j < n && str[j] !== "#"){
            j++;
        }
        console.log(j)

        const length = parseInt(str.substring(i, j));
        const start = j + 1;
        const end = start + length;
        console.log(`start: ${start}, end: ${end}`)
        console.log(str.substring(start, end))
        result.push(str.substring(start, end));
        i = end;

       }
       
       return result;
       // return origianal data "hello worl?d"
    }
    

}
