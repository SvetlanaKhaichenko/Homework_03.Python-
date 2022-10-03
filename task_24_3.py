a = [1.02, 1.23, 3.1, 5, 10.11]

res_a= []
for i in a:
    i = str(i)
    if i.find('.')!=-1:
        j=i.find('.')
        res_a.append('0'+i[j:])
res_b =[]

for j in res_a:
    res_b.append(float(j))
print(res_b)
res_b.sort()
print(res_b)
print (round((res_b[-1]-res_b[0]), 3))