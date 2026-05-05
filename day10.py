# # Write a program which will print sum of all the keys whose values are 
# the factor of 12

# dt = {1:2, 2:3, 3:4, 6:12, 17:18, 18:12}
# total = 0
# for keys,values in dt.items():
#     if 12 % values == 0:
#         total += keys
# print(total)  




# dt = {1:2, 2:3, 3:4, 6:12, 17:18, 18:12}
# # dt[2]
# print(dt.get(2))  



# dt = {1:2, 2:3, 3:4, 6:12, 17:18, 18:12}
# del dt[3]       # this line will remove the key 3 and  does not return anything
# print(dt.pop(6))    # this line will remove the key 6 and return its value
# print(dt)   



# dt = {1:2, 2:3, 3:4, 6:12, 17:18, 18:12}
# x=dt.popitem()
# print(x)
# print(dt)



# dt = {1:2, 2:3, 3:4, 6:12, 17:18, 18:12}
# dt[6] = "Hello"
# print(dt)



# subjects = {}.fromkeys(["Maths", "Physics", "Chemistry"], 0)
# print(subjects)


# squares = {2:4, 3:9, 4:16, 5:25}
# print(squares)
# s = squares        # Shallow copy
# s[2]=6
# print(s)



