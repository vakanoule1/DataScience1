def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    # initialises the output data
    maximums = []
    
    #using a loop to take in intgers in range
    for i in range(0,len(data), n):

    # temp variable is used to store the maximum value of the sliding window
        temp = data[i: i + n]

    # temp variable is appended to maximums
        maximums.append(max(temp))
    return maximums


def window_average(data: list, n: int) -> list:
    pass


def window_stddev(data: list, n: int) -> list:
    pass
