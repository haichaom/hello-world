def fib_nums(num):
    steps = [0] * num
    if num == 1 or num == 2:
        return [num]
    if num > 2:
        steps[0], steps[1] = 1, 2
        for i in range(2, num):
            steps[i] = steps[i-1] + steps[i-2]
        return steps

#print(fib_nums(1))
#print(fib_nums(2))
#print(fib_nums(7))

def fib_nums(num):
    last_tmp = 1
    last_two_tmp = 2
    if num <= 0:
        raise Exception('Invalid input num!')
    if num <= 2:
        return last_tmp if (num==1) else last_two_tmp
    else:
        for i in range(2, num):
            result = last_tmp + last_two_tmp
            last_tmp, last_two_tmp = last_two_tmp, result
        return result


#print(fib_nums(1))
#print(fib_nums(2))
#print(fib_nums(3))
#print(fib_nums(4))
#print(fib_nums(5))
if __name__ == '__main__':
    print(fib_nums(4))
