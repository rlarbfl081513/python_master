### 인풋의 정수 처리 방식 
   1. 질문 : 23 03434 이거를 n,num = map(int, input().split())이렇게 받아오는데 왜 0이 빠져서 받아지지? 
   2. 대답 : input()은 문자열로 받아오고, map(int, input().split())은 그걸 **정수(int)**로 바꾸기 때문에 숫자 앞의 0은 자동으로 사라져.

         ```python
          n, num = map(int, input().split())
          # 입력: 23 03434
          # 결과: n = 23, num = 3434   ← 앞의 0이 사라짐!
         ```
         ```python
            ## 출력 테스트_1
            n,m = map(int,input().split())
            
            print(f'출력 : {n} 과 {m}')
            
            # 입력 0 00
            # 출력 0 0
            #
            # 입력 0 0
            # 출력 0 0
            #
            # 입력 10 01
            # 출력 10 1
            
            
            ## 출력 테스트_2
            num_arr = [list(map(int,input().split())) for _ in range(2)]
            
            for row in num_arr:
                print(row)
            
            # 입력
            # 0 0 0 0
            # 10 01 001 0001
            # 출력
            # [0, 0, 0, 0]
            # [10, 1, 1, 1]
            
            
            ## 출력 테스트_3
            str_arr = [list(input().split()) for _ in range(2)]
            
            for row in str_arr:
                print(row)
            
            # 입력
            # 0 0 0 0
            # 10 01 001 0001
            # 출력
            # ['0', '0', '0', '0']
            # ['10', '01', '001', '0001']
            
            for row in str_arr:
                for i in row:
                    print(int(i), end=" ")
                print()
            
            # 입력
            # 0 0 0 0
            # 10 01 001 0001
            # 출력
            # 0 0 0 0
            # 10 1 1 1
            
            # 0으로 시작되는 숫자는 문자열로 받으면 가능
            for_str_print = ['0','01','001']  # ['0', '01', '001']
            
            # 0으로 시작하는 숫자를 정수로 썻을때 에러 발생
            # 파이선에서 0으로 시작하는 숫자는 예전에 8진수로 인식됐는데, 파이선3부터는 혼란방지를 위해 막음
            # for_num_print = [0, 01, 001]  # 에러 발생
            
            # 8진수로 쓰고 싶다면 0o를 붙여
            for_num_print = [0o0, 0o01, 0o001]  # [0, 1, 1]
            
            print(for_num_print)

         ```
#
### read line