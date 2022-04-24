# ################### WITH LISTS. O(n) to find marks of a students 
# import csv
# scores =[]
# with open('scores.csv', mode = 'w+', newline='')as f:
# 	writer = csv.writer(f, delimiter=',')
# 	writer.writerow(['Name', 'Score'])
# 	writer.writerow(['Lyn', '90'])
# 	writer.writerow(['Joj', '80'])
# 	writer.writerow(['Ray','98'])

# with open('scores.csv', mode='r') as f:
# 	for line in f:
# 		token = line.split(',')
# 		name = token[0]
# 		marks = token[1]
# 		scores.append([name, marks])
# print(scores)

# for _ in scores:
# 	if _[0] == 'Lyn':
# 		print(marks)

################### WITH DICTS. O(1) time complexity to find marks of a students 
import csv
scores = {}

# creating the csv
with open('scores.csv', mode = 'w+', newline='')as f:
	writer = csv.writer(f, delimiter=',')
	writer.writerow(['Name', 'Score'])
	writer.writerow(['Lyn', '90'])
	writer.writerow(['Joj', '80'])
	writer.writerow(['Ray','98'])

with open('scores.csv', mode='r') as f:
	for line in f:
		token = line.split(',')
		name = token[0]
		marks = token[1]
		scores[name] = marks

# O(1)
print(scores)
print(scores['Lyn'])
del scores['Ray']
print(scores)
scores['Peace'] = '100'
print(scores)





# scores = []
# n = int(input('Enter number of students: '))


# for i in range(0,n):
# 	name = input('Enter your name: ')
# 	marks = int(input('Enter marks: '))
# 	scores.append([name, marks])
# print(scores)

# if scores[0][0]=='Lyn':
# 	print(scores[0][1])
# else:
# 	print('Unknown.')

# # ##### REMARKS
# # Time analysis is O(n)
# # Try with dicts

# scores = {}
# name = input('Enter your name: ')
# marks = int(input('Enter marks: '))
# scores.key(name)
# scores.value(marks)
# print(scores)