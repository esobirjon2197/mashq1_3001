# 1-m
numbers = [10, 20, 30, 40, 50]
print(numbers)

print(len(numbers))

print(f"Uchinchi element-{numbers[3]}")

if 30 in numbers:
    print("Ro'yxatda bor")
else:
    print("Royxatta yo'q")

new_roy = numbers[-2:]
summa = sum(numbers)
print(summa)

print(summa)


# 2-m
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits.append("kiwi")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.insert(2, "peach")
print(fruits)

fruits.sort()
print(fruits)

print(fruits)


# 3-m
scores = [85, 90, 78, 92, 88]
print(scores)

summa = sum(scores)
print(scores)
orta_r = summa / 2
print(orta_r)

print(max(scores))

new_r = scores
print(new_r[::-1])

print(scores)


# 4-m
items = [1, 2, 2, 3, 3, 4, 1]
print(items)

print(set(items))

new_r = items
print(new_r)

items.sort()
print(items)

print(items[1::-1])

print(len(items))

print(items)


# 5-m
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(list1)
print(list2)

list1.extend(list2)
print(list1)

list1.sort()
print(list1)

new_r = list2
print(list2)

summa = sum(list2)
print(summa)

print(list1)


# 6-m
values = [12, 5, 8, 19, 3, 15]
print(values)

print(max(values))

print(min(values))

m = values.index(max(values))
print(m)

m = values.index(min(values))
print(m)

print(values)


# 7-m
words = ["apple", "cherry", "banana", "date"]
print(words)

print(words[::-1])

rew_r = words
print(rew_r)

rew_r.sort()
print(rew_r)

print(len(rew_r))

print(words)


# 8-m
data = [10, 20, 30, 40, 50]
print(data)

if 30 in data:
    print("Bor")
else:
    print("Yo'q")

data.index(30)
print(data)

data.insert(3, 35)
print(data)

data.append(60)
print(data)

print(data)


# 9-m
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)

juft = sorted(n for n in nums if n % 2 == 0 )
print(juft)

summa = sum(juft)
print(summa)

juft.sort()
print(juft)

juft.append(10)
print(juft)

print(nums)
