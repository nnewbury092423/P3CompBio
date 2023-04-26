from treeswift import *

def euler_tour(T): # TODO: COMPLETE THIS FUNCTION
# perform the euler_tour on the tree T
# output: 
#   + E: the euler tour
#   + F: the index in E where each node first occurs
#   + H: the height (branch distance to root) of each node in E
    E = []
    H = {}
    F = {}
   
    # TODO: REPLACE WITH YOUR CODE!
    raise Exception("NOT IMPLEMENTED ERROR!")
    
    return E,F,H

def compute_diameter(T): # TODO: COMPLETE THIS FUNCTION
    '''
    This function computes a diameter path (i.e. a longest path between any two nodes) of a tree and its length
    :param tree: the tree
    :return: a list P containing the diameter path and a floating point number d showing the diameter length
    '''
    P = [1]
    d = 0.0
    
    for node in tree.traverse_postorder():
        # TODO: REPLACE WITH YOUR CODE!
        raise Exception("NOT IMPLEMENTED ERROR!")

    return P,d

def find_LCAs(T,Q):
# find LCA for each of the list of nodes in Q
# return the label of the LCA node of each query
    def __query__(q):
        # TODO: REPLACE WITH YOUR CODE!
        raise Exception("NOT IMPLEMENTED ERROR")
        return None

    E,F,H = euler_tour(T) 
    LCAs = []
    for q in Q:
        lca = __query__(q)
        LCAs.append(lca)
    return LCAs    
