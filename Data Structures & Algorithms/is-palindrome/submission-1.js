class Solution {
     isPalindrome(str){
    let arr = [];
    str = str.toLowerCase();
    for(let s of str){
        let char = s.charCodeAt(0);
        if( (char < 97 && char > 57 ) || char > 122 || char < 48) continue;
        if(s === " ") continue;
        arr.push(s)
    }
    console.log(arr);
    
    let left = 0;
    let right = arr.length - 1;
    while(left < right){
        if(arr[right] !== arr[left]) return false;
        left++;
        right--;
    }
    return true;
}
}