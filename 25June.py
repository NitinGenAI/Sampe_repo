#count number of vowel in a sting
# str = 'Hello world'
# count =0
# for i in str :
#     if i=='a' or i== 'e' or i== 'o' or i=='u' or i== 'i' :
#         count = count + 1
# print(count)

# str = input("Enter the string :")
# count = 0
# for i in str :
#     if i in 'aeiou':
#        count = count + 1
# print(count)



# count number of unique vowel and consonant in a string

# str = 'Growingseed'
# unique = set(str)
# print(unique)
# vowel_count = 0
# vowel_consonant = 0
# for i in unique :
#      if i in 'aeiou' :
#          vowel_count = vowel_count + 1
#      else :
#          vowel_consonant = vowel_consonant +1
# print("Vowel :" ,vowel_count)
# print("Consonant :",vowel_consonant )

# verify that lists is in ascending order or not
# lst = [3, 22, 7, 9, 11]
# for i in range(len(lst)-1):
#
#     if lst[i] < lst[i+1]:
#         continue
#     else:
#         print("False")
#         break
#
# else:
#     print("Ascending")

# Print the maximum number from the lsit
# lst =[7, 8, 10, 23, 1, 56, 3, 5, 888]
# max = lst[0]
# for i in lst :
#     if i > max:
#         max = i
# print('max', max)


# i=0
# while i <=20:
#     if i % 2 ==0:
#     print("even" , i)
#     i = i + 1


# sum = 0
# number = 1
# while number <=20:
#
#     if number > 0:
#         total = sum + number
# print("The sum of the numbers is", total)


# for i in range(1, 6):
#     for j in range(5, i - 1):
#         print('5', end=' ')
#     print('')

# number = int(input("enter the number"))
# number =0
# while True:
#     if number/1 == 1 and number/number == 1  and number/2 !0:
#         print("Prime")
#         break
#     number = number + 1

l9 =[24,65,98,12,31,[9,8,7,6,[ 98,56,43]],1,2,3,4]
print(l9[5][4][1])

