# # only unique value hi store karta hai 
# names = {"Yatin", "Rahul", "Yatin", "Amit", "Rahul"}
# print(names)


# Set indexing nahi karta

# numbers = {10, 20, 30}
# print(numbers[0])      // Errors ayenge 


# sets ka upyog duplicates value ko httane ke liye bhi kiya jata hai 
# set()

# sales = [1000, 2000, 1000, 3000, 2000, 4000]
# unique_sales = set(sales)
# print(unique_sales)


# add() — value add karna

# numbers = {10, 20, 30}
# numbers.add(40)
# print(numbers)


# remove() — value remove karna

# numbers = {10, 20, 30, 40}
# numbers.remove(30)
# print(numbers)

# remove me di gyi value agr exesist nhi krti to error aaskta hai 

# numbers = {10, 20, 30, 40}
# numbers.remove(50)  // Error
# print(numbers)  


# Set me membership checking bhi hoti hai  
# "in" ka use kr ke aur result "true" ya 'false' aata hai 

# numbers = {10, 20, 30, 40}
# print( 20 in numbers) 


# Set Operations - Unions , intersections 

java_students = {"Yatin", "Rahul", "Amit", "Vijay"}
python_students = {"Yatin", "Amit", "Rohit", "Neha"}

# 1. Union 

# # all_students = java_students | python_students 
# # print(all_students)

# # union() ka bhi use kr skte h aise:- 
# all_students = java_students.union(python_students)
# print(all_students)


# 2. Intersection

# common = java_students & python_students
# print(common)



