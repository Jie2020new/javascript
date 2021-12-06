/**
 * @author JieHouse Robber
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
     const numHouses = nums.length;
    let robMoney =[];
    if(numHouses === 0){
        return 0;
    }else if(numHouses === 1){
        return nums[0];
 }else{
       robMoney.push(nums[0]);
        robMoney.push(Math.max(nums[0],nums[1]));
        for(let i = 2; i < numHouses; i++){
            robMoney.push(Math.max(robMoney[i-1], nums[i]+robMoney[i-2]));
        }
    }
        
        return robMoney[robMoney.length-1];
};
