y='Hello, I’m Jappy-Lappy-Happy'
print(y)
x=y[::-1]
print(x)

print(x.replace( "!","").replace(",","").replace("?","").replace(" ","").replace("-","").replace("'","").replace("’",""))


#'replace' works one at a time on each charater : notice it doesnt work with this array
rem= "!",",","?"," ","-","'","’"
print(x.replace(rem,""))