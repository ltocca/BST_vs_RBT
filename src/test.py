from RBT import RBT
from BST import BST
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
from scipy.interpolate import splrep, splev


def insertion_test(t, keys, n):
    start = timer()
    for j in range(n):
        t.insert(keys[j])
    end = timer()
    return round(end - start, 4)


def search_test(t, key):
    start = timer()
    t.find(key)
    end = timer()
    return round(end - start, 6)


def spline(x, y, p=2.0):  # implementazione bspline al fine di approssimare l'andamento dei grafici
    bspl = splrep(x, y, s=p)
    s = splev(x, bspl)
    return s


def exp_moving_averages(array):
    x = 1  # fattore di correzione
    ma = []  # vettore vuoto media
    ma.append(array[0])
    for i in range(1, len(array)):
        window_average = round((x * array[i]) + (1 - x) * ma[-1], 2)
        ma.append(window_average)
    array = ma
    return array


def test(shuffle=False, m=100, nn=100):
    height = []
    height_rb = []
    ins_time = []
    ins_rb_time = []
    search_time = []
    search_rb_time = []

    for i in range(1, m):
        t = BST()
        t_rb = RBT()
        n = i * nn
        print("Il numero di chiavi è pari a: ", n)
        keys = np.arange(n)
        if shuffle:
            np.random.shuffle(keys)

        ins_time.append(insertion_test(t, keys, n))
        ins_rb_time.append(insertion_test(t_rb, keys, n))

        x = np.random.randint(n)
        search_time.append(search_test(t, x))
        search_rb_time.append(search_test(t_rb, x))

        height.append(t.height())
        height_rb.append(t_rb.height())

        insertion = exp_moving_averages(ins_time)
        insertion_rb = exp_moving_averages(ins_rb_time)

    x = np.arange(1, len(ins_time) + 1) * nn

    plot_1 = plt.figure(1)
    plt.plot(x, spline(x, insertion))
    plt.plot(x, spline(x, insertion_rb))
    plt.xlabel("Numero di nodi")
    plt.ylabel("Tempo di inserimento (in s)")
    plt.legend(["ABR", "ARN"])
    if shuffle:
        plt.title("Confronto tempi inserimento: array randomizzato")
    else:
        plt.title("Confronto tempi inserimento: caso peggiore")

    plot_2 = plt.figure(2)
    plt.plot(x, spline(x, search_time))
    plt.plot(x, spline(x, search_rb_time))
    plt.xlabel("Numero di nodi")
    plt.ylabel("Tempo di ricerca (s)")
    plt.legend(["ABR", "ARN"])
    if shuffle:
        plt.title("Confronto tempi ricerca: array randomizzato")
    else:
        plt.title("Confronto tempi ricerca: caso peggiore")

    plot_3 = plt.figure(3)
    plt.plot(x, height)
    plt.plot(x, height_rb)
    plt.xlabel("Numero di nodi")
    plt.ylabel("Altezza")
    plt.legend(["ABR", "ARN"])
    if shuffle:
        plt.title("Confronto altezze: array randomizzato")
    else:
        plt.title("Confronto altezze: caso peggiore")

    if shuffle:
        plot_1.savefig('img/rand/ins_' + str(m * nn) + '.png')
        plot_2.savefig('img/rand/s_' + str(m * nn) + '.png')
        plot_3.savefig('img/rand/h_' + str(m * nn) + '.png')

    else:
        plot_1.savefig('img/w_case/ins_' + str(m * nn) + '.png')
        plot_2.savefig('img/w_case/s_' + str(m * nn) + '.png')
        plot_3.savefig('img/w_case/h_' + str(m * nn) + '.png')

    plt.clf()
    plot_1.clear()
    plot_2.clear()
    plot_3.clear()


def main():
    test()
    test(True)
    test(False, 100, 1000)
    test(True, 100, 1000)


if __name__ == "__main__":
    main()
