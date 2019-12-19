var firstUniqChar = function(s) {
    dict = {}
    for (var i = 0; i < s.length; i++) {
        if (!dict[s[i]]) {
            dict[s[i]] = 1;
        } else {
            dict[s[i]] += 1;
        }
    }
    for (var j = 0; j < s.length; j++) {
        if (dict[s[j]] == 1) {
            return j
        }
    }
    return -1
}

var s = "loveleetcode"
console.log(firstUniqChar(s))