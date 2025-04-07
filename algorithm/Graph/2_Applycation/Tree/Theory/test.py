def heappush(heap, data):
    heap.append(data)
    # 추가한 원소의 인덱스를 구한다.
    current = len(heap) - 1
    # 현재 원소가 루트(인덱스 0)에 도달하면 종료
    while current > 0:
        # 추가한 원소의 부모 인덱스를 구한다.
        parent = (current - 1) // 2
        if heap[parent] > heap[current]:
            heap[parent], heap[current] = heap[current], heap[parent]
            # 추가한 원소의 인덱스를 갱신한다.
            current = parent
        else:
            break


#테스트 코드
import heapq
h1 = [3, 4, 6, 8, 5, 7]
h2 = [3, 4, 6, 8, 5, 7]
heappush(h1, 2)
heapq.heappush(h2, 2)
print(f"힙 {h1}에 2를 추가한 결과")
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)
print()
heappush(h1, 3)
heapq.heappush(h2, 3)
print(f"힙 {h1}에 3을 추가한 결과")
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)
