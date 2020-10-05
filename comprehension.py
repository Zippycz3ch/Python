#list = ["Elie","Tim","Matt"]
#answer2 = [char.lower()[::-1] for char in list]
#print(answer2)

#num_list = [num for num in range(1,101) if num% 12 == 0]
#print(num_list)

abc = "amazing"
answer = [char for char in abc if char not in["a","e","i","o","u"]]
print(answer)