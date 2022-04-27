# case 분류 함수 유지 보수 프로그램
# case = '1234'로 고정, 가능한 경우의 수 출력
# case 분류 함수 > 프로그램 사용 용, case 분류 count 함수 > 유지 보수용

# x = 입력 받은 수, y = strike 수 , z = ball 수
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


def case_classify_count(x, y, z):
    global total
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
                total += 1
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
                total += 1
    elif y == 1:
        for i in range(len(able_list) - 1, -1, -1):
            if not ((able_list[i][0] == a or able_list[i][1] == b or able_list[i][2] == c or able_list[i][3] == d)
                    ):
                del able_list[i]
                total += 1

    # strike + ball 의 개수가 불일치하는 case 제외
    for i in range(len(able_list) - 1, -1, -1):
        count = 0
        for j in able_list[i]:
            if j == a or j == b or j == c or j == d:
                count += 1
        if count != y + z:
            del able_list[i]
            total += 1

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
            total += 1

    return total


# test tool
able_list = []
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

n1 = int(input('strike: '))
n2 = int(input('ball: '))

total = 0
case_classify_count('1234', n1, n2)

for i in able_list:
    print(i)

print(5040-total)
