item=['fan','can','book','radio','socket','plug','cable','biro','shirt']
#length of the list
print(item)
print(len(item))

#indexing
print(item[2::4])

#adding to the list
item.append('clock')
print(item)

#replace
item[4]='blanket'
print(item)

#remove from list
item.remove('shirt')
print(item)

air=item[0],item[5]
sub= list(set(item) - set(air))
print(sub)

#sorting a list
sub.sort(reverse=False)



