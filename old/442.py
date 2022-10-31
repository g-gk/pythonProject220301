n = int(input())
stack1 = list(map(int, input().split()))
stack2 = []
ans = []
for t in range(1, n + 1):
    if t in stack1:
        i = stack1.index(t)
        ans.append([1, i + 1])
        stack2 += stack1[:i + 1]
        stack1 = stack1[i + 1:]
    if t in stack2:
        if t == stack2[-1]:
            stack2.pop()
            if ans[-1][0] == 1:
                ans.append([2, 1])
            else:
                ans[-1][1] += 1
        else:
            print(0)
            exit(0)
for i in ans:
    print(i[0], i[1])
