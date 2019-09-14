# posiible Words from phone digits

dig1 = int(input("Enter Digit1 : "))
dig2 = int(input("Enter Digit2 : "))
dig3 = int(input("Enter Digit3 : "))

phone = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]

for i in phone[dig1-1]:
    for j in phone[dig2-1]:
        for k in phone[dig3-1]:
            print(i,j,k)
5