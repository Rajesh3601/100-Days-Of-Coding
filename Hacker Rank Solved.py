#Given list is [2,3,6,6,5]. The maximum score is , second maximum is . Hence, we print  as the runner-up score.
n = int(input())
arr = map(int, input().split())
a = list(arr)
r = max(a)
while max(a) == r:
    a.remove(max(a))

print(max(a))


# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

