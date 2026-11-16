movies = []
movie1 = input("Enter Your Favourite Movies Name: ")
movie2 = input("Enter Your Favourite Movies Name: ")
movie3 = input("Enter Your Favourite Movies Name: ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)


# Check Palindrom yes or not.... Palindrom means starting and ending side word is same like "RaceCar" or "Maam"
list1 =[1,2,1]
list2 =[1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if( copy_list1 == list1 ):
    print("The list 1 is Palandrom")
else:
    print("The list 1 is not Palandrom")

# Tuple Count  Practine 
grade = ("A","B","C","A","D","A")
print(grade.count("A"))
# Sort in List
grade = ["A","B","C","A","D","A"]
grade.sort()
print(grade)