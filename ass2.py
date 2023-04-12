def average(sum, total):
    avg_num = sum / list
    return avg_num
int_num = []
list = int(input("enter any integer for number of times"))
for i in range(list):
    num = int(input("enter number:"))
    int_num.append(num)
    sum = 0
    total = 0
for i in int_num:
    sum += i
    w = average(sum, list)
    z = average(sum, list) * 3
    print("the integer of your choice that you are working with is", list)
    print(int_num)
    print("the sum of your number is", sum)
    print("the average is", w)
    print("this is your average multiplied by 3 =", z)
