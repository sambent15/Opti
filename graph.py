import copy
import random
import numpy as np
import math


class Graph:
    def __init__(self, nodes=None, edges=None, weights=None, visites=None):
        if (nodes is not None and edges is not None) and weights is not None and visites is not None:
            self._nodes = nodes
            self._out = edges
            self._weight = weights
            self._visites = visites
        else:
            self._nodes = []
            self._out = dict()
            self._weight = dict()
            self._visites = []

    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def add_node(self, u):
        if u not in self._nodes:
            self._nodes.append(u)
            self._out[u] = []

    def add_edge(self, u, v, weight=None):
        if u not in self._nodes:
            self.add_node(u)
        if v not in self._nodes:
            self.add_node(v)
        if v not in self._out[u]:
            self._out[u].append(v)
        if u not in self._out[v]:
            self._out[v].append(u)
        self._weight.update({(u, v): weight})
        self._weight.update({(v, u): weight})

    def delete_node(self, u):
        if u in self._nodes:
            self._nodes.remove(u)
            del self._out[u]

            for k in self._out:
                if u in self._out[k]:
                    self._out[k].remove(u)

            l = [k for k in self._weight if u in k]
            for e in l:
                del self._weight[e]

    def delete_nodes(self, l):
        for e in l:
            self.delete_node(e)

    def degree(self):
        l = [len(self._out[u]) for u in self._nodes]
        return l

    def node_degMax(self):
        l = self.degree()
        deg_max = max(l)
        return self._nodes[l.index(deg_max)]

    def getDegMax(self):
        l = self.degree()
        if (l == []):
            return 0
        return max(l)

    def copy(self):
        return Graph(copy.deepcopy(self._nodes),
                     copy.deepcopy(self._out),
                     copy.deepcopy(self._weight),
                     copy.deepcopy(self._visites))


def read_file(filepath):
    l=[]
    l2=[]
    boolsommet=False
    boolaretes=False
    with open(filepath) as fp:
       for line in fp:
           values = line.split()
           if (values[0]=="Sommets"):
               boolsommet=True
               continue
           if (values[0]=="Aretes"):
               boolaretes=True
               continue
           if (values[0]=="Nombre" and values[2]=="aretes"):
               boolsommet=False
               continue
           if (boolsommet==True):
               l.append(int(values[0]))
           if (boolaretes==True):
               l2.append((int(values[0]),int(values[1])))
    return l,l2


def graph_fromFile(filepath):
  nodes,edges=read_file(filepath)
  g=Graph()
  for u in nodes:
    g.add_node(u)
  for e in edges:
    g.add_edge(e[0],e[1],0)
  return g