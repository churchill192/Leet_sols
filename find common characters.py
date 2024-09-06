list1=["abc",'bcd','bca']
set_of_letters=[]
for word in list1:
    set_of_letters.append(set(word))
print(set_of_letters)

common_letters = set.intersection(*set_of_letters)
print(list(common_letters))

