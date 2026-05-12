class Solution {
     isPalindrome(str){
    let left = 0;
    let right = str.length - 1;
    while(left < right){
        while(left < right && !this.alphaNum(str[left])){
            left++;
        }
        while(right > left && !this.alphaNum(str[right])){
            right--;
        }

        if(str[left].toLowerCase() !== str[right].toLowerCase()) return false;
        left++;
        right--;
    }

    return true;
    }

    alphaNum(c){
        return (
            (c >= "A" && c <= "Z") ||
            (c >= "a" && c <= "z") ||
            (c >= "0" && c <= "9")
        )
    }
}