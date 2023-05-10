#print(range(1, 5))
#print(list(range(1, 5,)))
squares=[]
for value in range(0, 20,2):
    #print(value)
    square=value+5
    squares.append(square)
    #print(value)

'''numbers=[2,4,6,8,10]
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))
print(numbers[1:4])'''

print(squares)

values = [value + 5 for value in range(0, 20, 2)]
print(values)