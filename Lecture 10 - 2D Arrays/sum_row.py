a = [[5, 9, 2], [-3, 0, 8]]

r = len(a)  # 2
c = len(a[0])  # 3

for i in range(len(a)):
    row = a[i]
    # print(row)
    # Compute the sum of each row
    # row = list
    s = 0
    for x in row:
        s += x
    print(s)

    # print(sum(row))


# l = [2, 5, 7, 8, 1]
# # Sum of l
# s = 0
# for x in l:
#     s += x

# print(s)
