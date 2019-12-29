var permute = function(nums) {
    const n = nums.length;
    const ans = [];
    
    backtrack(0);
    
    function backtrack(first) {
        if (first == n) {
            ans.push([...nums]);
        }
        
        for (var i = first; i < n; i++) {
            [ nums[first], nums[i] ] = [ nums[i], nums[first] ];
            
            backtrack(first + 1);
            
            [ nums[first], nums[i] ] = [ nums[i], nums[first] ];
        }
    };
    
    return ans
}

const nums = [1,2,3];

console.log(permute(nums)); //[ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]