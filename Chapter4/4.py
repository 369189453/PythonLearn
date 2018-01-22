#第四章的练习

#4-1
pizzas = ['xiaoniu', 'daliu', 'peigen']

for pizza in pizzas:
	print('我喜欢' + pizza)
print('我确实非常喜欢披萨！')

#4-2
#省略

#4-3
for num in range(1,21):
	print(num)

#4-4
#for num in range(1,10000001):
#	print(num)

#4-5
nums = [num for num in range(1, 1000001)]
print(min(nums))
print(max(nums))
print(sum(nums))

#4-6
nums = [num for num in range(1, 21, 2)]
for num in nums:
	print(num)

#4-7
nums = [num for num in range(3, 31, 3)]
for num in nums:
	print(num)

#4-8
nums = [num**3 for num in range(3, 11)]
for num in nums:
	print(num)

#4-8
nums = [num**3 for num in range(3, 11,2)]
for num in nums:
	print(num)

#4-10
print('The first three items in the list are:')
for num in nums[:3]:
	print(num)
print('The last three items in the list are:')
for num in nums[-3 :]:
	print(num)


#4-11
nums = (1, 2, 4, 5 ,6)
nums =(1,23)