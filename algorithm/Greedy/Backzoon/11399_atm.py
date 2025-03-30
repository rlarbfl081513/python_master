
def time(num,total):
    global result

    result += total

    if num == n-1:
        return total

    # print(num,total)
    return time(num+1,total+arr[num+1])



n = int(input())
arr =list(map(int,input().split()))
arr.sort()
result = 0
cnt = 0
# print(arr)
time(0, arr[0])
print(result)