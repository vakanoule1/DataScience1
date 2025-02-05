def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
<<<<<<< HEAD
=======
     # Create a new empty list.
    if len(data) == 0 or "":
        return data
    
    new_data = []
    # using a loop
    for rate in data:

    # check if my rate is a digit (considering \n)
        rate = rate.strip()
        if rate.isdigit():

    # if my rate is a digit append it to new_data
            new_data.append(int(rate))
        else:
            rate = rate
    return new_data
>>>>>>> 64fda89a9abe3ebca872a2acedf9a3925a4d405a


    # Create a new empty list.
    if len(data) == 0 or "":
        return data
    
    new_data = []
    # using a loop
    for rate in data:

    # check if my rate is a digit (consideing \n)
        rate = rate.strip()
        if rate.isdigit():

    # if my rate is a digit append it to new_data
            new_data.append(int(rate))
        else:
            rate = rate
    return new_data

def filter_outliers(data: list) -> list:
    """
    Filter all integers from list that are less or equal 30 and greater than or equal to 250

    Arg:
        data (list[str]):list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
<<<<<<< HEAD
        list[int]: list of integers less than 30 and greater than 250, with all non-digit strings removed
=======
        list[int]: list of integers greater than 30 and less than 250, with all non-digit strings removed
>>>>>>> 64fda89a9abe3ebca872a2acedf9a3925a4d405a
    """
    
    
# Create a new empty list.
    
    if len(data) == 0:
        return data
    
    new_data = []
    # using a loop
    # Take in integers
    for rate in data:

     # check if my rate is less or equal to 30 and greater or equal to 250.
        if rate > 30 and rate < 250:
           
<<<<<<< HEAD
    # if my rate is less than 30 and greater than 250 append it to new_data
=======
    # if my rate is greater than 30 and less than 250 append it to new_data
>>>>>>> 64fda89a9abe3ebca872a2acedf9a3925a4d405a
           new_data.append(rate)
        else:
            rate = rate
    return new_data
        
<<<<<<< HEAD
=======

>>>>>>> 64fda89a9abe3ebca872a2acedf9a3925a4d405a
