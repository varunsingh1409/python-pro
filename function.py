# extract  all the uppercase alphabets in list from a given string 
# s='ADmin123File'
# li=[]
# for i in s:
#     if i.isupper(): 
#         li.append(i)
# print(li)

#Extract all numbers in a list from a given string 

# s='ADmin123File'
# li=[]
# for i in s:
#     if i.isupper(): 
#         li.append(i)
# print(li)

# s='ADmin123File'
# li=[]
# l1=[]
# for i in s:
#     if i.islower():
#         li.append(i)
#     if i.isupper():
#         l1.append(i)
# print(li)
# print(l1) 


# s='ADmin1!@#$23File'
# li=[]
# for i in s:
#     if not(i.isalnum()):
#         li.append(i)
# print(li)




#extract upper,lower,case,nummber,and special char in seperate lists 

# s='ADmin1!@#$23File'
# li1=[]
# li2=[]
# li3=[]
# li4=[]

# for i in s:
#     if i.isupper():
#         li1.append(i)
#     if i.islower():
#         li2.append(i)
#     if i.isdigit():
#         li3.append(i)
#     if not(i.isalnum()):
#         li4.append(i)

# print(li1,
# li2,
# li3,
# li4)


#user defined function

# def even_odd():
#     n=int(input('enter no.: '))
#     if n%2==0:
#         print('even')
#     else:
#         print('odd')
# even_odd()



# def checkpalindrome(n):
#     temp=n
#     rev=0
#     while temp>0:
#         last=temp%10
#         temp//=10
#         rev=rev*10+last
#     if rev==n:
#         print(n,'is palindrome')
#     else:
#         print(n,'is not')


# checkpalindrome(121)

# create a function to return sq of a funtion

# def sqr(a):
#     return a**2

# sq=sqr(3)
# print(sq)


# create a fucntino which returns reverse of a number

# def rev(a):
#     rev=''
#     for i in str(a):
#         rev=i+rev
#     return int(rev)
# print(rev(123))


# def even_odd(a):
#     if a%2==0:
#         return True
#     else:
#         return False
# print(even_odd(23))
# print(even_odd(22))
# print(even_odd(2))
# print(even_odd(1))


# store the factorial of number in a list

# list1=['hii',2,8.99,'bye',5,4,'pthon']

# list2=[]
# def store_fact(i):
#     fact=1
#     for i in range(1,i+1):
#         fact*=i
#     return fact

# for i in list1:
#     if type(i)==int:
#         list2.append(store_fact(i))
# print(list2)
    
    
    
# def is_prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return True
#     else:
#         return False


# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# def series_prime(n):
#     for i in range(1,n+1):
#         if is_prime(i):
#             print(i)
        
    

#series of prime number 
# n=int(input('enter range: '))
# series_prime(n)

# for i in range(1,n+1):
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#          count+=1
#         j+=1
#     if count==2:
#         print(i)


# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# def is_strong(n):
#     check=0
#     for i in str(n):
#         check+=fact(int(i))
#     # if check==n:
#     #     return True
#     # else:
#     #     return False
#     return check==n

    
# n=int(input('enter num:'))
# print(is_strong(n))


#prime of prime

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def series_prime(n):
    li=[]
    for i in range(1,n+1):
        if is_prime(i):
            li.append(i)
    return li
        

def prime_of_prime(n):
    li=series_prime(n)
    for i in li:
            check=0
            i=str(i)
            for j in i:
                check+=int(j)
            if is_prime(check):
                print(i)



n=int(input('enter range: '))
prime_of_prime(n)