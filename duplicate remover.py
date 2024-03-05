numbers = [1,1,3,4,5,2,2,3,6,9,8,8,7,5]
new = []
for number in numbers:
    if number not in new:
        new.append(number)
print (new)