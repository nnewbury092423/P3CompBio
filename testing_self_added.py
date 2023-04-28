#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:55:39 2023

@author: kalyani
"""
from treeswift import *
import glob
from treelib.todo import *


'''
Test case from README
'''
tree = Tree()
tree.root.set_label('1')
node_2 = Node('2')
node_3 = Node('3')
node_4 = Node('4')
node_5 = Node('5')
node_6 = Node('6')
node_7 = Node('7')
tree.root.add_child(node_2)
tree.root.add_child(node_3)
tree.root.add_child(node_4)
node_2.add_child(node_5)
node_2.add_child(node_6)
node_4.add_child(node_7)

for node in tree.traverse_postorder():
    node.set_edge_length(1)



ancestor_traversal = [i.get_label() for i in node_6.traverse_ancestors()]
print("Traversal from 6 to 1: {}".format(" ".join(ancestor_traversal)))












'''
Test cases from files
'''

tst_dir = "testing/test_data/checking/"

'''
test = 1
n = 100
'''
for test in [1,2,3,4,5]:
    for n in [100,1000,10000,100000]:
        in_filename = tst_dir+"test_{}_{}.nwk".format(test,n)
        euler_filename = tst_dir+"test_{}_{}_euler.txt".format(test,n)
        diameter_filename = tst_dir+"test_{}_{}_diameter.txt".format(test,n)
        queries_filename = tst_dir+"test_{}_{}_queries.txt".format(test,n)
        LCAs_filename = tst_dir+"test_{}_{}_LCAs.txt".format(test,n)
        print("test = {}, n = {}".format(test,n))
        
     #   import pdb; pdb.set_trace()
        tree = read_tree_newick(in_filename)
        
        '''
        Playing with the tree
        '''
        print("Root: {}".format(tree.root.get_label()))
        
        root_children = [c.get_label() for c in tree.root.children]
        print("Direct descendants of root: {}".format(" ".join(root_children)))
        
        gggparent = tree.root
        ggparent = gggparent.children[0]
        gparent = ggparent.children[0]
        parent = gparent.children[0]
        child = parent.children[0]
        ancestor_traversal = [i.get_label() for i in child.traverse_ancestors()]
        print("Traversal from child to gggparent: {}".format(" ".join(ancestor_traversal)))
        
        
        
        '''
        Playing with desired outputs
        '''
        euler_open = open(euler_filename, 'r')
        euler_str = euler_open.readlines()
        desired_E = euler_str[0].split(' ')
        desired_E[-1]=desired_E[-1][:-1]
    
        F_str = euler_str[1].split(' ')
        F_str[-1]=F_str[-1][:-1]
        desired_F = dict()
        for f in F_str:
            k,v = f.split(":")
            desired_F.update({k: int(v)})
        
        H_str = euler_str[2].split(' ')
        desired_H = dict()
        for h in H_str:
            k,v = h.split(":")
            desired_H.update({k: int(v)})
        
        
        test_E,test_F,test_H = euler_tour(tree)
