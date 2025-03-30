ar = input().strip().split(" ")
ar = map(int, ar)
ar = list(ar)

nums = set(map(int, input().strip().split(" ")))
order = []

def f(ar: list, nums: set):
    for i in nums:
        if i in ar:
            order.append(ar.index(i))
        else:
            order.append(None)

    s = '{'
    for i in range(len(nums)):
        s += str(nums[i]) + ': ' + str(order[i]) + "; "
    s += '}'
    return s



print(f(ar, nums))


#dict and other py