n = int(input())
arr = []

for _ in range(n):
    parts = input().split()
    cmd = parts[0]

    if cmd == "insert":
        arr.insert(int(parts[1]), int(parts[2]))
    elif cmd == "append":
        arr.append(int(parts[1]))
    elif cmd == "remove":
        arr.remove(int(parts[1]))
    elif cmd == "pop":
        arr.pop()
    elif cmd == "sort":
        arr.sort()
    elif cmd == "reverse":
        arr.reverse()
    elif cmd == "print":
        print(arr)
