contact=[{"name":"jawad","number":"9966554000","email":"syed@mail.umkc.edu"},{"name":"saad","number":"9998866550","email":"saad@mail.umkc.edu"}]
x=""#taking dictionaries inside the list
while x!="exit":#implementing while loop to meet reqirements,exit to exit
  a=input("enter the contact name or number you want to access : ")#display contact by name or number
  if a==contact[0]["name"] or a==contact[0]["number"]:
    print(contact[0])
  elif a==contact[1]["name"] or a==contact[1]["number"]:
    print(contact[1])
  else:
    print("Sorry cannot match details entered ")
  b = input("do yo want to edit any contact : yes or no ")#edit contact
  if b == "yes":
    c = input("enter the name of contact you want to edit : ")
    if c == contact[0]["name"]:
      e = input("you can edit 'name','number','email'.type and enter anyone of thoose options : ")
      if e=="name" or e=="number" or e=="email":
        d = input("enter the new detail: ")
        contact[0][e] = d
        print("the updated contact is ",contact[0])
      else:
        print("enter the valid detail to edit")
    elif c == contact[1]["name"]:
      e = input("you can edit 'name','number','email'.type and enter anyone of thoose options : ")
      if e=="name" or e=="number" or e=="email":
        d = input("enter the new detail: ")
        contact[0][e] = d
        print("the updated contact is ", contact[1])
      else:
        print("enter the valid detail to edit")
    else:
      print("the name cannot be found")
  elif b == "no":
    print("...........")
  else:
    print("enter the valid option or enter 'exit' to go back to main menu")
  print("the updated contact list is",contact)
  x=input("press 'exit' to close or any button to continue : ")