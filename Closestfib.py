# This function takes an integer and returns the closest fibonacci number above and below the given number
import math
def closestFib(n):
    golden = 0.5 + ((5**0.5) / 2)
    nearestPlace = round(math.log(n*(5**0.5),golden))
    x1 = round(((golden**(nearestPlace)) - ((1 - golden)**(nearestPlace)))/(5**0.5))
    x2 = round(x1 * golden)
    return (x1,x2)
