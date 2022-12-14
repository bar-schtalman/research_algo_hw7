import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import doctest


def max_clique(g: nx.Graph):
    """
    Find the Maximum Clique
    Finds the O( |V| / log|V|)^2 apx of maximum clique set in the worst case.
    >>> G = nx.Graph()
    >>> G.add_nodes_from([1, 2, 3, 4])
    >>> G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
    >>> max_clique(G)
    4
    >>> G1 = nx.Graph()
    >>> G1.add_nodes_from([1, 2, 3, 4, 5, 6])
    >>> G1.add_edges_from([(1, 2), (1, 3), (2, 3),(1,3),(2,6)])
    >>> max_clique(G1)
    3
     >>> G = nx.Graph()
    >>> G.add_nodes_from(['a', 'b', 'c', 'd'])
    >>> G.add_edges_from([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'd')])
    >>> max_clique(G)
    3
    """
    max = 0
    cliques = nx.find_cliques(g)
    for clique in cliques:
        # If the current clique has more nodes than the maximum clique, update the maximum clique
        if len(clique) > max:
            max = len(clique)
    return max


def all_max_clique(G: nx.Graph):
    """
    Find the Maximum Clique
    Finds the exact maximum Clique using brute force search
    >>> G = nx.Graph()
    >>> G.add_nodes_from([1, 2, 3, 4])
    >>> G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
    >>> all_max_clique(G)
    4
    >>> G1 = nx.Graph()
    >>> G1.add_nodes_from([1, 2, 3, 4, 5, 6])
    >>> G1.add_edges_from([(1, 2), (1, 3), (2, 3),(1,3),(2,6)])
    >>> all_max_clique(G1)
    3
     >>> G = nx.Graph()
    >>> G.add_nodes_from(['a', 'b', 'c', 'd'])
    >>> G.add_edges_from([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'd')])
    >>> all_max_clique(G)
    3
    """
    nodes = set(G.nodes())
    max_clique = 0
    for subset in powerset(nodes):
        if is_clique(G, subset):
            if len(subset) > max_clique:
                max_clique = len(subset)
    return max_clique


def is_clique(G: nx.Graph, nodes):
    """
    >>> G = nx.Graph()
    >>> G.add_nodes_from([1, 2, 3, 4])
    >>> G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
    >>> is_clique(G,[1,2,3,4])
    True
    >>> is_clique(G,[1,2,3])
    True
    >>> G1 = nx.Graph()
    >>> G1.add_nodes_from([1, 2, 3, 4, 5, 6])
    >>> G1.add_edges_from([(1, 2), (1, 3), (2, 3),(1,3),(2,6)])
    >>> is_clique(G1,[1,5,6,3])
    False
    >>> is_clique(G1,[1,2,3])
    True
    >>> G2 = nx.Graph()
    >>> G2.add_nodes_from(['a', 'b', 'c', 'd'])
    >>> G2.add_edges_from([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'd')])
    >>> is_clique(G2,['a','b','c'])
    False
    >>> is_clique(G2,['a','b'])
    True
    >>> is_clique(G2,'d')
    True

    """
    for node1, node2 in combinations(nodes, 2):
        if not G.has_edge(node1, node2):
            return False
    return True


def powerset(nodes):
    # Generate all possible subsets of the nodes
    for i in range(1, len(nodes) + 1):
        yield from combinations(nodes, i)


def testing_methods(fun1: callable, fun2: callable, p, n):
    n_vals = []
    rate_vals = []
    t_test = 0
    for j in range(3, n):
        t_test += 1
        G = nx.gnp_random_graph(j, p)
        a = fun1(G)
        b = fun2(G)
        n_vals.append(j)
        rate = b / a
        rate_vals.append(rate)
    plt.plot(n_vals, rate_vals)
    plt.xlabel('n')
    plt.ylabel('rate')
    title = 'p = ' + str(p)
    plt.title(title)
    plt.show()


# testing_methods(all_max_clique,max_clique,0.1,23)
# testing_methods(all_max_clique,max_clique,0.3,21)
# testing_methods(all_max_clique,max_clique,0.5,20)
# testing_methods(all_max_clique,max_clique,0.8,22)
# testing_methods(all_max_clique,max_clique,0.9,24)
if __name__ == '__main__':
    doctest.testmod()






