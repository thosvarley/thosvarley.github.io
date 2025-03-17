#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:22:38 2025

@author: thosvarley
"""

import numpy as np 
import matplotlib.pyplot as plt 
import calsight as cal
import scipy.stats as stats

arr = cal.load_video_as_numpy("xenobot_calcium.mp4").mean(axis=-1)

#%%

img = arr.mean(axis=0)
fig = plt.figure(dpi=400, figsize=(2, 1.33))
ax = fig.add_subplot(1,1,1)

ax.imshow(np.sqrt(img), cmap="bone", aspect="auto")

ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.set_xticks([])
ax.set_yticks([])

out_dir =  '/home/thosvarley/Website/thosvarley.github.io/assets/images/'

fig.savefig(out_dir + "xenobot_raw.jpg", bbox_inches="tight")