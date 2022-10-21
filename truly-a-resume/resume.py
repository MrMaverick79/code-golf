#Print out my resume, including the image
import sys
a,b,c,d,e=",",".","\n","%","&"
print(a*14+b*15+a*31+c+a*15+b*12+a*33+c+a*14+b*11+d*2+e*7+d*2+a*24+c)
#line 3
for f in sys.argv[1:]:
    g=open(f,"r")
    print(g.read())