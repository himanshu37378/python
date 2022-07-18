a = int(input("enter the submissions for problem a"))
b = int(input("enter the submissions for problem b"))
c = int(input("enter the submissions for problem c"))

if( c < a and c < b):
    print("alice")
elif( a < b and a < c):
    print("No one wins")
elif( b < a and b < c):
    print("bob")
elif( b == c ):
    print("draw")
