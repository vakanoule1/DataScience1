"""he main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt
""


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<=30 or >=250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
<<<<<<< HEAD
    """ 
=======
    """
>>>>>>> 64fda89a9abe3ebca872a2acedf9a3925a4d405a
    # Initializing variable data 
    if len(data) == 0:
        return data
    data = []

    # open file and read into the `data` list
    file = open(filename)
    for line in file:
        data.append(line)
    file.close
    #print file
    print(data)
    
    #filter out all non-digits
    data = filter_nondigits(data)

    #filter out all outliers
    data = filter_outliers(data)

    #calculate window_max
    maximum = window_max(data, 6)

    #calculate window_avg
    avg = window_average(data, 6)

    #calculate window_stdevs
    tdevs = window_stddev(data, 6)

    #creating lineplots in metaplotlib
    #import the matplotlib library.
    # import the pyplot sub-library, to generate charts and plots
    plt.plot(maximum)
    plt.savefig('images/maximums.png')
    plt.close()

    plt.plot(avg)
    plt.savefig('images/averages.png')
    plt.close()

    plt.plot(tdevs)
    plt.savefig('images/stdevs.png')
    plt.close()
    
    # return all 3 lists
    return maximum, avg, tdevs  
 
<<<<<<< HEAD
=======


>>>>>>> 64fda89a9abe3ebca872a2acedf9a3925a4d405a

if __name__ == "__main__":
    run("data/data1.txt")
