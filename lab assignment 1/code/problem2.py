def short(x):#define function to find shortest word
    list=[]#empty list
    y=x.split()#spitiing words in string
    for i in y:#for to add string words in the list
        list.append(i)#using append function
    z=sorted(list,key=len)#sorting the list inascending order of length
    print("shortest :",z[0])#printing first element
def long(x):#fuction to define longest word
    list = []
    y = x.split()
    for i in y:
        list.append(i)
    z = sorted(list, key=len)
    print("longest :",z[-1])#print last element in the list
def middle(x):#function to define middle element
    list = []
    y = x.split()
    for i in y:
        list.append(i)
    a=len(list)#taking length in to integer
    if a%2==1:#for odd length
        l=(a-1)/2
        g=int(l)
        print("middle ;",list[g])
    else:#for even
        m=a/2
        n=(a-2)/2
        h=int(m)
        j=int(n)
        print("middle ",list[j],list[h])
def reverse(x):#to reverse the string
    rev=""
    y=x.split()
    for i in y:
        i=i[::-1]#to reverse each element
        rev=rev+i+" "
    print("reverse :",rev)

b=input("enter the words : ")#to enter input
short(b)#calling functions
long(b)
middle(b)
reverse(b)

