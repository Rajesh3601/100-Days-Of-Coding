#Given list is [2,3,6,6,5]. The maximum score is , second maximum is . Hence, we print  as the runner-up score.
n = int(input())
arr = map(int, input().split())
a = list(arr)
r = max(a)
while max(a) == r:
    a.remove(max(a))

print(max(a))


# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s)
# of any student(s) having the second lowest grade.

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks = student_marks[query_name]
    total = (sum(query_marks)/ len(query_marks))
    print("{0:.2f}".format(total))
    
    
