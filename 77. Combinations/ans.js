var combine = function(n, k) {
    const ans = [];
    var arr = [];
    for (let i = 1; i < n + 1; i++) arr.push(i);
    
    backtrack([], 0);
    
    function backtrack(temArr, index) {
        if (temArr.length == k) {
            ans.push([...temArr]);
            return;
        }
        
        for (let j = index; j < arr.length; j++) {
            temArr.push(arr[j]);
            backtrack(temArr, j+1);
            temArr.pop();
        }              
    }
    return ans;
};

const n = 4;
const k = 2;

console.log(combine(n,k)); //[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]