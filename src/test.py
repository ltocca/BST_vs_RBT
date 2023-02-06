from RBT import RBT
from BST import BST
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer


def insertion_test(t, keys, n):
    start = timer()
    for j in range(n):
        t.insert(keys[j])
    end = timer()
    return round(end - start, 6)


def search_test(t, key):
    start = timer()
    t.find(key)
    end = timer()
    return round(end - start, 6)


def test(shuffle):
    t = BST()
    t_rb = RBT()
    height = []
    height_rb = []
    ins_time = []
    ins_rb_time = []
    search_time = []
    search_rb_time = []

    for i in range(1, 10): ## dovrebbe essere 1000
        n = i * 1000
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

    x = np.arange(1, len(ins_time) + 1) * 1000

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
    plt.ylabel("Tempo di ricerca (in s)")
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
        plot_1.savefig('img/rand/ins.png')
        plot_2.savefig('img/rand/s.png')
        plot_3.savefig('img/rand/h.png')
    else:
        plot_1.savefig('img/w_case/ins.png')
        plot_2.savefig('img//w_case/s.png')
        plot_3.savefig('img/w_case/h.png')

    plt.clf()
    plot_1.clear()
    plot_2.clear()
    plot_3.clear()


def main():
    test(False)
    test(True)


if __name__ == "__main__":
    main()
