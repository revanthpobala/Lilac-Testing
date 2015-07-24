#####################################################################################
#extract.py
#Authors: Revanth Pobala and Hussain Mucklai.
#This project is about the Testing of Lilac(Lightweight low latency anonymous chat)
#This program will provide the graph for cdf(Cumulative Distribution function)
#####################################################################################
import os
import matplotlib.pyplot as plt
from pylab import *
from scipy.stats import norm
import matplotlib.patches as mpatches
from bisect import bisect_left


class discrete_cdf:
    def __init__(self,data):
        self._data = data # must be sorted
        self._data_len = float(len(data))

    def __call__(self,point):
        return (len(self._data[:bisect_left(self._data, point)]) / 
                self._data_len)

class extract():



    def __init__(self):
        self.to_draw = []    
    
    
    def read_from_file(self,filename):
        file = open(filename,'rw')
        return file
    
    
    
    def merge_files(self):
        os.system('cat /home/revanth/Projects/workspace/Lilac_Testing/src/users/logs/*.txt >/home/revanth/Projects/workspace/Lilac_Testing/src/Results/finalfile.log')
        
        

    def add_to_dict(self):
        items = {}
        graph_values = []
        to_draw = []
        median = []
        sum = 0
        file = extract.read_from_file('finalfile.log')
        for i in file.readlines():
            if len(i.strip()) != 0:
                content = i.split(',')
                msg = content[0].strip()
                Time = float(str(content[1].strip()))
                if msg not in items:
                    items[msg] = []
                items[msg].append(Time)
        
        for i in items:
            for j in items[i]:
                graph_values.append(float(max(items[i])- min(items[i])))
        #graph_values = set(graph_values)
        for i in graph_values:
            if i >= 1.5:
                to_draw.append(i*0.1)
                sum = sum+i
        avg = np.average(sum)/len(to_draw)*0.1
        #plt.plot(0,avg)
        self.to_draw = np.array(to_draw)
        anthax =  np.arange(0,len(to_draw)) 
        plt.plot(anthax, self.to_draw, '-')
        plt.ylabel('Time (Seconds)')
        plt.xlabel('Number of Messages')
        plt.title(r'Time  vs Number of messages')
        plt.show()   
 
    def draw_cdf(self):
        self.to_draw = sort(self.to_draw)
        #print self.to_draw 
        cdf = discrete_cdf(self.to_draw)
        xvalues =  np.arange(0,6)
        yvalues = [cdf(point) for point in xvalues]
        plt.plot( yvalues)
        #plt.xticks(xvalues)
       # red_patch = mpatches.Patch(color='green', label='')
       # plt.legend(handles=[red_patch])
        plt.title(r'Cumulative Distribution Function')
        plt.ylabel('cdf of messages')
        plt.xlabel('Time')
        plt.show()

    

extract =  extract()
extract.merge_files()
extract.add_to_dict()
extract.draw_cdf()