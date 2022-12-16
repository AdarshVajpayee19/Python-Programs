s = set()

# print(type(s))
# s_from_list = set([1, 2, 3, 4])
# print(s_from_list)
# print(type(s_from_list))

s.add(1)
s.add(1)
s.add(2)
print(s)  # Set is used to Retain unique values
s1 = s.union({1, 2, 5})
print(s, s1)

s2 = s.intersection({1, 2, 5})
print(s, s2)
print(len(s))
print(min(s1))
print(max(s1))

s3 = {1, 4, 5, 6}
print(s.isdisjoint(s3))
s4 = {4, 5, 6}
print(s.isdisjoint(s4))

