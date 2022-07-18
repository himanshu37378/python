m = int(input("Enter the minutes left in the exam"))
n = int(input("Enter the number of episodes"))
k = int(input("Enter hoe long each episode is"))\

season = n * k

if(season <= m):
    print("yes")
elif(season > m):
    print("no")
