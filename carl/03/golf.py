s='map(int,open("input.txt").read().split())[i+%d*'
l=0,1,2
exec'print sum([x+y>z for i in%sfor x,y,z in map(sorted,zip(%s))]);'*2%("[0]",(s+"1::3],")*3%l,l,(s+"3::9],")*3%l)
