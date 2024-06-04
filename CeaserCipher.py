def first_sol():
    s = input()
    res = ""
    for char in s:
        if char.islower():
            if ord(char) + 3 > 122:
                res += chr(97 + (ord(char) + 3) % 122)
            else:
                res += chr(ord(char) + 3)
        elif char.isupper():
            if ord(char) + 3 > 90:
                res += chr(65 + (ord(char) + 3) % 90)
            else:
                res += chr(ord(char) + 3)
    
    count = 0
    for i in range(len(res)):
        if i + 1 < len(res) and res[i] == res[i + 1]:
            count += 1
        else:
            print(res[i], end="")
            if count + 1 > 1:
                print(count + 1, end="")
            count = 0
first_sol()
