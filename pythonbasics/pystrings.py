# String methods
# substrings check
# in
# split, strip , lstrip, rstrip

str1 = 'Rahulshetty@academy.com'
str2 = 'consultingfirm'
str3 = str1+str2
print(str3)
print(str1 in str3) # returns a boolean value
print(str1[:5]) # Rahul
print(str1.split('.')) # Rahulshetty@academy, com
str4 = ' great '
print(str4.strip())  # strips spaces
print(str4.lstrip())  # strips left space
print(str4.rstrip()) # strips right space

