# 1라인 주석

'''
라인1
라인2
여러라인...
'''

a = 1
b = 2
if a>b: 
    print(str(a) + "이 " + str(b) + "보다 크다")
elif a<b:
    print(str(a) + "이 " + str(b) + "보다 크다")
else:
    print(str(a)+ " 은 " + str(b)+ "와 같다")
    
print("이것은 위의 if문과 상관없이 수행되는 구문")