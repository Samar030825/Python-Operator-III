print("Identity Operators")

x = 5
if(type(x) is int):
    print("True")
else:
    print("False")

x = 5.5
if(type(x) is not float ):
    print("True")
else:
    print("False")

x = 20
y = 20
if( x is y ):
    print("They have the same identity")
else:
    print("They have different identity")

y = 30
if(y is not x):
    print(" x & y have differnt value")