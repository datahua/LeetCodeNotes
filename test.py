def merge( nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    r = m+n-1
    m = m-1
    n = n-1
    
    # 想一个可以handle 一般和极端情况的algo
    # 从右边开始比, 
    # 1. 如果nums1大, 代表num2比值左边所有都将放入nums1这个值的左边
    # 2. 如果nums2大, 则nums2这个值放到nums1 这个值的右边
    # 3. 挤卡怎么处理呢?

    # 最差情况,都需要重新放, n个elements放入前, n个elemnts 换到后面的0
    # 操作: 
    # 1.对比
    # 2. nums1 比 nums2 大: nums1的这个元素换成最后一位的0, 0的位置再换成nums2的值
    # 3. nums1 比 nums2 小: r的位置换nums2, 因为比的是剩下nums2中最右边的值
    # 4. nums1 == nums 2: 
    while m>=0 and n>=0:
        if nums1[m] > nums2[n]:
            # 换 0 
            nums1[m], nums1[r] = nums1[r], nums1[m]
            # 0 换 nums2 的所比值
            nums1[m] = nums2[n]
            # n 向左边移动一个
            n-=1
            # m 向左移动一个
            m-=1
            # r 向左移动一个
            r-=1
            print("m > n", nums1, "r = ", r)
        else:
            nums1[r] = nums2[n]
            # r 向左移动一个
            r-=1
            # n 向左移动一个
            n-=1
            print("m <= n", nums1)


x = [1,2,3,0,0,0]
m=3
y=[2,5,6]
n=3
merge(x,m,y,n)