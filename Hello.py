first_name="W"
last_name="q"
full_name=first_name+" "+last_name
print(full_name)

print("Hello, "+full_name.title()+"!")

print("languages:\nPythone\nC+")
# \n 换行符 \t 制表符
full_name = ' wq '
full_name.rstrip()
full_name.lstrip()
full_name.strip()
#暂时删除空格 strip   r右 l左
#str() 非字符串转化为字符串
age=23
message="Hell "+str(age)+"!"
print(message)

abd=['a','b','c']
print(abd)
print(abd[0])

#列表[]   索引从0开始

print(abd[-1])
#-1为倒数第一
#append 添加元素 列表末尾
ab=['a','b','c']
ab.append('d')
print(ab)

#insert（位置,'yuansu '）  del 列表[位置]

ab=['a','b','c']
ab.insert(0,'d')
del ab[-1]
print(ab)
last_ab=ab.pop()
print(last_ab)
print(ab)
#pop(位置) 默认最后一元素，pop弹出元素输出，不保留在列表

# 列表.remove(' ')  删除列表元素 但还处于被删除列表中

car=['a','c','b']
car.sort()
print(car)
#sort() 列表按顺序排列
#sort(reverse=Ture) 反转排序
#sorted() 临时排序

ab=['a','b','c']
len(ab)
#len 可得到列表长度 在py中运行

magicians=['a','b','c']
for magician in magicians:
    print(magician)
    print('1'+magician.title())
print("Thank you")
#for 循环  :冒号  for后面2行缩进的会重复运行，一般加个end

# rang(1,2) range是从指定的第一个数开始到第二个数结束 不包含第二个值
for value in range(1,5):
    print(value)
#list(range(1,5)) list将range的结果转化为列表
numbers=list(range(1,5))
print(numbers)

squares=[]
for value in range(1,6):
    square=value**2
    squares.append(square)
print(squares)

# ab=[]
# min(ab)  #列表最小值
# max(ab)  #最大值
# sum(ab)  #总和

ab=[value**2 for value in range(1,6)]
print((ab))


abs=['a','b','c','d']
print(abs[0:2])   #索引元素0-2
print(abs[:2])    #自动从开头开始
print(abs[2:])    #从2开始到最后
print(abs[-3:])   #最后3个

for ab in abs[:3]:
    print(ab.title())

abs=(200,50)
for ab in abs:
    print(ab)
#元组不能修改，可以重新定义
abs=(100,50)
for ab in abs:
    print(ab)


cars=['a','b','c','d']
for car in cars:
    if car=='a':
        print(car.upper())
    else:
        print(car)
# =值 ==检查是否为该值
# upper大写 lower小写  不会修改变量中的值

car='abc'
if car !='ab':
    print("Hold on")
# != 感叹号表示不等

banned_users=['ab','abc','ef']
user='abcdef'

if user not in banned_users:
    print(user.title()+", Hello")
# <=  >=

age=17
if age>=18:
    print('1')
else:
    print('No!')
# if  else

age=17
if age<12:
    print("to 12")
elif age<18:
    print("To 18")
else:
    print("Go")
# if  elif elif  else  依次运行，通过一个跳过其他  依次运行用if

abs=['ab','cd','ef']
cds=['ab','abc','abcd']
for cd in cds:
    if cd in abs:
        print("adding "+cd)
    else:
        print("Sorry to "+cd)

#字典 {} 键和值成对出现
a_0={'color':'green','points':5}
print(a_0['color'])
print(a_0['points'])
new_points=a_0['points']
print("You to "+str(new_points))

a_1={}
a_1['color']='red'
a_1['points']='6'
print(a_1)
a_1['color']='green'
print(a_1)

del a_1['points']
print(a_1)
#del语句是永久删除

love_languages={
    'a':'pythonn',
    'b':'jave',
    'c':'c+',
}
print("a is like "+
      love_languages['a'].title())

for k,v in love_languages.items():
    print("\nKey:"+k)
    print("Value:"+v)

#set() 删除重复项
favorite_languages={
    'a':'python',
    'b':'jave',
    'c':'c+',
    'd':'python',
}
print("The languages:")
for language in set(favorite_languages.values()):
    print(language.title())

#waixingren
aliens=[]
for alien_number in range(0,30):
    new_alien={'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']='5'
        alien['speed']='medium'

for alien in aliens[0:5]:
    print(alien)
print("...")

