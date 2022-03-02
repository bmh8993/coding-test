# 큰 수의 

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[-1]
second = data[-2]

block_len = k + 1
first_count = (m // block_len) * k + m % block_len
second_count = m - first_count

result = first_count * first + second_count * second
