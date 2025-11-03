'''Top NumPy Project Ideas (with Hints)
🔹 1️⃣ Student Marks Analysis

Goal: Analyze students’ marks using NumPy arrays.
Hint:

Create arrays for marks in different subjects.

Use np.mean(), np.max(), np.min() to find topper, average, and least marks.

Show the student with highest average.'''
import numpy as np
marks=np.array([
    [23,21,21],  # student marks in row
    [14,12,11],   # subject in column
    [16,15,13],
    [13,14,13],
    [25,24,21]])
# average of each student by axis =1
avg_marks=np.mean(marks,axis=1,dtype="int")
print("the Average of students :",avg_marks.reshape(-1,1)) 
topper_index=np.argmax(avg_marks)
least_index=np.argmin(avg_marks)
print("The Top Scorer Student is :",topper_index+1)
print("The low Scorer Student is :",least_index+1)
avg_subject=np.mean(marks,axis=0)
print("The Average subject marks is :",avg_subject)
Highest_marks=np.max(marks,axis=0)
print("The Highest marks per subject is :",Highest_marks)
Lowest_marks=np.min(marks,axis=0)
print("The Lowest marks per subject is :",Lowest_marks)

for i,avg in enumerate(avg_marks):
    print(f"Student{i+1} Average is : {avg}")



