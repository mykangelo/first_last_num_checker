


#create a function that identify if the first number of a set is equal to the last number 
def check_first_last_num(set):

    first_num = set[0]
    last_num = set[-1]

    if first_num == last_num:
        return True
    else:
        return False
    

#store and set the list of number sets     
first_set = [10, 20, 30, 40, 10]
second_set = [75, 65, 35, 75, 30]

#print the given list with the first set and call the function with first set 
print("Given list: ", first_set)
result = check_first_last_num(first_set)
print("result is", result)

#print the given list with the second set and call the function with second set
print("Given list: ", second_set)
result = check_first_last_num(second_set)
print("result is", result)





