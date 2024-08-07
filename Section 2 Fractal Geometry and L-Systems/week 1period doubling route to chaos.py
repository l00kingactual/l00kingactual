def logistic(x,r):
   return r*x*(1 - x)


def fastForward(x,r):
    for i in range(100000):
        x = logistic(x,r)
        return x
def findCycle(x,r):
   items = [x]
   current = logistic(x,r)
   period = 1
   while current != x:
       items.append(current)
       current = logistic(current,r)
   return items


rates = [3.5,3.53,3.565,3.567,3.5695,3.5698,3.56993,3.56994,3.569945]
for rate in rates:
   print("rate = " + str(rate))
   x = fastForward(0.3,rate)
   items = findCycle(x,rate)
   #print("Items = " + str(items))
   print("period = " + str(len(items)))
