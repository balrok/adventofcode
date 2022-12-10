import md5
c=0
n=""
m=[c]*16
while 0 in m:
 h=md5.new("ugkcyxxp%d"%c).hexdigest();c+=1
 if h[:5]=="0"*5:
	n+=h[5];q=int(h[5],16)
	if m[q]<1:m[q]=h[6]
print n[:8],"\n","".join(m)[:8]
