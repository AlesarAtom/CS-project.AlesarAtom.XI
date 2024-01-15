list1=[1,5,9,3,7,6,3,23]
prime=[]
for i in list1:
    f=0
    for k in range(1,i):
        if i%k==0:
            f+=1
    if f==1:
        prime.append(i)
print(prime)
list2=prime
res = {key: list1.count(key) for key in list2}
print("Lists elements Frequency : " +str(res))

