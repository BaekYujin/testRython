
#정렬과 공백 :::
testStr = "%15s" % "hi"
## 전체 15개 자리에서 오른쪽정렬로 공백은 15-2 = 13공백과 뒤에 hi가 return
print(testStr)
print("=" * 50)

#소수점 4자리만 출력 -> 단, 다섯번째 자리에서 반올림됨
testfloat = "%0.4f" % 3.12344678
print(testfloat)
print("=" * 50)

#format함수
testformat = "I eat {0} apples" .format(3)
print(testformat)

num1 = 3
days1 = 4
testformat1 = "I ate {0} apples. so I was sick for {1} days" .format(num1, days1)
testformat2 = "I ate {num} apples. so I was sick for {days} days" .format(num=num1, days=days1)
print(testformat1 + ":::" + testformat2)

#정렬 및 공백 & 공백 채우기
##왼쪽정렬  :<[자리수]  ::: 공백채우기 >> :[채울문자]<[자리수]
testLeft = "{0:<10}" .format("hi")
testLeft1 = "{0:!<10}" .format("hi")
print(testLeft + " ::::: " + testLeft1)
##오른쪽정렬  :>10[자리수] ::: 공백채우기 >> :[채울문자]>[자리수]
testRight = "{0:>10}" .format("hi")
testRight1 = "{0:@>10}" .format("hi")
print(testRight + " ::::: " + testRight1)
#가운데 정렬  :^[자리수] ::: 공백채우기 >> :[채울문자]^[자리수]
testCenter = "{0:^10}" .format("hi")
testCenter1 = "{0:=^10}" .format("hi")
print(testCenter + " ::::: " + testCenter1)
print("="*50)

#f문자열 포매팅
name = "백유진"
age = 31

testF = f"나의 이름은 {name} 입니다. 나의 나이는 {age} 입니다."
print(testF)
print("="*50)

##딕셔너리 에서의 F 문자열 포매팅
sample = {'name':'백유진', 'age': 30}
testF1 = f"내 이름은 {sample['name']} 이고, 지금 나이는 {sample['age']+1} 입니다."
print(testF1)
print("="*50)
##정렬
fLeft = f'{"hi":!<10}'
fRight = f'{"hi":@>10}'
fCenter = f'{"hi":=^10}'
print(fLeft + ">>>>>" + fRight + ">>>>>>" + fCenter)
print("="*50)


#문자열 개수
# count : 특정 문자 개수
# len : 전체 개수
# find : 특정 문자가 처음 나온 위치 , 존재 하지 않으면 -1 출력
# index : find와 같이 특정 문자가 처음 나온 위치 출력, 그러나 다른점은 존재 하지 않음 오류
# join : 문자열삽입, 문자열 사이사이에 특정 문자 넣기 --> split와 비교하면서 생각함 좋겠음.. 배열을 ','로 join하고 split로 ','각각 나누면 다시 배열로 됨
# split : 문자열 나누기
# upper : 소문자를 대문자로
# lower : 대문자를 소문자로
# lstrip / rstrip : 왼쪽/오른쪽 공백 지우기
# strip : 전체 공백 지우기
# replace : 문자열 바꾸기

a = "hobby"
print(a.count('b')) #특정 문자 개수
print(len(a)) #전체 개수

b = "Python is the best choice"
print(b.find('b'))

bb = ['a', 'b', 'c']
aa = ",".join(bb)
print(aa)

aaa = aa.split(",")
print(aaa)

t = " hi "
print(t.rstrip())