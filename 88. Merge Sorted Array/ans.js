var merge = function(nums1, m, nums2, n) {
    var [index1, index2, p] = [m-1, n-1, m+n-1];
    while (index1 >= 0 && index2 >= 0) {
        if (nums1[index1] <= nums2[index2]) {
            nums1[p] = nums2[index2];
            index2--;
        } else {
            nums1[p] = nums1[index1];
            index1--
        }
        p--;
    }
    while (index2 >= 0) {
        nums1[index2] = nums2[index2];
        index2--;
    }
    return nums1;
};

const nums1 = [4,5,6,0,0,0];
const m = 3;
const nums2 = [1,2,3];
const n = 3;

console.log(merge(nums1, m, nums2, n)); // [1,2,3,4,5,6]