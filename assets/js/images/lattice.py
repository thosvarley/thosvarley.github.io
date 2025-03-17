#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 19:31:29 2025

@author: thosvarley
"""

import networkx as nx 
import matplotlib.pyplot as plt
import pickle 

with open('lattice.pickle', 'rb') as f:
    lattice = pickle.load(f)
    
lattice = nx.to_undirected(lattice)

#%%

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(1,1,1)

ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)

pos = {(((0,), (1,)), ((0,), (1,))): [0., 0.],
       (((0,), (1,)), ((0,),)): [-2, 1], 
       (((0,), (1,)), ((1,),)): [-0.75, 1], 
       (((0,),), ((0,), (1,))): [0.75, 1], 
       (((1,),), ((0,), (1,))): [2, 1], 
       
       (((0,),), ((1,),)): [0,  2], 
       (((0,),), ((0,),)): [-1.35, 2.5], 
       
       (((0,), (1,)), ((0, 1),)): [ -3, 2.5], 
       (((0, 1),), ((0,), (1,))): [3,  2.5],
       
       (((1,),), ((1,),)): [1.35, 2.5], 
       (((1,),), ((0,),)): [0, 3], 
       
       (((0,),), ((0, 1),)): [-2, 4],
       (((1,),), ((0, 1),)): [-0.75, 4],
       (((0, 1),), ((0,),)): [0.75, 4],  
       (((0, 1),), ((1,),)): [2, 4], 
       
       (((0, 1),), ((0, 1),)): [0.        , 5.],}

nx.draw_networkx(G=lattice, pos=pos, with_labels=False, ax=ax,
                 node_color="k", width=2.5)

plt.savefig("lattice.svg", bbox_inches="tight",
            transparent=True)