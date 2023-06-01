
nums = input("Gimme a numbers to find maximum among them, separated by ',': ")
nums_list = nums.split(',')

for j in range(len(nums_list)):
    nums_list[j] = int(nums_list[j])
#print(nums_list)

max_num = nums_list[0]
for num in nums_list:
    if num > max_num:
        max_num = num
    
print(f"The maximum number among {nums_list} is {max_num}!!")
