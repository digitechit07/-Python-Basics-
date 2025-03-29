my_list = [10,20,30,40,50,30,30,30]

unique_list= list(set(my_list))     # we remove the duplication and convert backt in to the list
print("unique list",unique_list)

sorted_list = sorted(unique_list)
print("sorted_list",sorted_list)
print(type(sorted_list))
print(id(sorted_list))
