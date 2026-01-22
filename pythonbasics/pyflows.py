# if else condition > follow indentation

# for loop , i in list  :/ j in range :

# while loop > executes until the condition is true
# break > exits the loop abruptly > used to exit a loop after achieving certain condition
# continue > skips the current iteration and goes to the next iteration in that loop > useful to exclude specific index / iterations


# if else condition
text = 'Good Morning'
if text == 'Good Morning':
    print('condition matches')
    print('if condition matches')
else:
    print('condition doesnt match')

print('out of if else block')

# for loop ex:1
num_list = [1,2,3,4,5]
for i in num_list:
    print(i)

# sum of first 5 natural nums from a num list
sum_0 = 0
for i in num_list:
    sum_0 = sum_0 + i
    print("{}{}{}{}".format('sum of first ', i ,'elements:', sum ))

# sum of only even nums in range 20 > 0+2+4+6... > use range
sum_even_nums = 0
for j in range(1,21):
    if j % 2 != 0:
        continue
    sum_even_nums = sum_even_nums + j
    print("sum in the loop: ", sum_even_nums)
print("{}{}".format('sum of only even nums ', sum_even_nums))

# while loop > needs to print 10 , 9, 8, 7, 6,5, 4
it =10
while it > 1:
    print(it)
    if it == 9:
        it  = it - 1
        continue
    if it == 4:
        break
    it = it - 1
print(it)
print('out of while loop')

# use of break statement