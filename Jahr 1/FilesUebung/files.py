file1 = open("file1.txt", "r").readlines()
file2 = open("file2.txt", "r").readlines()

result = [int(x.rstrip('\n')) for x in file1 if x in file2]

# Write your code above 👆

print(result)


