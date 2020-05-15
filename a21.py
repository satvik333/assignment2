'''Write a Python Program to implement your own myreduce() function which works exactly like
Python's built-in function reduce()'''
def myreduce(anyfunc, sequence):


    result = sequence[0]

    for item in sequence[1:]:
        result = anyfunc(result, item)

    return result



def myfilter(anyfunc, sequence):


    result = []

    for item in sequence:
        if anyfunc(item):
            result.append(item)


    return result



def sum(x,y): return x + y


def ispositive(x):
    if (x <= 0): 
        return False 
    else: 
        return True


print ("Sum on list [1,2,3] using custom reduce function "   + str(myreduce(sum, [1,2,3])) )
print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))