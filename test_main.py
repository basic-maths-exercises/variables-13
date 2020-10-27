import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_xvalues(self) :
       fighand=plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       self.assertTrue( len(this_x)==20, "You appear to have plotted the wrong number of coordinates.  You should have plotted 20" )
       for i in range( len(this_x) ) :
           self.assertTrue( np.abs(i-this_x[i])<1e-7, "One or more of the x values in your graph are not correct" )
           
   def test_yvalues(self) :
       fighand=plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       self.assertTrue( len(this_y)==20, "You appear to have plotted the wrong number of coordinates.  You should have plotted 20" )
       for i in range( len(this_y) ) :
           self.assertTrue( np.abs((1/2)**i-this_y[i])<1e-7, "One or more of the y values in your graph are not correct" )  
