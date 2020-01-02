var trap = function(height) {
/* two pointers */
    let ans = 0;
    let [left, right] = [0, height.length - 1];
    let [leftMax, rightMax] = [0, 0];
    
    while (left < right) {
        if (height[left] <= height[right]) {
            if (leftMax < height[left]) leftMax = Math.max(leftMax, height[left]);
            else ans += leftMax - height[left];          
            left++;
        } else {
            if (rightMax < height[right]) rightMax = Math.max(rightMax, height[right]);
            else ans += rightMax - height[right];
            right--
        }
    }
    return ans;
};

const height = [0,1,0,2,1,0,1,3,2,1,2,1];

console.log(trap(height)); //6