s = input("s = ")
flag = [1] * 123
temp = 0
for i in range(len(s) - 1):
    if(s[i] == s[i + 1]):
        flag[ord(s[i])] += 1

for i in range(123):
    if(flag[i] != 1):
        print('Included')
        temp += 1
        print(max(flag))
        break

if(temp == 0):
    print("Not included")