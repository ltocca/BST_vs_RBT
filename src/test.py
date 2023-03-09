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


def test(shuffle=False, m=100, nn=10):  # 1000 nodi totali, con incrementi da 10
    height = []
    height_rb = []
    ins_time = []
    ins_rb_time = []
    search_time = []
    search_rb_time = []
    n_means = 100  # numero di test su cui calcolare media

    for i in range(1, m):
        t = BST()
        t_rb = RBT()
        height_m = []
        height_rb_m = []
        ins_time_m = []
        ins_rb_time_m = []
        search_time_m = []
        search_rb_time_m = []
        n = i * nn
        print("Il numero di chiavi è pari a: ", n)
        keys = np.arange(n)
        if shuffle:
            np.random.shuffle(keys)

        for j in range(n_means):

            ins_time_m.append(insertion_test(t, keys, n))
            ins_rb_time_m.append(insertion_test(t_rb, keys, n))

            x = np.random.randint(n)
            search_time_m.append(search_test(t, x))
            search_rb_time_m.append(search_test(t_rb, x))

            height_m.append(t.height())
            height_rb_m.append(t_rb.height())

        ins_time.append(np.mean(ins_time_m))
        ins_rb_time.append(np.mean(ins_rb_time_m))
        search_time.append(np.mean(search_time_m))
        search_rb_time.append(np.mean(search_rb_time_m))
        height.append(np.mean(height_m))
        height_rb.append(np.mean(height_rb_m))

        height_m.clear()
        height_rb_m.clear()
        ins_time_m.clear()
        ins_rb_time_m.clear()
        search_time_m.clear()
        search_rb_time_m.clear()



    x = np.arange(1, len(ins_time) + 1) * nn

    plot_1 = plt.figure(1)
    plt.plot(x, ins_time)
    plt.plot(x, ins_rb_time)
    plt.xlabel("Numero di nodi")
    plt.ylabel("Tempo di inserimento (in s)")
    plt.legend(["ABR", "ARN"])
    if shuffle:
        plt.title("Confronto tempi inserimento: array randomizzato")
    else:
        plt.title("Confronto tempi inserimento: caso peggiore")

    plot_2 = plt.figure(2)
    plt.plot(x, search_time)
    plt.plot(x, search_rb_time)
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


if __name__ == "__main__":
    main()
