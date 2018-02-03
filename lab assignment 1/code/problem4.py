cstudents=[]#empty list to fill common students
nstudents=[]#empty list to fill un common students
def common(a,b):#define fuction to find common students
    l=len(a)
    m=len(b)
    for i in range(0,l):#nested for loop to append common students in cstudents
        for j in range(0,m):
            if a[i]==b[j]:
                cstudents.append(a[i])
def not_common(a,b):
    for i in a:#nested for loop to append uncommon elements in to nstudents
        if i not in b:
                nstudents.append(i)


python=["ram","sham","jam"]
web_application=["sham","ram","rahim"]
common(python,web_application)#calling fuction to find common elements
print("common students :",cstudents)#printing common
not_common(python,cstudents)#calling function to find uncommon in python and cstudents
not_common(web_application,cstudents)#calling fuctiion to find uncommon elements in web_application and cstudents
print("uncommon students :",nstudents)#printing uncommon