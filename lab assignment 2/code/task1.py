import sys #importing sys
max=sys.maxsize
lib={"python":10,"java":20,".net":30,"c":40}#dictionary taken
a=int(input("enter the upper range : "))
b=int(input("enter the lower range : "))
#using simple if else statement to achieve output
if a<0 or b<0:
  print("we dont accept negitive price range")
elif a<=10 and b>=0:
  if a<10 and b>=0:
    print("we do not have anything for you in this price range")
  else:
    print("you can purchase (%s)"%list(lib.keys())[0])
elif a<=20 and b>=0:
  if a<=20 and b>=10:
    if a<=20 and b>10:
      if a<20 and b>10:
        print("we do not have anything for you in this price range")
      else:
        print("you can purchase (%s)"%list(lib.keys())[1])
    elif a<20 and b>=10:
        print("you can purchase (%s)"%list(lib.keys())[0])
    else:
      print("you can purchase (%s,%s)"%(list(lib.keys())[0],list(lib.keys())[1]))
  elif a<20 and b>=0:
    print("you can purchase (%s)"%(list(lib.keys())[0]))
  else:
    print("you can purchase (%s,%s)" % (list(lib.keys())[0], list(lib.keys())[1]))
elif a<=30 and b>=0:
  if a<=30 and b>=10:
    if a<=30 and b>10:
      if a<=30 and b>=20:
        if a<=30 and b>20:
          if a<30 and b>20:
            print("we do not have anything for you in this price range")
          else:
            print("you can purchase (%s)"%(list(lib.keys())[2]))
        elif a<30 and b>=20:
          print("you can purchase (%s)"%(list(lib.keys())[1]))
        else:
          print("you can purchase (%s,%s)"%(list(lib.keys())[1],list(lib.keys())[2]))
      else:
        print("you can purchase (%s,%s)"%(list(lib.keys())[1],list(lib.keys())[2]))
    else:
      print("you can purchase (%s,%s,%s)"%(list(lib.keys())[0],list(lib.keys())[1],list(lib.keys())[2]))
  elif a<30 and b>=0:
    print("you can purchase (%s,%s)" % (list(lib.keys())[0], list(lib.keys())[1]))
  else:
    print("you can purchase (%s,%s,%s)"%(list(lib.keys())[0],list(lib.keys())[1],list(lib.keys())[2]))
elif a<=max and b>=0:
  if a<=max and b>=10:
    if a<=max and b>10:
      if a<=max and b>=20:
        if a<=max and b>20:
          if a<=max and b>=30:
            if a<=max and b>30:
              if a<40 and b>30:
                print("we do not have anything for you in this price range")
              else:
                print("you can purchase (%s)"%(list(lib.keys())[3]))
            elif a<40 and b>=30:
              print("you can purchase (%s)"%(list(lib.keys())[2]))
            else:
              print("you can purchase (%s,%s)"%(list(lib.keys())[2],list(lib.keys())[3]))
          else:
            print("you can purchase (%s,%s)"%(list(lib.keys())[2],list(lib.keys())[3]))
        else:
          print("you can purchase (%s,%s,%s)"%(list(lib.keys())[1],list(lib.keys())[2],list(lib.keys())[3]))
      else:
        print("you can purchase (%s,%s,%s)"%(list(lib.keys())[1],list(lib.keys())[2],list(lib.keys())[3]))
    else:
      print("you can purchase (%s,%s,%s,%s)"%(list(lib.keys())[0],list(lib.keys())[1],list(lib.keys())[2],list(lib.keys())[3]))
  elif a<40 and b>=0:
    print("you can purchase (%s,%s,%s)"%(list(lib.keys())[0],list(lib.keys())[1],list(lib.keys())[2]))
  else:
    print("you can purchase (%s,%s,%s,%s)"%(list(lib.keys())[0],list(lib.keys())[1],list(lib.keys())[2],list(lib.keys())[3]))
else:
  print("we do not have anything for you in this price range")
