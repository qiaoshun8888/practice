AI Project
==========

HOW TO RUN
----------
run the directory/folder like:

python aiproject 

or run the __ main __ .py in the folder

please make sure using python 2.x



DESCRIPTION
-----------
'models.py' contains Class 'Game', 'State'. 
'Views.py' is controller of UI, using TKinter.
'ab.py' is the alpha beta algorithm.

The cut off function is defined in ab.py.
It does:
  1. Test the game whether it is terminal
  2. Test the time is up

The evaluation function is defined in Game Class.
And the utility of State instance get from the evalutaion function.
It does:
 * If there are 4 x in a row: return inf
 * else if there are 4 o in a row: return -inf
 * else: return 3 * C3(x) + 1 * C2(x) -  3 * C3(o) + 1 * C2(o)



