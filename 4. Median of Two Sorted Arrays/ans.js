nums1 = [1,2]
nums2 = [3,4]

var findMedianSortedArrays = function(nums1, nums2) {
    if (nums1.length > nums2.length) {
        return(findMedianSortedArrays(nums2, nums1))
    }
    var x = nums1.length;
    var y = nums2.length;
    var low = 0;
    var high = x;
    while (low <= high) {
        var partitionX = Math.floor((low + high) / 2);
        var partitionY = Math.floor((x + y + 1) / 2 - partitionX);
        var maxLeftX = (partitionX == 0) ? -1 * Number.MAX_VALUE : nums1[partitionX-1];
        var minRightX = (partitionX == x) ? Number.MAX_VALUE : nums1[partitionX];
        var maxLeftY = (partitionY == 0) ? -1 * Number.MAX_VALUE : nums2[partitionY-1];
        var minRightY = (partitionY == y) ? Number.MAX_VALUE : nums2[partitionY];
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((x+y) % 2 == 0) {
                return ((Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2);
            }
            else {
                return (Math.max(maxLeftX, maxLeftY));
            }
        }
        else if (maxLeftX > minRightY) {
            high = partitionX - 1;
        }
        else {
            low = partitionX + 1;
        }
    }
    
};


console.log(findMedianSortedArrays(nums1, nums2))