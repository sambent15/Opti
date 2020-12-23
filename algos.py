import time
import copy
import math
import random
import numpy as np
from graph import graph_fromFile
from graph import Graph


# Integrer probabilites : generation instance aléatoire
def rndm(n, p):
    g = Graph()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                r = random.randint(1, 100)
                if r <= p * 100:
                    g.add_edge(i, j, 0)
                else:
                    g.add_node(i)
                    g.add_node(j)
    return g


def algo_greedy(g):
    g1 = g.copy()
    c = []
    while sum(g1.degree()) != 0:
        s = g1.node_degMax()
        c.append(s)
        g1.delete_node(s)
    return c


if __name__ == "__main__":
    g = graph_fromFile("file.txt")
    g = rndm(25, 1 / math.sqrt(25))
    a = g.degree()
    print("len :")
    print(len(g))
    print('Nodes :')
    print(g._nodes)
    print("Edges :")
    print(g._out)
    print("Poids :")
    print(g._weight)
    print("Deg :")
    print(a)
    print("DegmaxTEST")
    print(g.node_degMax())
    g1 = g.copy()
    print("Algorithme Glouton :")
    print(algo_greedy(g1))
