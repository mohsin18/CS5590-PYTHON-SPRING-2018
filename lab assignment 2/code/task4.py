import numpy as n#importing numpy as n
x = n.random.randint(0,20, size= 15)#initializing integers between 0 to 20 of size 15
print('The random vector generated is: ',x)#print the above logic
similar=n.bincount(x)#counting the frequency of words
final= n.argmax(similar)#most common integer
print('The repeating integers are: ', final)#printing