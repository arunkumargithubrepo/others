# Method 1:
def reverse1(s):
    name = ""
    for i in s:
        name = i + name
    return name


# Method 2 (using recursion):
def reverse2(s):
    if len(s) == 0:
        return s
    else:
        return reverse2(s[1:]) + s[0]


# Method 3:
def reverse3(string):
    string = string[::-1]
    return string


# Method 4:
def reverse4(string):
    string = "".join(reversed(string))
    return string
