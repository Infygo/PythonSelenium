# Exception > raise Exception keyword
# try , except mechanism
# finally keyword > executes even if exception occurs / test fails / test passes as well > use of cleaning up data / resources etc

ItemsInCart = 0
# 2 items expected to be added in cart and hence result expected is 2
if ItemsInCart != 2:
    #raise Exception('ItemsInCart count doesnt match')
    pass

assert ItemsInCart == 0

# try except block
try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)
finally:
    print('clearing cookies/data/resources')



