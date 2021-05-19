#流水线状态转移图出版，

def move(n):
    for i in range(size - 1, n - 1, -1):
        vec[i] = 1 if (initial[i] == 1 or vec[i - n] == 1) else 0
    for i in range(n):
        vec[i] = initial[i]


if __name__ == '__main__':
    loop = True
    print('请输入初始冲突向量：')
    initial = list(map(eval, list(input())))
    print('请输入起始向量：')
    start = list(map(eval, list(input())))
    vec = start.copy()
    size = len(start)
    while loop:
        print('请输入移动次数：')
        n = eval(input())
        if n == -1:
            exit()
        move(n)
        flag1, flag2 = True, True
        for i in range(size):
            print(vec[i], end='')
            if vec[i] != start[i]:
                flag1 = False
            if vec[i] != initial[i]:
                flag2 = False
        if flag1:
            print('(与起始向量相同)', end='')
        if flag2:
            print('(与初始冲突向量相同)', end='')
        print('')
        print('请输入起始向量（回车表示不变）：')
        new = input()
        if len(new) != 0:
            new = list(map(eval, list(new)))
            start = new
            size = len(start)
            move_tmp = [0] * size
        vec = start.copy()
