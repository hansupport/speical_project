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


# 입력 받은 값을 자리별로 나누고, 불가능한 경우의 수를 제외하는 함수
def case_classify(x, y, z):
    x = int(x)
    a = x // 1000
    b = x // 100 % 10
    c = x // 10 % 10
    d = x % 10
    if y == 3:
        for i in range(len(able_list) - 1, -1, -1):
            if not ((able_list[i][0] == a and able_list[i][1] == b and able_list[i][2] == c)
                    or (able_list[i][0] == a and able_list[i][1] == b and able_list[i][3] == d)
                    or (able_list[i][0] == a and able_list[i][2] == c and able_list[i][3] == d)
                    or (able_list[i][1] == b and able_list[i][2] == c and able_list[i][3] == d)
                    ):
                del able_list[i]
    elif y == 2:
        for i in range(len(able_list) - 1, -1, -1):
            if not ((able_list[i][0] == a and able_list[i][1] == b)
                    or (able_list[i][0] == a and able_list[i][2] == c)
                    or (able_list[i][0] == a and able_list[i][3] == d)
                    or (able_list[i][1] == b and able_list[i][2] == c)
                    or (able_list[i][1] == b and able_list[i][3] == d)
                    or (able_list[i][2] == c and able_list[i][3] == d)
                    ):
                del able_list[i]
    elif y == 1:
        for i in range(len(able_list) - 1, -1, -1):
            if not ((able_list[i][0] == a or able_list[i][1] == b or able_list[i][2] == c or able_list[i][3] == d)
                    ):
                del able_list[i]

    # strike + ball 의 개수가 불일치하는 case 제외
    for i in range(len(able_list) - 1, -1, -1):
        count = 0
        for j in able_list[i]:
            if j == a or j == b or j == c or j == d:
                count += 1
        if count != y + z:
            del able_list[i]

    # strike 의 개수가 불일치하는 case 제외
    for i in range(len(able_list) - 1, -1, -1):
        count = 0
        if able_list[i][0] == a:
            count += 1
        if able_list[i][1] == b:
            count += 1
        if able_list[i][2] == c:
            count += 1
        if able_list[i][3] == d:
            count += 1
        if count != y:
            del able_list[i]


# 모든 경우의 수 리스트 생성
able_list = []

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

                    able_list.append(line)


while True:
    # input
    input_num = input('4자리 수를 입력하세요:')
    strike = int(input('스트라이크의 개수를 입력하세요: '))
    ball = int(input('볼의 개수를 입력하세요: '))

    # wrong input check
    code = 'true'
    check(input_num, strike, ball)
    if code == 'false':
        print('잘못된 입력입니다')
        continue

    # correct answer > while loop break
    if strike == 4:
        break

    # case classify
    case_classify(input_num, strike, ball)

    # print probability
