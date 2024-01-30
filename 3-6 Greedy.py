# 곱하기 혹은 더하기

# 내 풀이
# s=str(input())
# data=[]
# result=0
# for i in s:
#     data.append(int(i))
#
# for j in data:
#     if j<=1 or result<=1:
#         result+=j
#     else:
#         result*=j
#
# print(result)

# 답지
data=input()

#첫 번째 문자를 숫자로 변경하여 대입
result=int(data[0])

for i in range(1,len(data)):
    # 두 수 중에서 하나라도 '0'혹은'1'인 경우, 곱하기보다는 더하기 수행
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num
print(result)