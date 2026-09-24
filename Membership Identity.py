print("Marks obtaines in all subjects")

Mark1 = int(input())
Mark2 = int(input())
Mark3 = int(input())
Mark4 = int(input())
Mark5 = int(input())

total = Mark1 + Mark2 + Mark3 + Mark4 + Mark5
avg = total/5

valid_range =range(1,101)

if avg not in valid_range :
    print("Invalid Range")

elif avg in range(91,101):
    print(" Your score is A1")


elif avg in range(81,91):
    print(" Your score is A2 ")


elif avg in range(71,81):
    print(" Your score is B1")


elif avg in range(61,71):
    print(" Your score is B2")


elif avg in range(51,61):
    print(" Your score is C1")


elif avg in range(41,51):
    print(" Your score is C2 ")


elif avg in range(31,41):
    print(" Your score is D1")


elif avg in range(21,31):
    print(" Your score is D2")

elif avg in range(1,21):
    print("Your score is F")
