"""boolean logic"""
print(True and True)
 #true
print(False and True)
 #false
print(1 == 1 and 2 == 2)
 #true
print("test" == "test")
 #true
print(1 == 1 or 2 != 1)
 #true
print(True and 1 == 1)
 #true
print(False and 0 != 0)
 #false
print("test" == "testing")
#False
print(1 !=0 and 2 == 1)
 #false
print("test" != "testing")
#True
print("test" == 1)
 #false
print(not(True and False))
#true
print(not(1 == 1 and 0 != 1))
#false
print(not(10 == 1 or 1000 == 1000))
#false
print(not(1 != 10 or 3 == 4))
#False
print(not("testing" == "testing" and "zed" == "cool guy"))
#true
print(1 ==1 and (not("testing" == 1 or 1 == 0)))
#true
print("chunky" == "bacon" and not(3 == 4 or 3 == 3))
#false
print(3 == 3 and (not("testing" == "testing" or "pythong" == "fun")))
#false
