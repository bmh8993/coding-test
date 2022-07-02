input = input()
alpha_list = []
num = 0

for i in input:
    if i.isalpha():
        alpha_list.append(i)
    else:
        num += int(i)

sorted_list = sorted(alpha_list)
if num != 0:
    sorted_list.append(str(num))

print("".join(sorted_list))

