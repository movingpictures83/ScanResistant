#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sb
import pandas as pd
import seaborn as sns
sns.set(color_codes=True)

from scipy import stats
import matplotlib.pyplot as plt
import os.path as path
# plt.style.use('seaborn-whitegrid')
from itertools import cycle


# In[28]:
import PyIO
import PyPluMA

class ScanResistantPlugin:
 def input(self, inputfile):
   self.parameters = PyIO.readParameters(inputfile)
 def run(self):
     pass
 def output(self, outputfile):
  df = pd.read_csv(PyPluMA.prefix()+"/"+self.parameters["motivation"])

  algos = df["Algorithm"].unique()
  traces=  df["traces"].unique()
  print(traces)
  fig = plt.figure(figsize=(14,14))
  no_of_subplots = 4
  plot_no =0
  index = 0
  filenames = PyIO.readSequential(PyPluMA.prefix()+"/"+self.parameters["traces"])
  for i in range(0, len(filenames)):
      filenames[i] = PyPluMA.prefix()+"/"+filenames[i]

  plt.subplots_adjust(hspace=0.3)

  for file_name in filenames:
    f= open(file_name, 'r')
    
    pages=[]
    for line in f :
        row = line.split(',')
        for  val in row:
            pages.append( int(val ))

    ax = plt.subplot2grid((2, 2), (plot_no, index))
    
    
    ax.plot(range(len(pages)),pages, 'k.', markersize=12)
    ax.set_ylabel('Block Address', fontsize=38)
    if index == 1:
        ax.set_ylabel("")
    if index == 1:
        ax.set_xlabel("")
    if index == 2:
        ax.set_xlabel("")
    ax.set_xlabel('Time', fontsize=38)
    plt.tick_params(labelsize=38)
#     plt.setp(ax.get_xticklabels(), visible=False)
#     plt.setp(ax.get_yticklabels(), visible=False)
    plt.xticks(rotation=0)
    index += 1
  plot_no += 1  
  index = 0
  for trace in traces:
    df_trace = df[ df["traces"]== trace]
    ax = plt.subplot2grid((2, 2), (plot_no, index))
    #print(df_all)       
    x_axis = list(df_trace["Cache size"].unique())
    row_lru = list(df_trace [df_trace["Algorithm"] == "lru" ]["Hit Rate"])
    row_sr_lru = list(df_trace [df_trace["Algorithm"] == "sr-lru" ]["Hit Rate"])
    #row_cr_lfu = list(df_trace [df_trace["Algorithm"] == "cr-lfu" ]["Hit Rate"])
    
    
    ax.plot(x_axis, row_lru, color='red', label='LRU', marker='o', linewidth=5)
    ax.plot(x_axis, row_sr_lru, color='k', label='SR-LRU', marker='s', linewidth=5)
    #ax.plot(x_axis, row_sr_lru, color='#bcbd22', label='SR-LRU', marker='x', linewidth=3)
    #ax.plot(x_axis, row_cr_lfu, color='#e377c2', label='CR-LFU', marker='s', linewidth=2)
    

  #     sb.set_style("whitegrid")
  #     plt.setp(ax.get_xticklabels(), visible=False)
  #     plt.setp(ax.get_yticklabels(), visible=False)
    index += 1
    plt.tick_params(labelsize=38,length=0)
    plt.xticks(rotation=0)
    plt.legend(loc='lower right', fontsize=30)

    ax.set_xlabel('Cache size', fontsize=38)
    ax.set_ylabel('Hit Rate (%)', fontsize=38)
    if index == 2:
        ax.set_ylabel("")

  outf = open(outputfile+".txt", 'w')
  outf.write(str(traces))
  plt.savefig(outputfile, bbox_inches = 'tight', dpi=600)
  plt.show()   


  # In[ ]:





# In[ ]:




