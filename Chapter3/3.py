#第三章的练习

#3-1
names = ['小波', '二蛋', '老朱', '老贱']
print(names[0])
print(names[1])
print(names[-2])
print(names[-1])

#3-2
print(names[0].title() + ' ,你好！')
print(names[2].title() + ' ,过年好！')

#3-3
vehicles = ['bus', 'bike', 'train', 'car', 'plane']
print(vehicles[1] + ' is very environment')
print(vehicles[-1] + ' is very safe')

#3-4
names = ['小波', '二蛋', '老朱', '老贱']
print('我想邀请' + names[0] + names[1] + names[2] + names[3] + '喝酒')

#3-5
print(names[-1] + ' 不能来喝酒')
names[-1] = '阿肥'
print('我想邀请' + names[0] + names[1] + names[2] + names[3] + '喝酒')

#3-6
print('我还可以邀请更多的人！')
names.insert(0, '小米')
names.insert(2, '小明')
names.append('小青')
print('我想邀请' + names[0] + names[1] + names[2] + names[3]+ names[4]+ names[5]+ names[6] + '喝酒')

#3-7
print('我只能邀请二人')
print('对不起，' + names.pop() +'你不能参加聚餐')
print('对不起，' + names.pop() +'你不能参加聚餐')
print('对不起，' + names.pop() +'你不能参加聚餐')
print('对不起，' + names.pop() +'你不能参加聚餐')
print('对不起，' + names.pop() +'你不能参加聚餐')
 
print(names[0] + '还能参加聚会')
print(names[1] + '还能参加聚会')

del names[0]
del names[-1]

print(names)

#3-8
places = ['sanya', 'xizang', 'taiguo', 'feizhou', 'dali']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse = True))

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

print(len(places))