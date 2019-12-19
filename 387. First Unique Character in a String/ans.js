var firstUniqChar = function(s) {
    var dict = new Map();
    for (var i = 0; i < s.length; i++) {
        if (!dict.get(s[i])) {
            dict.set(s[i], 1);
        } else {
            dict.set(s[i], dict.get(s[i])+1);
        }
    }

    ans = null;
    for (var [key, value] of dict) {
        if (value == 1) {
            ans = key;
            break
        }
    }
    for (var j = 0; j < s.length; j++) {
        if (s[j] == ans) {
            return j
        }
    }
    return -1;
}

var s = "loveleetcode"
console.log(firstUniqChar(s))