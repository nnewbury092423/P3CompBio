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
    #import pdb; pdb.set_trace()

    P = []
    distrec = {}
    paths = {}
    d = 0.0
    #dists= [0]
   
    # post order moves 
    # only one for loop - for each node
    for node in T.traverse_postorder():
        if node.is_root():
            #children = node.child_nodes()
            dists =[]
            biurn  = []
            for children in node.child_nodes():
                dists.append(distrec[children] +  children.edge_length)
                #import pdb; pdb.set_trace()
                biurn.append(children)
            #import pdb; pdb.set_trace()
            indices = sorted(range(len(dists)),key=lambda index: dists[index])
            #sorted(dists) 
            #import pdb; pdb.set_trace()
            d = dists[indices[-1]] + dists[indices[-2]]
            front = paths[biurn[indices[-1]].get_label()]
            n1 = biurn[indices[-1]].get_label() 
            r = node.get_label() 
            n2 = biurn[indices[-2]].get_label()
            middle = [n1, r, n2]
            back =paths[biurn[indices[-2]].get_label()]
            P = front + middle +back[::-1] 
            #import pdb; pdb.set_trace()

            break

            #import pdb; pdb.set_trace()
        if node.is_leaf():
            distrec[node]  = 0
            paths[node.get_label()] = [] 
        else:
            # d is nodes
            # for each d[c] add the edge length
            # in the node make sorted list o each children
            best =0
            biurn  = {}
            for children in node.child_nodes():
                # node length insident to this node
                #import pdb; pdb.set_trace()
                if best <= distrec[children] +  children.edge_length:
                    best = distrec[children] +  children.edge_length
                    biurn = children
               # each has longest distance to their children
            distrec[node] = best
            #import pdb; pdb.set_trace()
            paths[biurn.get_label()].append(biurn.get_label())
            paths[node.get_label()] = paths[biurn.get_label()]
            #dists = sorted([d[c] + c.edge_length for c in node.children])
            #d[node] = dists[-1]
            #P = add to path
        # TODO: REPLACE WITH YOUR CODE!
        #raise Exception("NOT IMPLEMENTED ERROR!")


    import pdb; pdb.set_trace()
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
