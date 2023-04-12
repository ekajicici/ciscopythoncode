def median(nums):
    n = len(nums)
    m = n // 2
    if n % 2 == 0:
        return (nums[m - 1] + nums[m]) / 2
    else:
        return nums[m]
print(median([1, 3, 6, 9, 12]))
print("TO FIND THE MEDIAN OF X NUMBERS")
range_no = int(input("HOW MANY NUMBERS?"))
bl = []
for j in range(range_no):
    g = int(input("ENTER A VALUE:"))
    bl.append(g)
    bl.sort()
print(bl)
print("THE MEDIAN IS:", median(bl))