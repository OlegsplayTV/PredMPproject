import csv

f = open('students.csv', encoding='UTF-8')
reader = list(csv.reader(f))

# 1
name_for_search, surname_for_search = 'Хадаров Владимир'.split()

for i in range(len(reader)):
    reader[i] = str(reader[i][0]).split(';')

# for line in reader:
#     if name_for_search in str(line) and surname_for_search in str(line):
#         print(f'Ты получил: {line[1]}, за проект: {line[-1]}')


print(reader[0])

classes = []
for i in range(1, len(reader)):
    if not reader[i][3] in classes:
        classes.append(reader[i][3])
print(classes)

sr_scores = []
for each_class in classes:
    count = 0
    summ = 0
    sr_score = 0
    for i in range(1, len(reader)):
        if reader[i][3] == each_class and reader[i][-1] != 'None':
            summ += int(reader[i][-1])
            count += 1
    sr_score = round(summ/count, 3)
    sr_scores.append(sr_score)

for i in range(len(classes)):
    each_class = classes[i]
    for k in range(1, len(reader)):
        #print(sr_scores[i])
        if reader[k][3] == each_class and reader[k][-1] == 'None':
            reader[k][4] = str(sr_scores[i])

count = 0
for_change = []

while count < len(reader)-2:
    count = 0
    for i in range(1, len(reader)-1):
        if float(reader[i][-1]) < float(reader[i+1][-1]):
            for_change = reader[i+1]
            reader[i + 1] = reader[i]
            reader[i] = for_change
        else:
            count += 1
    #print(count)

print(reader)


