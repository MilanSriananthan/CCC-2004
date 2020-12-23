cases = int(input())

def prefix(pre, word):
    if len(pre) > len(word):
        return False
    if pre == word[:len(pre)]:
        return True
    return False

def suffix(suf, word):
    if len(suf) > len(word):
        return False
    if suf == word[-len(suf):]:
        return True
    return False

for i in range(cases):
    line1 = input()
    line2 = input()
    line3 = input()

    if prefix(line1, line2) == True or  prefix(line1, line3) == True or  prefix(line2, line1) == True or  prefix(line2, line3) == True or  prefix(line3, line1) == True or  prefix(line3, line2) == True or suffix(line1, line2) == True or  suffix(line1, line3) == True or  suffix(line2, line1) == True or  suffix(line2, line3) == True or  suffix(line3, line1) == True or  suffix(line3, line2) == True:
        print("No")
    else:
        print("Yes")