#count no of vowels 
# text='hello ,how are you?'
# vowel=0
# for i in text:
#     if i in 'aeiouAEIOU':
#         vowel+=1
# print(vowel)


#create new list having only pos no from list

# num=[-2,5,-1,0,3,-7]
# n=[]
# for i in num:
#     if i >=0:
#         n.append(i)
# print(n)


#reversing without slicing

# word='python'
# new=''
# for i in word:
#     new=i+new
# print(new)

# max from list

# num=[4,1,9,12,7]
# maxa=num[1]
# for i in num:
#     if i>maxa:
#         maxa=i
# print(maxa)

#loop through 2d list 

# mat=[[1,2],[3,4],[5,6]]
# for i in mat:
#     for j in i:
#         print(j)


#freq count of char

# word='banana'
# out={}
# for i in word:
#     out[i]=out.get(i,0)+1
# print(out)


#find users with overdue payments
# user=[{'name':'Alice','days_late':5},
#       {'name':'Bob','days_late':45},
#       {'name':'Carol','days_late':0}]
# for i in user:
#     if i.get('days_late')>30:
#         print(f"{i.get('name')}'s have overdued till {i.get('days_late')}")


#group students by grade 

# students=[{'name':'john','grade':'A'},
#           {'name':'Amy','grade':'B'},
#           {'name':'Zoe','grade':'A'},
#           {'name':'Jake','grade':'C'}]
# grouped={}
# for i in students:
#     grade=i['grade']
#     name=i['name']
#     if grade in grouped:
#         grouped[grade].append(name)
#     else:
#         grouped[grade]=[name]
# print(grouped)


#print 1 to 10

# for i in range(1,11):
#     print(i)

# print 10 to 1

# for i in range(10,0):
#     print(i)

# create a list of five by taking user input

# l=[]
# for i in range(5):
#     data=eval(input('enter element: '))
#     l.append(data)
# print(l)


# print n natural no
# n=int(input('enter no.'))
# for i in range(1,n+1):
#     print(i)

# print n natural no in reverse order

# n=int(input('enter no.'))
# for i in range(n,0,-1):
#     print(i)

#print natural no. from n to n1

# n=int(input('enter no.'))
# n1=int(input('enter no.'))
# if n<n1:
#     for i in range(n,n1+1):
#         print(i)
# else:
#     for i in range(n,n1-1,-1):
#         print(i)


# print multiplication table

# n=int(input('enter no.'))
# for i in range(1,11):
#     print(f'{n} X {i} = {n*i}')

# print n natural even no

# n=int(input('enter no.'))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)


# print n natural odd no

# n=int(input('enter no.'))
# for i in range(1,n+1):
#     if i%2!=0:
#         print(i)

# print n natural no divisible by 5

# n=int(input('enter no.'))
# for i in range(1,n+1):
#     if i%5==0:
#         print(i)


# print n natural palindrome no

# n=int(input('enter no.'))
# for i in range(1,n+1):
#     temp=i
#     rev=0
#     while temp>0:
#         last=temp%10
#         rev=rev*10+last
#         temp//=10
#     if i==rev:
#         print(i)

# n=int(input('enter no.:'))

# for i in range(1,n+1):
#     i=str(i)
#     rev=''
#     for j in i:
#         rev=j+rev
#     if i==rev:
#         print(i)

# sum of n natural no
# num=int(input('enter no.: '))
# add=0
# for i in range(1,n+1):
#     add+=i
# print(add)

# product of n natural no.

# n=int(input('enter no.: '))
# prod=1
# for i in range(1,n+1):
#     prod*=i
# print(prod)

# factorial of a number

# n=int(input('enter no.: '))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#print digit of number

# num=int(input('enter no.: '))
# for i in str(num):
#     print(i)

 

# xylem and pheloem no
# num=43256
# extreme=num%10
# num//=10 
# mean=0
# first=num//(10**(len(str(num))-1))
# extreme+=first
# for i in str(num):
#     i=int(i)
#     if i!=first:
#         mean+=i    
# if extreme==mean:
#     print('xylem')
# else:
#     print('pheloem')




# num=432
# add=0
# for i in str(num):
#     add+=int(i)
# print(add)
 
# print digit from left to right using while 

# num=123
# i=0
# power=len(str(num))
# while i<len(str(num)):
#     print(num//(10**(power-1))%10)
#     power-=1
#     i+=1

# using for loop

# num=123
# power=len(str(num))
# for i in range(len(str(num))):
#     print((num//(10**(power-1)))%10)
#     power-=1


