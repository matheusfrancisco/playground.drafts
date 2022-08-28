#!/usr/bin/env python3


class Item:
    def __init__(self, w, p):
        self.w = w
        self.p = p

    def __repr__(self):
        return f'Item(w={self.w}, p={self.p})'

def opt(opt_values, size_pesos, items, n_trucks, idxs):
    st = [1]
    for i in range(1, n_trucks, 1):
        st.append(st[i-1]* (trucks[i-1] + 1))

    for i in range(1, len(items) + 1, 1):
        for j in range(size_pesos):
            ax = [opt_values[size_pesos* (i-1) +j]]
            for k in range(n_trucks):
                if(idxs[k] - items[i-1].w >= 0):
                    ax.append(opt_values[size_pesos*(i-1)+j - st[k]*items[i-1].w] + items[i-1].p)


            opt_values[i*size_pesos+j] = max(ax)

            for k in range(n_trucks):
                if idxs[k] < trucks[k]:
                    idxs[k] += 1
                    break
                idxs[k] = 0
    return opt_values

def calcula_melhores_items(trucks, items):
    size_pesos = 1
    n_trucks = len(trucks)
    for i in range(n_trucks):
        size_pesos *= trucks[i] + 1

    s = (len(items) + 1) * size_pesos

    idxs = [0] * n_trucks
    opt_values = [0] * s

    opt_values = opt(opt_values, size_pesos, items, n_trucks, idxs)
    selected_items = []
    distancia_wk = [1]
    tamanho_x = int(len(opt_values) / (len(items)+ 1))

    for i in range(1, n_trucks, 1):
        distancia_wk.append(distancia_wk[i-1] * (trucks[i-1] + 1))

    idxs = [0] * n_trucks

    k = len(opt_values) - 1

    for i in range(len(items),0, -1):
        ks = k

        for j in range(n_trucks):

            idxs[j] = ks % (trucks[j] + 1)
            ks = int(ks / (trucks[j] + 1))

            ax = [[opt_values[k - tamanho_x] - items[i-1].p, k - tamanho_x]]

            for j in range(n_trucks):
                if (idxs[j] - items[i-1].w >= 0):
                    ax.append([opt_values[k - tamanho_x - distancia_wk[j] * items[i-1].w], k -tamanho_x - distancia_wk[j] - items[i-1].w])

            if max(ax)[1] != k - tamanho_x:
                selected_items.append(i)

            k = max(ax)[1]

    return selected_items

def valor_perdido(i, items):
    n  = set(range(1, len(items) + 1)) - set(i)
    l = 0
    for i in n:
        l += items[i-1].p
    return l


trucks = [5, 10]
items =[Item(8, 6), Item(5, 10), Item(5, 5), Item(3, 10)]

i = calcula_melhores_items(trucks, items)
p = valor_perdido(i, items)

print("valor perdido ", p)
