sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = '' #empty variable
for s in sounds: #goes thru list sounds
    result = result + s #add item from list to result
    result = result.upper() #chamge the chars om result to upper case
print(result)