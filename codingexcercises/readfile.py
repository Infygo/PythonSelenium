# open_file = open('file1.txt', 'r')
# read_lines = open_file.readlines()
# for i in read_lines:
#     print(i)
# open_file.close()
with open('file1.txt', 'r') as reader:
    print(reader.read())

# count # of lines in the file
with open('file1.txt', 'r') as reader2:
    list_lines = reader2.readlines()
    print('Total number of lines:', len(list_lines))
