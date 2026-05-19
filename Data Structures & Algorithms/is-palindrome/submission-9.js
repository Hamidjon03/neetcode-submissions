class Solution {
     isPalindrome(str){
        let left = 0;
        let right = str.length - 1;

        while(left < right){
            while(!this.isAlphaNumeric(str[left]) && left < right){
                left++;
            } 
            while(!this.isAlphaNumeric(str[right]) && right > left){
                right--;
            } 

            if(str[left].toLowerCase() !== str[right].toLowerCase()) return false;
            left++;
            right--;
        }

        return true;

     }

     isAlphaNumeric(char){
        return (
            (char >= "a" && char <= "z") ||
            (char >= "A" && char <= "Z") ||
            (char >= "0" && char <= "9")
        )
     }
}