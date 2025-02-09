cel=[10,15,20,25,30,35,40]

#create list fah that contains temp in fah for the corresponding elements in cel,create list cel contains temp in celcius for the corresponding elements in fah


fah=[x*1.8+32 for x  in cel]

fah=[100,101,102,103,104,105]

cel = [ (x-32)/1.8  for x in fah  ] 

print(fah)
print(cel)


