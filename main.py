# Given the list, use loop to sum up the total sum of the list

my_list = [1,2,3,4,5,6,7,8,9,10]
total = 0

for list_sum in my_list:
  total = list_sum + total
print(total)

#possible mistakes 
# - doing a print statement inside the for loop
# - may not create a variable outside the loop
