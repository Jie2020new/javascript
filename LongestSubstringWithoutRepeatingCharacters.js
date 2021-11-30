
@author JieGao
"""

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    s = s.split("");
    if(s.length === 0){
        return 0;
    }
    
    let secondLongestSubString = "";
    let sLength = s.length; 
    let i = 0;
    secondLongestSubString = s[0];
      let longestSubString = secondLongestSubString;
    i++;
    while(i<sLength){
    const indexOfNextLetter = secondLongestSubString.indexOf(s[i]);
        if(indexOfNextLetter>-1){
            longestSubString = (longestSubString.length>secondLongestSubString.length?longestSubString:secondLongestSubString); 
            secondLongestSubString =secondLongestSubString.slice(indexOfNextLetter+1,secondLongestSubString.length);
            secondLongestSubString = secondLongestSubString+s[i];
        }else{
            secondLongestSubString = secondLongestSubString+s[i];
        }
        i++;
    }
    
    return (longestSubString.length>secondLongestSubString.length?longestSubString.length:secondLongestSubString.length);
};

function isLetter(c) {
  return c.toLowerCase() != c.toUpperCase();
}
