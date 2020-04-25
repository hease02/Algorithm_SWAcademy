# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''

import sys
import queue
sys.stdin = open("input.txt", "r")
q = queue.Queue()

T = int(input())

class posi :
    def __init__(self, dire_x, dire_y):
        self.dire_x = dire_x
        self.dire_y = dire_y

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ladder = list()
    result = 0

    for i in range(0, 100):
        row = list(map(int,input().split()))
        ladder.append(row)

    direction_x = [1, -1, 0] #right, left, down
    direction_y = [0, 0, 1] #right, left, down

    for s in range(0, 100):
        start = s

        if ladder[s][0] is not 1:
            continue

        q.put(posi(s, 0))

        while q.not_empty:
            p = q.get()

            for a in range(0, 3):
                x = p.dire_x + direction_x[a]
                y = p.dire_y + direction_y[a]

                if 0 <= x < 100 and 0 <= y < 100:
                    if ladder[x][y] is 1:
                        q.put(posi(x, y))
                        break
                    if ladder[x][y] is 2:
                        result = start

    print(result)