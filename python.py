'''import keyword
print(keyword.kwlist)

a=None
print(a )

a=0
print(type(a))
print(bool(a))

print(bool([1.0]))
print(bool([0]))
print(bool([0.0]))


a=3j+5
print(a)


a=6j
print(a)

list
a=[1,2,3,4,5,True,'Hello']
print(a)

a.append(6)
print(a)
popped_value = a.pop()
print("The popped value is:", popped_value)
print(a)


TUPLE
a=(1,2,3,4,5,True,'Hello')
print(a)
a={'a':[10,20,30],'b':40,}
print(a)
print(a['a'][1])
print(a.get('b'))'''

'''Slicing'''
'''a='Hello'
print(a[2:4])
print(a[2:3+1+1])


a="Good Morning"
print(a[7:11])
print(a[7:10+1])   
print(a[1:5+1:2])
print(a[5::3])
print(a[-7::3])
print(a[-2:-9:-3])
print(a[10:-9:-1])


a=eval(input("Enter a number:"))
print(a,type(a))


a=int(input("Enter a number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")''' 

#Checking a length of a list is 5 or not

'''a=eval(input("Enter a list:"))
if len(a)==5:
    print("Length is 5")
else:
    print("Length is not 5")

print(ord('A'),ord('B'),ord('C'),ord('D')+ord('E')+ord('F')+ord('G')+ord('H'))

ch=input("Enter a Alphabet:")
if "A"<=ch<="Z":
    print("Uppercase")
elif "a"<=ch<="z":
    print("Lowercase")
else:
    print("Not an Alphabet")

i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1


n=int(input("Enter a number:"))
rev=0
while n>0:
    id=n%10
    n=n//10
    rev=rev*10+id
print("The reversed number is:", rev)

s=input('enter:')
out=''
for i in s:
    if"A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif"a"<=i<="z":
        out+=chr(ord(i)-32)
print("The modified string is:", out)

s=input('enter:')
rev=''

for i in s:
    rev=i+rev
    print(rev)

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('1',end=' ')
        else:
            print('@',end=' ')
    print()  