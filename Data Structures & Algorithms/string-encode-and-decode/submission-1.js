class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let result = "";

        for(let str of strs){
            let length = str.length;
            result += length + "#" + str;
        }

        return result;
    }


     // "5#Hello5#World2#C#2#is5#cool#"

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let result = [];
        let i = 0
        while(i < str.length){
            let j = i;
            while(str[j] !== "#"){
                j++;
            }

            let length = parseInt(str.substring(i, j));
            let start = j + 1;
            let end = start + length;
            result.push(str.substring(start, end));

            i = end;


        }

        return result;
    }
    

}
