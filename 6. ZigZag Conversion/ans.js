var convert = function(s, numRows) {
    if (numRows == 1) return s;
    
    var container = [];
    for (var i = 0; i < numRows; i++) container.push("");
    
    var up = true;
    var index = 0;
    
    for (str of s) {
        if (index == 0 || index == numRows-1) up = !up;
        
        if (up == false) {
            container[index] += str;
            index++;
        } else {         
            container[index] += str;
            index--;
        }
    }
    
    return container.join("");
};

const [s, numRows] = ["PAYPALISHIRING", 3];

console.log(convert(s, numRows)); //"PAHNAPLSIIGYIR"