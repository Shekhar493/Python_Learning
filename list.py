marks1 = 45
marks2 = 78
marks3 = 89
marks4 = 67
marks5 = 90
marks6 = 56

marks = [marks1, marks2, marks3, marks4, marks5, marks6]
print("Marks List:", marks)
print("Length of Marks List:", len(marks))
print(type(marks))
total = sum(marks)
average = total / len(marks)
print("Total Marks:", total)
print("Average Marks:", average)
# Accessing elements
print("First Mark:", marks[0])
print("Last Mark:", marks[-1])
# Slicing
print("Marks from index 1 to 3:", marks[1:4])
# Modifying an element
marks[2] = 95
print("Updated Marks List:", marks)
# Adding a new mark
marks.append(88)
print("Marks List after adding a new mark:", marks)
# Removing a mark
marks.remove(marks1)
print("Marks List after removing the first mark:", marks)
# Sorting the marks
marks.sort()
print("Sorted Marks List:", marks)
# Reversing the marks
marks.reverse()
print("Reversed Marks List:", marks)
# Finding the index of a mark
index_of_67 = marks.index(67)
print("Index of mark 67:", index_of_67)
# Counting occurrences of a mark
count_of_90 = marks.count(90)
print("Count of mark 90 in the list:", count_of_90)
# Clearing the list
marks.clear()
print("Marks List after clearing:", marks)
# Re-initializing the list for further operations
marks = [marks1, marks2, marks3, marks4, marks5, marks6]
# Copying the list
marks_copy = marks.copy()
print("Copied Marks List:", marks_copy)
# Extending the list
marks.extend([100, 85])
print("Marks List after extending:", marks)
# Popping an element
popped_mark = marks.pop()
print("Popped Mark:", popped_mark)
print("Marks List after popping an element:", marks)
# Inserting an element at a specific position
marks.insert(2, 75)
print("Marks List after inserting 75 at index 2:", marks)
# Finding maximum and minimum marks
max_mark = max(marks)
min_mark = min(marks)
print("Maximum Mark:", max_mark)
print("Minimum Mark:", min_mark)
# Summing all marks
total_marks = sum(marks)
print("Total Marks after all operations:", total_marks)
# Checking if a mark exists in the list
is_89_present = 89 in marks
print("Is mark 89 present in the list?", is_89_present)
# Iterating through the list
for mark in marks:
    print("Mark:", mark)
# List comprehension to create a new list with marks greater than 70
high_marks = [mark for mark in marks if mark > 70]
print("Marks greater than 70:", high_marks)
# Finding the length of the new list
length_of_high_marks = len(high_marks)
print("Length of marks greater than 70 list:", length_of_high_marks)
# Sorting the new list
high_marks.sort()
print("Sorted marks greater than 70:", high_marks)
