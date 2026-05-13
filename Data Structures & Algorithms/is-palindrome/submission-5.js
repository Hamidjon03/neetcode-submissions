class Solution {
     isPalindrome(str){
        let left = 0;
        let right = str.length - 1;

        while(left < right){

            if(!this.isAplphaNumeric(str[left])){
                left++;
            } else if(!this.isAplphaNumeric(str[right])){
                right--;
            }else {
            if(str[left].toLowerCase() !== str[right].toLowerCase()) return false;
            left++;
            right--;
            }
        }

        return true;
    }

    isAplphaNumeric(char){
        return (
            (char >= "a" && char <= "z") ||
            (char >= "A" && char <= "Z") ||
            (char >= "0" && char <= "9")
        )
    }
}