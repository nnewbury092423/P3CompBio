from treeswift import *
from math import log2

def euler_tour(T): # TODO: COMPLETE THIS FUNCTION
# perform the euler_tour on the tree T
# output: 
#   + E: the euler tour
#   + F: the index in E where each node first occurs
#   + H: the height (branch distance to root) of each node in E
    E = []
    #E.append(T.root.get_label())
    H = {}
    H[T.root.get_label()] = 0
    F = {}
    F[T.root.get_label()] = 0

    # initialize arrays to keep track
    #visited = {}
    count = [0]
    layer = 0



    def euler(node,layer):

        # add node to visited list (only added once ) and euler tour
        #visited.append(node.get_label())
        E.append(node.get_label())
        # count to keep track of when node was visited in euler tour
        count[0] = count[0] + 1
        # layer is incremented when we look at child nodes
        layer = layer + 1
        for child in node.child_nodes():
            # check for self referential
            #if child not in visited:
            if child.get_label() not in F:
                F[child.get_label()] = count[0]
                H[child.get_label()] = layer
            #add children recusively
            euler(child,layer)
            # in each euler call, also add parents after recursively
            E.append(node.get_label())
            # increment nodes visited after adding to euler tour
            count[0] = count[0]+1

        
    euler(T.root,layer)

    #raise Exception("NOT IMPLEMENTED ERROR!")
    
    return E,F,H

def compute_diameter(T): # TODO: COMPLETE THIS FUNCTION
    '''
    This function computes a diameter path (i.e. a longest path between any two nodes) of a tree and its length
    :param tree: the tree
    :return: a list P containing the diameter path and a floating point number d showing the diameter length
    '''
    #initialize backtracking/
    P = []
    distrec = {}
    paths = {}
    d = 0.0
   

# postorder loops through the leaves first
    for node in T.traverse_postorder():
        
        #calculate and break at root node
        if node.is_root():
            dists =[]
            biurn  = []
            # in case there are more than 2 children/paths coming into root, we only want to add 2 paths
            for children in node.child_nodes():
                dists.append(distrec[children] +  children.edge_length)
                biurn.append(children)


            # build path from our paths array, add the two largest distances together
            indices = sorted(range(len(dists)),key=lambda index: dists[index])
            d = dists[indices[-1]] + dists[indices[-2]]
            front = paths[biurn[indices[-1]].get_label()]
            n1 = biurn[indices[-1]].get_label() 
            r = node.get_label() 
            n2 = biurn[indices[-2]].get_label()
            middle = [n1, r, n2]
            back =paths[biurn[indices[-2]].get_label()]
            
            # we have to reverse the second path.
            P = front + middle +back[::-1] 
            break

        # if the node is a leaf, put in the paths dictionary and the distance recording dictionary as 0. We will reference this node as a child later
        if node.is_leaf():
            distrec[node]  = 0
            paths[node.get_label()] = [] 
        else:
            # best is the longest distance path so far
            best =0
            # biurn is recording which child should be added to our path
            biurn  = {}
            for children in node.child_nodes():
                # adding the edge lengths incident on these children, find the one longest distance path so far
                if best <= distrec[children] +  children.edge_length:
                    best = distrec[children] +  children.edge_length
                    biurn = children
            # the longest distance from our node is then recorded in our distrec list 
            distrec[node] = best
            # this path is also recorded
            paths[biurn.get_label()].append(biurn.get_label())
            paths[node.get_label()] = paths[biurn.get_label()]
    #import pdb; pdb.set_trace()
    return P,d

def find_LCAs(T,Q):
# find LCA for each of the list of nodes in Q
# return the label of the LCA node of each query
    
    def __query__(q):

        # finding the two nodes farthest apart
        indices = []
        for elem in q:
            indices.append(F[elem])
        
        
        R = max(indices)
        L = min(indices)


        # creating sparse table indices
        i = int(log2(R - L + 1))  
        
        # finding solution preloaded in the sparse table
        option2 = [H[st[L][i]], H[st[R - (2**i) + 1][i]]]
        min_index = min(enumerate(option2), key=lambda x: x[1]) [0]
        if min_index == 0:
            minimum = st[L][i]
        else:
            minimum = st[R - (2**i) + 1][i]
        # returning preloaded soltuion
        return minimum
    E,F,H = euler_tour(T) 


    # allocate space for the sparse table
    MAX = len(E) + 1
    st = [[0 for i in range(MAX)]
                 for j in range(MAX)]   
    
    # The first entries range of 1
    for i in range(0, len(E)):
        st[i][0] = E[i]


    # preload solutions into sparse table
    j = 1
    while 2**j <= len(E):
        i = 0       
        while i + 2**j -1 < len(E):

            # find the minimum of our ranges dynamically, using previous range minimum solutions       
            option =[H[st[i][j-1]], H[st[i + 2**(j-1)][j-1]]]            
            min_index = min(enumerate(option), key=lambda x: x[1]) [0]
            if min_index == 0:
                st[i][j] = st[i][j-1]
            else:
                st[i][j] = st[i + 2**(j-1)][j-1]
            i = i+ 1
        j = j+1
    

    # initialize LCA array
    LCAs = []
    # call our query function  after preloading our solutions
    for q in Q:
        lca = __query__(q)
        LCAs.append(lca)
    return LCAs    
