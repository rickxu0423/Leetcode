S = "loveleetcode"
C = "e"
def shortestToChar(S, C):
    List = ["" for letter in S]
    for i in range(len(S)):
        if S[i] == C:
            List[i] = 0
    for j in range(len(List)):
        if List[j] == 0:
            left, right = int(j) - 1, int(j) + 1
            leftcounter, rightcounter = 1, 1
            while left >=0:
                if List[left] == 0:
                    break
                if not List[left] or List[left] > leftcounter:
                    List[left] = leftcounter
                    left -= 1
                    leftcounter += 1
                else:
                    break
            while right < len(List):
                if List[right] == 0:
                    break
                if not List[right]:
                    List[right] = rightcounter
                    right += 1
                    rightcounter += 1
                else:
                    break
    return List
print(shortestToChar(S, C))