# 더블더블
# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

# 주어질 숫자는 30을 넘지 않는다.

# 입 8
# 출 1 2 4 8 16 32 64 128 256

N=int(input())
re=1
for i in range(N+1):
    print(re, end=' ')
    re=re*2