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

    visited = []
    count = [0]
    layer = 0
    #eulerar = []

    # TODO: REPLACE WITH YOUR CODE!
    #print(T)

    def euler(node,layer):
        visited.append(node.get_label())
        E.append(node.get_label())
        count[0] = count[0] + 1
        layer = layer + 1
        for child in node.child_nodes():
            #import pdb; pdb.set_trace()
            if child not in visited:
                    #import pdb; pdb.set_trace()
                    
                    if child.get_label() not in F:
                        F[child.get_label()] = count[0]
                        H[child.get_label()] = layer
                    euler(child,layer)
                    E.append(node.get_label())
                    count[0] = count[0]+1

        
            #visited.append(node)
            #other.append(node.get_label())
            
        #else:
         #   import pdb; pdb.set_trace()
         #   other.append(node.get_parent().get_label())
    euler(T.root,layer)
    #import pdb; pdb.set_trace()
    
    #raise Exception("NOT IMPLEMENTED ERROR!")
    
    return E,F,H

def compute_diameter(T): # TODO: COMPLETE THIS FUNCTION
    '''
    This function computes a diameter path (i.e. a longest path between any two nodes) of a tree and its length
    :param tree: the tree
    :return: a list P containing the diameter path and a floating point number d showing the diameter length
    '''
    P = []
    d = 0.0
    
    for node in tree.traverse_postorder():
        # TODO: REPLACE WITH YOUR CODE!
        raise Exception("NOT IMPLEMENTED ERROR!")

    return P,d

def find_LCAs(T,Q):
# find LCA for each of the list of nodes in Q
# return the label of the LCA node of each query
    
    #import pdb; pdb.set_trace()
    def __query__(q):
        #import pdb; pdb.set_trace()  
        indices = []
        for elem in q:
            indices.append(F[elem])
        R = max(indices)
        L = min(indices)
        #import pdb; pdb.set_trace()
        i = int(log2(R - L + 1))  
        #import pdb; pdb.set_trace()

        option2 = [H[st[L][i]], H[st[R - (2**i) + 1][i]]]
        min_index = min(enumerate(option2), key=lambda x: x[1]) [0]
        if min_index == 0:
            minimum = st[L][i]
        else:
            minimum = st[R - (2**i) + 1][i]
        #minimum = min(option2)
        #import pdb; pdb.set_trace()      
        return minimum


        import pdb; pdb.set_trace()
        # TODO: REPLACE WITH YOUR CODE!
        raise Exception("NOT IMPLEMENTED ERROR")
        #return None
    E,F,H = euler_tour(T) 


    # generate the sparse table 
    # allocate space
    MAX = len(E) + 1
    st = [[0 for i in range(MAX)]
                 for j in range(MAX)]

   # import pdb; pdb.set_trace()   
    
    for i in range(0, len(E)):
        st[i][0] = E[i]

    #import pdb; pdb.set_trace() 
    j = 1
    while 2**j <= len(E):
        i = 0       #(int i = 1; i <= K; i++)
        while i + 2**j -1 < len(E):   # (int j = 0; j + (1 << i) <= N; j++)    
            option =[H[st[i][j-1]], H[st[i + 2**(j-1)][j-1]]]            
            min_index = min(enumerate(option), key=lambda x: x[1]) [0]
            if min_index == 0:
                st[i][j] = st[i][j-1]
            else:
                st[i][j] = st[i + 2**(j-1)][j-1]
             
            i = i+ 1
            #querey here thingy
        j = j+1
    #import pdb; pdb.set_trace()   
    LCAs = []
    #test = Q[10]
    #lca = __query__(test)
    for q in Q:
        lca = __query__(q)
        LCAs.append(lca)
    #import pdb; pdb.set_trace()
    return LCAs    
