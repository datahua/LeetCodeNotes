def mySqrt(x: int) -> int:
    if x <= 1:
        return x
    l = 0
    r = x
    while l < r:
        mid = (l + r) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            print("l was ", l)
            l = mid
            print("l now is ", l)
        else:
            print("r is ", r)
            r = mid
            print("r now is ", r)


print(mySqrt(150))
