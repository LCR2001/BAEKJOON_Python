### 입출력과 사칙연산 ###
# 입력 및 출력 (1)
A,B = input().split()
print(int(A)+int(B))
print(int(A)/int(B))

# 입력 및 출력 (2) - map함수 사용
A,B = map(int,input().split())
print(A+B,A-B,A*B,A/B,A%B,sep='\n')

# 문자열 합치기
print(input() + "??!")

# 두 세자리 정수 곱 구하기 
A = int(input()) ##첫번째 수만 정수형으로 변환
B = input()  ## 두번째 수는 문자열 형태로 저장

print(A*int(B[2])) # B가 세자리수라는 전제 하에
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))
