import string
# input card no.
card_num = input("Enter your credit card number: ")
card_num2=""
# remove " " or "-"
for char in card_num:
    if char in string.digits:
        card_num2+=char
# add all digits in odd places from right to left
sum1=0
rev_odd_num = card_num2[::-2]
for num in rev_odd_num:
    num = int(num)
    sum1 += num
# double and add all even digits from right to left and if double > 10 then use sum of digits of double
sum2=0
rev_num = card_num2[::-1]  
rev_even_num = rev_num[1::2]
for num in rev_even_num:
    double = 2*(int(num))
    if double < 10:
        sum2+=double
    else:
        split = double//10 + double % 10
        sum2+=split
if (sum1+sum2)%10 == 0:
    print("The credit card number is valid")
else:
    print("The credit card number is invalid")