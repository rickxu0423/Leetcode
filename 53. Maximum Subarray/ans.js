nums = [-2,1,-3,4,-1,2,1,-5,4]
var maxSubArray = function(nums) {
    
    var n = nums.length;
    var SUM = nums[0];
    for (var i = 1; i < n; i++) {
        nums[i] = Math.max(nums[i]+nums[i-1], nums[i])
        SUM = Math.max(nums[i], SUM)
    };
    return SUM
};
console.log(maxSubArray(nums))