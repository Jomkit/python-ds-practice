def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    set_nums = set(nums)
    freq = {}

    for num in set_nums:
        freq[num] = nums.count(num)
    
    max_num = max(freq.values())
    for (num, often) in freq.items():
        if often == max_num:
            return num