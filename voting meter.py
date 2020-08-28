# print("welcome to election day")
# eligible_citizen = (18)
# non_eligible_citizen = (17)
# int ( input("enter your age: "))
# if eligible_citizen == True:
#     print('you are welcome')
# else:
#     print('oops! you are not eligible to vote')

print('welcome to election day')
user_age =int(input('enter your age'))
if user_age < 18:
    print('oops! you are not eligible to vote')
else:
    print('you are eligible to vote!')
   