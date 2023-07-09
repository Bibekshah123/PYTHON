a,b,c,d,e=9,8,12,33,5
sum=a+b+c+d+e
mean=sum/5
f=(a-mean)**2
s=(b-mean)**2
t=(c-mean)**2
p=(d-mean)**2
n=(e-mean)**2
add=f+s+t+p+n
variance=add/5
Sd=variance**0.5
print(f"The sum, average and population standard deviation are {sum}, {mean} and {Sd}, respectively.")