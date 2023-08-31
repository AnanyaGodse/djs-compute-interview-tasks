list = []
N = int(input())
for n in range(N):
    string = input()
    string_split = string.split()

    if (string_split[0] == "insert"):
        i = int(string_split[1])
        e = int(string_split[2])
        list.insert(i, e)
    if (string_split[0] == "print"):
        print(list)
    if (string_split[0] == "remove"):
        e = int(string_split[1])
        list.remove(e)
    if (string_split[0] == "append"):
        e = int(string_split[1])
        list.append(e)
    if (string_split[0] == "sort"):
        list.sort()
    if (string_split[0] == "pop"):
        list.pop(-1)
    if (string_split[0] == "reverse"):
        list.reverse()
