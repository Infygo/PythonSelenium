# reading the contents in a file
# open , read, readline
# readlines > returns list of strings > loop it up
# write to a file in a reversed fashion
# inbuilt method reversed to reverse a list


file = open('test.txt', 'r')
# print(file.read(6)) #apple
# print(file.readline()) #banana
# print(file.readline()) #cat

# reading line by line using readline and while loop
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# using readlines inbuilt method
lines_list = file.readlines()  # returns a list of strings
print(lines_list)
for i in lines_list:
    print(i.strip())
file.close()

# read and write using reader and writer > keyword with > no need of file.close
with open('test.txt', 'r') as reader:
    content = reader.readlines() # returns all lines in the file
    reversed_content = reversed(content) # reverse the list
    print(content)
with open('test.txt', 'w') as writer:
    for line in reversed_content:
        writer.write(line)
