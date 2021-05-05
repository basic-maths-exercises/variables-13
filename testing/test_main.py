try:
    import AutoFeedback.plotchecks as pc
    from AutoFeedback.plotclass import line
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.plotchecks as pc
    from AutoFeedback.plotclass import line

import unittest
from main import *

xvals = np.linspace(0,19,20), 
line1 = line(xvals,(0.5)**xvals)

axislabels=["Index", "Geometric series"]

class UnitTests(unittest.TestCase) :
    def test_fib(self) :
       assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )    
