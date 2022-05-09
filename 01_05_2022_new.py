def average_mark(n):
    marks_list = []
    marks_sum = 0
    for i in range(n):
        x_i = int(input("Input the mark: "))
        marks_list.append(x_i)
        marks_sum += x_i
    # return marks_list
    return marks_list, marks_sum, marks_sum / n


marks_amount = int(input("Input the number of marks: "))
list_of_marks, sum_of_marks, aver_mark = average_mark(marks_amount)
print(" List of marks: {} \n Sum of marks: {} \n Average mark: {} \n". format(list_of_marks, sum_of_marks, aver_mark))
# print(" List of marks:", list_of_marks, '\n',
#     "Sum of marks:", sum(list_of_marks), '\n',
#     "Average mark:", sum(list_of_marks) / marks_amount)
# print(average_mark(marks_amount))


