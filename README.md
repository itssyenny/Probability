# Probability
Design any random value generating function

# CODE 1
Goal : Design a random experiment function to estimate the circumference ratio π. <br />

So, here I want to use a random value generator randomize() which can return a value between [0,1]. <br />
For example, imagie that there is a circlie inscribed square with radius of 1 <br />
The area of square = 4 <br />
The area of circle = π <br />
__The ration of the (area of square)/(area of circle) = (total number of dots within square)/(total number of dots within circle) = 4/π <br />__
![Picture](http://mathcentral.uregina.ca/qq/database/qq.09.06/s/lori1.1a.gif) 
  ## FAQ
  You must be curious why the formula for the xrand and yrand in the code 1 is *2random()-1* is because : <br />
  > 2x will generate a range between 0 and 1.999. After subtracting by 1, the range will be between -1 and 0.999,in which         
  > the range that we are searching for.
