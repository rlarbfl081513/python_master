import sys
sys.stdin = open("input.txt")


from collections import deque

# delta = [(-1,0),(0,1),(1,0),(0,-1)]
#
# def cut_tree(start_y,start_x):
#     global arr,end_y, end_x,n,li
#
#     dir = 0
#     for i in range(num):
#         if li[i] == 'L':
#             dir = (dir+3) % 4
#         elif li[i] == 'R':
#             dir = (dir+1) % 4
#         else:
#             if 0 <= start_y + delta[dir][0] < n and 0 <= start_x + delta[dir][1] < n:
#                 if arr[start_y+delta[dir][0]][start_x+delta[dir][1]] != 'T':
#                     start_y, start_x = start_y+delta[dir][0], start_x+delta[dir][1]
#
#
#     if (start_y,start_x) == (end_y, end_x):
#         print(1,end=" ")
#     else:
#         print(0,end=" ")
#
#
# t = int(input())
#
# n = int(input())
# arr = [list(input())for _ in range(n)]
#
# m = int(input())
#
# print('#1',end=" " )
#
# for tc in range(m):
#     num, li = map(str, input().split())
#     num = int(num)
#     li = list(li)
#
#     start_y,start_x = 0,0
#     end_y, end_x = 0, 0
#
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i][j] == 'X':
#                 start_y, start_x = i,j
#             if arr[i][j] == 'Y':
#                 # arr[i][j] = 'G'
#                 end_y, end_x = i,j
#
#     cut_tree(start_y, start_x)



