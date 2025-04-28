


def solution(name):
  # 조이스틱 조작 횟수
  answer = 0

  # 기본 최소 좌우이동 횟수는 길이 - 1
  min_moves = len(name) - 1

  for i, char in enumerate(name):
      # 해당 알파벳 변경 횟수 추가
      answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
      
      # 해당 알파벳 다음부터 연속된 A 찾기
      next_idx = i + 1
      while next_idx < len(name) and name[next_idx] == 'A':
          next_idx += 1
          
      # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교
      # i: 현재 위치, next_idx: 다음 알파벳 위치, len(name): 문자열 전체 길이
      # i+i+len(name)-next_idx: 현재 위치에서 되돌아가서 다음 알파벳 위치로 가는 경우
      min_moves = min([min_moves, i + i + len(name) - next_idx, 2 * (len(name) - next_idx) + i])
          
  # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 더하기
  answer += min_moves

  return answer