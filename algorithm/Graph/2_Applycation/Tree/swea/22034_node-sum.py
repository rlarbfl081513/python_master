import sys
sys.stdin = open("input.txt")



# 완전이진트리
# 재귀를 통한 완전이진 트리의 부모노드값 구하기
# 자식노드가 있는지 없는지 노드번호를 통해 재귀를 돌면서  값을 가져온다.
# def recusion(node):
#     global n, arr
#
#     # 왼쪽 자식 노드가 있다면 가서 값을 가져와
#     if node*2 <= n:
#         a = recusion(node*2)
#     else:
#         # 왼쪽 자식노드가 없다는건 리프노드라는거
#         # 그럼그냥 문제에서 준 값을 가져와
#         return arr[node]
#
#     # 오른쪽 자식 노드 부르기
#     if node*2+1 <= n:
#         b = recusion(node * 2+1)
#         # 오른쪽 자식 노드가 있다는건 왼쪼 자식도 있다는거임 - 완전이진트리니까
#         # 그래서 두개의 자식값을 더한거로 노드값을 넣어준다.
#         arr[node] = a+b
#         return a+b
#     else:
#         # 오른쪽 자식이 업다면 왼쪽 자식값만으로 값을 넣어준다.
#         arr[node] = a
#         return a

# t = int(input())
# for tc in range(1,1+t):
#     n,m,l = map(int, input().split())
#     arr = [0]*(n+2)
#     for i in range(m):
#         a,b = map(int,input().split())
#         arr[a] = b
#     # recusion(1)
#     print(arr[l])



## 레벨을 구하는 거까지 해보자
# def recusion(node,lav):
#     global n, arr,lav_list
#
#     lav_list[node] = lav
#     # 왼쪽 자식 노드가 있다면 가서 값을 가져와
#     if node*2 <= n:
#         a = recusion(node*2,lav+1)
#     else:
#         # 왼쪽 자식노드가 없다는건 리프노드라는거
#         # 그럼그냥 문제에서 준 값을 가져와
#         return arr[node]
#
#     # 오른쪽 자식 노드 부르기
#     if node*2+1 <= n:
#         b = recusion(node * 2+1,lav+1)
#         # 오른쪽 자식 노드가 있다는건 왼쪼 자식도 있다는거임 - 완전이진트리니까
#         # 그래서 두개의 자식값을 더한거로 노드값을 넣어준다.
#         arr[node] = a+b
#         return a+b
#     else:
#         # 오른쪽 자식이 업다면 왼쪽 자식값만으로 값을 넣어준다.
#         arr[node] = a
#         return a
#
#
# t = int(input())
# for tc in range(1,1+t):
#     n,m,l = map(int, input().split())
#     arr = [0]*(n+2)
#     lav_list = [0] * (n + 1)
#     for i in range(m):
#         a,b = map(int,input().split())
#         arr[a] = b
#
#     recusion(1,1)
#     print(arr[l],lav_list[l])




# ## 재귀 -> 인덱스 번호를 이용한 값 구하기_1
# def repeat(node):
#     global l,arr
#
#     if arr[node] == 0:
#         arr[node] = arr[node*2] + arr[node*2+1]
#
#     if node == l:
#         return
#
#     repeat(node-1)
#
#
# import math
# t = int(input())
# for tc in range(1,1+t):
#     n,m,l = map(int, input().split())
#     arr = [0]*(n+2)
#     ## 이 방식은 자식노드가 무조건 두개 다 있다고 생각하고 돌아가는 코드기에 2를 더해서
#     ## 모든 노드가 두개의 자식노드를 가질때를 생각해서 모든 노드에 2개의 방을 만들어놓아야함
#
#     lav_list = [0] * (n + 1)
#
#     for i in range(m):
#         a,b = map(int,input().split())
#         arr[a] = b
#
#     repeat(n)
#     print(arr[l])




## 재귀 -> 인덱스 번호를 이용한 값 구하기_2
# def repeat(node):
#     global l,arr
#
#     if arr[node] == 0:
#         arr[node] = arr[node*2] + arr[node*2+1]
#
#     if node == l:
#         print(f'#{tc} {arr[node]}')
#         return
#
#     repeat(node-1)
#
# t = int(input())
# for tc in range(1,1+t):
#     n,m,l = map(int, input().split())
#     arr = [0]*(n+2)
#     for i in range(m):
#         a,b = map(int,input().split())
#         arr[a] = b
#     res = 0
#     repeat(n)
