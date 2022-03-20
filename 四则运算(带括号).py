#  输入，数字，加减乘除，括号
#  输出：结果


# 用有限自动状态机似乎更明确些




# 计算乘除结果
def cal_mul_div(nums, operators):
    op = operators.pop()
    n2 = nums.pop()
    n1 = nums.pop()
    if op == '*':
        nums.append(n1*n2)
    else:
        nums.append(n1/n2)


# 计算括号内结果（+， -）
def cal_brace(nums, operators):
    ops = []
    ns = []
    while 0 != len(operators):
        op = operators.pop()
        if op == '(':
            break
        ops.append(op)
        ns.append(nums.pop())
    ns.append(nums.pop())
    while 0 != len(ops):
        op = ops.pop()
        n1 = ns.pop()
        n2 = ns.pop()
        if '+' == op:
            ns.append(n1+n2)
        else:
            ns.append(n1-n2)
    nums.append(ns[0])


def compute(expression):
    nums = []
    operators = []
    num = 0
    num_flag = False
    for ch in expression:
        if '0'<=ch<='9':
            num = num*10+ord(ch)-48
            num_flag = True
        elif ch in ['+', '-']:
            if num_flag:
                nums.append(num)
            if 0 != len(operators) and operators[-1] in ['*', '/']:
                cal_mul_div(nums, operators)
            operators.append(ch)
            num = 0
            num_flag = False
        elif ch in ['*', '/']:
            if num_flag:
                nums.append(num)
            if 0 != len(operators) and operators[-1] in ['*', '/']:
                cal_mul_div(nums, operators)
            operators.append(ch)
            num = 0
            num_flag = False
        elif '(' == ch:
            operators.append(ch)
        elif ')' == ch:
            if num_flag:
                nums.append(num)
            if 0 != len(operators) and operators[-1] in ['*', '/']:
                cal_mul_div(nums, operators)
            cal_brace(nums, operators)
            if 0 != len(operators) and operators[-1] in ['*', '/']:
                cal_mul_div(nums, operators)
            num = 0
            num_flag = False
    if num_flag:
        nums.append(num)
    if 0 != len(operators) and operators[-1] in ['*', '/']:
        cal_mul_div(nums, operators)
    cal_brace(nums, operators)
    return nums[0]


print(compute('13+5-6'))
print(compute('20*5/10+2-6'))
print(compute('20*(10-2*3)/10'))
print(compute('20*(10-(6*5-20)*(3*3-6)/6)/10'))
print(compute('10*(6+(3*(5-(8/4))))'))
