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
    """
    Calculate the moving average of 'n'- size parameter

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: the moving average with window size 6
    """
    # Program to calclate moving average
    # Initialize an empty array to hold the resulting data points.
    average_list = []

    # loop through the original array n - window_size + 1 times.
    # where n is the initial number of elements.
    for i in range(0,len(data), n):
        window = data[i:i + n]

    # Calculate the average of a sequence
        average = sum(window) / len(window)

    #Append the newly calculated window average to our result array
        average_list.append(round(average, 2))
        
    return average_list


def window_stddev(data: list, n: int) -> list:
    """
    Calculate the standard deviation of 'n'- size parameter

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: A list containing the standard deviations with window size 6
    """
    import statistics
    if data == []:
        return data
    
    # Create am empty list to store standard  deviations
    stddev = []

    # Using a loop to iterate through the data
    # starting from the first element and ending at the index
    for i in range(0,len(data), n):
    
    # Create a slice of data representing the current window of size n.
        window_stddev = data[i : i + n]

        if len(window_stddev) == 1:
            continue
        std_dev = statistics.stdev(window_stddev)

    # The window_stddev() function computes the standard deviation of the current window
    # Append it to stddev.
        stddev.append(round(std_dev, 2))
        

    # Return the list containing the calculated standard deviattions for neach window 
    return stddev

