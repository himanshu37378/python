tag = input("Enter the tag you want to check")
first = tag.find("<")
second = tag.find("/")
last = tag.find(">")
length = len(tag)
if(first == 0 and second == 1 and last + 1 == length):
    print("this is a correct html tag")
else:
    print("this is not a correct html tag")


