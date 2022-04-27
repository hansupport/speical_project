# 입력 받은 값 참거짓 판별 함수
def check(x, y, z):
    global code
    modify_num = []

    length = 0
    for _ in x:
        length += 1

    if length == 4:
        for i in x:
            if not '0' <= i <= '9':
                code = 'false'
                break

        for i in x:
            if i not in modify_num:
                modify_num.append(i)

        if not len(modify_num) == 4:
            code = 'false'
    else:
        code = 'false'

    if not 0 <= y <= 4:
        code = 'false'

    if not 0 <= z <= 4:
        code = 'false'

    if y + z > 4:
        code = 'false'

    if y == 3 and z == 1:
        code = 'false'

    return code


# 모든 경우의 수 리스트 생성
possible_list = []

# 모든 경우의 수 2차원 리스트 값 생성
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                line = []
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    line.append(i)
                    line.append(j)
                    line.append(k)
                    line.append(l)

                    possible_list.append(line)


while True:
    input_num = input('4자리 수를 입력하세요:')
    strike = int(input('스트라이크의 개수를 입력하세요: '))
    ball = int(input('볼의 개수를 입력하세요: '))

    code = 'true'
    check(input_num, strike, ball)

    if code == 'false':
        print('잘못된 입력입니다')
        continue

    if strike == 4:
        break

    # elif strike == 3:



