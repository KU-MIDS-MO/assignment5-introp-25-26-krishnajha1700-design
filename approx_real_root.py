def approx_real_root(nums, zone):
    a, b = zone

    def f(x):
        return nums[0] + nums[1]*x + nums[2]*x*x + nums[3]*x*x*x

    left = f(a)
    right = f(b)

    while (b - a) > 1e-12:
        mid = (a + b) / 2
        mval = f(mid)

        if left * mval <= 0:
            b = mid
            right = mval
        else:
            a = mid
            left = mval

    return (a + b) / 2
