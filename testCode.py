# test
# a = "hellow"
#
# print()

# if 문 연습
test = 3


# if test > 3:
#     print("nope")
# elif test < 4:
#     print(test)
# else:
#     print("ddd")

# for문 연습
# for b in [1, 2, 3]:
#     print(b)
# i = 0
# while i < 5:
#     i = i + 1
#     print(i)


# function -> def 예약어

def add(a: object, b: object) -> object:
    return a + b


test1 = add(3, 7)
print(test1)

print("=" * 50)

def testfunction(aa, bb):
    print(aa//bb)
    print(aa%bb)

testfunction(14, 3)

print("=" * 50)

testStr = "Life is too short"

testlength = len(testStr)
print(testlength)
print("=" * 50)
print(testStr[0])
print("=" * 50)
print(testStr[0:3] + "===" + testStr[:])
print("=" * 50)

#date slicing

datetest = "2020-04-30 10:10"

print("Year:::"+datetest[0:4])
print("Month:::"+datetest[5:7])
print("Day:::"+datetest[8:10])
print("Hour:::"+datetest[11:13])
print("Minute:::"+datetest[14:])

print("=" * 50)

num1 = 3
str1 = "개"

num = "I eat %d %s apples" % (num1, str1)
print(num)
print("="*50)

strtest = "%10s" % "hi"
print(strtest)