k = 23
m = 15
n = 17
tot = k+m+n

kk = (k/tot)*((k-1)/(tot-1))
km = 2*(k/tot)*((m)/(tot-1))
kn = 2*(k/tot)*((n)/(tot-1))
mm = 0.75*(m/tot)*((m-1)/(tot-1))
mn = (m/tot)*((n)/(tot-1))

print (kk+km+kn+mm+mn)