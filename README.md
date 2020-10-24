# Plotting series data

Congratulations on writing code to compute the Fibonacci series.  Hopefully, you are now starting to get a real sense of just how much more powerful Python is than your calculator.  You would have had to have pressed a lot of buttons to compute those 100 numbers using your calculator!

I want to finish this exercise by showing you one final (useful) thing we can do with Python that we cannot do with a calculator.   For this exercise, we are going to consider the geometric sequence: 

![](https://render.githubusercontent.com/render/math?math=a_n=\left(\frac{1}{2}\right)^n)

The first few terms in this series are:

![](https://render.githubusercontent.com/render/math?math=a_0=\left(\frac{1}{2}\right)^0=1\qquad\a_1=\left(\frac{1}{2}\right)^1=\frac{1}{2}\qquad\a_2=\left(\frac{1}{2}\right)^2=\frac{1}{4}\qquad\a_3=\left(\frac{1}{2}\right)^3=\frac{1}{8})

I want you to proceed in a similar way to the previous exercise.  In other words, I want you to create an array.  This time your array should have only 20 elements and you should use a for loop to the elements of this array to the first 20 terms in this sequence.  The first element of the array will thus be 0, the second will be 1/2, the third 1/4 and so on. 

In addition, to this array I also want you to create a 20-element array that holds the integers from 0 up to 19.  The first element in this array should be 0 the second element should be 1 and so on. 

To complete this exercise I want you to use python to draw a graph in which the first 20 integers are on the x-axis and the terms in the geometric sequence are on the right.  

The Python commands you  use to draw a graph in which the x-coordinates of the points are in an array called `indices` and the y-coordinates are in an array called `geometric`  are:

````
plt.plot( indices, geometric, 'ko' )
plt.savefig( "geometric.png" )
````
***
These commands are making use of functionality from a Python library called matplotilb.  To use these commands you thus need to include:

````
import matplotlib.pyplot as plt
````

at the top of your python script.
