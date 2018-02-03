def pair(a):#fuctionn to find the pairs
    l=len(a)#length of list
    for i in range(0,l-2):#loop to find the pairs
        for j in range(i+1,l-1):
            for k in range(j+1,l):
                if a[i]+a[j]+a[k]==0:
                    print("[(%d,%d,%d)]"%(a[i],a[j],a[k]))
A=[-6,3,10,-4,2]
pair(A)

