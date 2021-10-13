# Using numpy and matplotlib/pylab generate bar plots for appropriate data.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    a = np.array([22, 87, 5, 43, 56,
                  73, 55, 54, 11,
                  20, 51, 5, 79, 31,
                  27])

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.hist(a, bins=[0, 25, 50, 75, 100])

    plt.show()
