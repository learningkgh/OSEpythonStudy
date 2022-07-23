# jump_to_pythom_5장
# Q_1 다음은 Calculator 클래스이다.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        
# 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자.
# 즉 다음과 같이 동작하는 클래스를 만들어야 한다.        

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value-= val
        
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# Q_2 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자. 
# 즉 다음과 같이 동작해야 한다.

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
    
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value) # 100 출력

# Q_3 다음 결과를 예측해 보자.
# 하나.
all([1, 2, abs(-3)-3])
# False

# 둘.
chr(ord('a')) == 'a' # ord('a') = chr(97) 
# True

# Q_4 filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
def positive(x):
    return x > 0

a = list(filter(positive, [1, -2, 3, -5, 8, -3]))
print(a)

b = list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))
print(b)

# Q_5 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
hex(234) #'0xea'
# 이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.
# ※ 내장 함수 int를 활용해 보자.
print(int(0xea))

# Q_6 map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 
# [3, 6, 9, 12]를 만들어 보자.
c = list(map(lambda x: x * 3, [1, 2, 3, 4]))
print(c)

# Q_7 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
d = [-8, 2, 7, 5, -3, 5, 0, 1]
print(min(d)+max(d))

# Q_8 17 / 3의 결과는 다음과 같다.
# 5.666666666666667
# 위와 같은 결괏값 5.666666666666667을 소숫점 4자리까지만 반올림하여 표시해 보자.
print(round(17/3, 4))

# Q_9 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트(C:\doit\myargv.py)를 작성해 보자.
import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)

# Q_10 os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
import os 
os.chdir("c:/doit")
result = os.popen("dir")
print(result.read())
