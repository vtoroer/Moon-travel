# В этом файле указаны функции для работы с данными
import numpy as np
import matplotlib.pyplot as plt


def plot(n, file, plotname, variable): # n = TotalSimTime / deltaTime
    data = np.zeros(shape=n)

    for i in range(0, n):
        data[i] = int(file.readline())

    f = plt.figure()
    ax = f.add_subplot()

    ax.plot(data)
    ax.grid()

    #  Добавляем подписи к осям и название графика:
    ax.set_xlabel('время (с)')
    ax.set_ylabel(variable)
    plt.title(plotname)

    # plt.show()

    f.savefig("speed_over_time.pdf", bbox_inches='tight')
    return 0


