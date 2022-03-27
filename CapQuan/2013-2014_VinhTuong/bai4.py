n = int(input("Enter n: "))
inp = input("Enter numbers: ")

while len(inp.split(" ")) > n or len(inp.split(" ")) < n:
    print("Input > n or < n")
    inp = input("Enter numbers again: ")

lists = list(inp.split(" "))

sum_list = 0
for i in range (0, n):
    sum_list = sum_list + int(lists[i])

print(sum_list)
