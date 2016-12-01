import string

print "micro optimize"
for i in range(1,4):
    for k in range(3,0,-1):
        if k == 1:
            print ".replace('"+str(i)+"', '1"+str(i)+"')"
        else:
            print ".replace('"+(str(i)*k)+"', '"+string.ascii_lowercase[i*4+k]+"')"

for i in range(1,4):
    for k in range(2,4):
        print ".replace('"+string.ascii_lowercase[i*4+k]+"', '"+str(k)+str(i)+"')"


print "no optimize"
for i in range(1,4):
    for k in range(3,0,-1):
        print ".replace('"+(str(i)*k)+"', '"+string.ascii_lowercase[i*4+k]+"')"

for i in range(1,4):
    for k in range(1,4):
        print ".replace('"+string.ascii_lowercase[i*4+k]+"', '"+str(k)+str(i)+"')"

