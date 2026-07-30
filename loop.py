#sum of square of even digits 

# num=83497
# add=0
# while num>0:
#     last=num%10
#     if last%2==0:
#         add+=(last**2)
#     num=num//10
# print(add)
    
        

#print sum of even digits and product of odd digits 
# num=int(input('enter no.: '))
# add=0
# prod=1

# while num>0:
#     last=num%10
#     if last %2==0:
#         add+=last
#     else:
#         prod*=last
#     num=num//10
# print(add)
# print(prod)

#count total digits

# num=int(input('enter no.: '))
# count=0
# while num>0:
#     count+=1
#     num//=10
# print(count)

#count no of zeros
# num=int(input('enter no.: '))
# count=0
# while num>0:
#     if num%10==0:
#         count+=1
#     num//=10
# print(count)


#count total no of odd digits 
# num=int(input('enter no.: '))
# count=0
# while num>0:
#     if (num%10)%2!=0:
#         count+=1
#     num//=10
# print(count)

# check for palindrom

# num=int(input('enter no.: '))
# rev=0
# temp=num
# while temp>0:
#     last=temp%10
#     rev=rev*10+last
#     temp//=10
# if rev==num:
#     print('palindrome')
# else:
#     print('not')


# find factor of number

# num=int(input('enter no.: '))
# i=1
# count=0
# while i<=num:
#     if num%i==0:
#         count+=1
#         print(i)
#     i+=1
# print('total factors are',count)


#prime no.

# num=int(input('enter no.: '))
# i=1
# count=0
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print('prime no.')



#armstrong no.

# temp=num=int(input('enter no.: '))
# check=0
# while temp>0:
#     last=temp%10
#     check+=last**3
#     temp//=10
# if check==num:
#     print('armstrong no.')

#disarium no.
#135
# temp=num=int(input('enter no.: '))
# check=0
# power=len(str(num))
# while temp>0:
#     last=temp%10
#     check=check+(last**power)
#     power-=1
#     temp//=10
# if check==num:
#     print('number is disarium')
# else:
#     print('not')


#perfect no or not

# num=int(input('enter no: '))
# check=0
# i=1
# while num>i:
#     if num%i==0:
#         check=check+i
#     i+=1
# if check==num:
#     print('perfect no.')
# else:
#     print('not')


#xylem and pheloem no
# 6
# num=int(input('enter no:'))
# check=0
# length=len(str(num))
# mean=0
# first=num//(10**(length-1))
# last=num%10
# while num>0:    
#     num=num//10
#     if num%10!=first and num%10!=last:
#         mean+=num%10
# if first+last==mean:
#     print('xylem') 
# else:
#     print('pheloem')

# alternative

# num=43256
# extreme=num%10 #last
# num//=10 #remove last 
# mean=0
# while num>9:
#     mean+=num%10
#     num//=10
# extreme+=num
# if extreme==mean:
#     print('xylem') 
# else:
#     print('pheloem')




#spy number

# num=int(input('enter no: '))
# prod=1
# add=0
# while num>0:
#     n=num%10
#     add+=n
#     prod*=n
#     num//=10
# if prod==add:
#     print('spy no.')
# else:
#     print('not')

# strong no

# num=145
# check=0
# for i in str(num):
#     i=int(i)
#     fact=1
#     for j in range(1,i+1):
#         fact*=j
#     check+=fact

# neon no

# num=9
# check=0
# for i in str(num**2):
#     i=int(i)
#     check+=i
# print(check)

