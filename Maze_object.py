from random import shuffle, randrange
import numpy as np
import pickle

class Maze:


    def __init__(self, size_x=10, size_y=10, start=[0,0], end=[5,5]):

        self.size_x = size_x
        self.size_y = size_y
        try:
            if start[0] < 0 or start[0] > size_x or start[1] < 0 or start[1] > size_y:
                raise IndexError("Error start position")
            else:
                self.start = start

            if end[0] < 0 or end[0] > size_x or end[1] < 0 or end[1] > size_y:
                raise IndexError("Error end position")
            else:
                self.end = end
            self.end = end

        except Exception as e:
            print(e)


    def __str__(self):
        s = ""
        s += "Size : "+str(self.size_x)+' by '+str(self.size_y)+'\n'
        s += "Start : "+str(self.start[0])+','+str(self.start[1])+'\n'
        s += "End : "+str(self.end[0])+','+str(self.end[1])+'\n'
        return s