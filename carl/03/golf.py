m=[int(s)for s in open("input.txt").read().split()]
s='sum([x+y>z and x+z>y and z+y>x for '
exec'print %sx,y,z in zip(m[::3],m[1::3],m[2::3])]),"\\n",%si in 0,1,2 for x,y,z in zip(m[i::9],m[3+i::9],m[6+i::9])])'%(s,s)
