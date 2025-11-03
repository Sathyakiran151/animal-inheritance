'''4️⃣ Matrix Calculator

Goal: Perform matrix addition, subtraction, and multiplication.
Hint:

Create two 2D arrays using np.array().

Use np.add(), np.subtract(), and np.dot() for operations.'''
import numpy as np
a=np.array([
    [10,20,30],
    [30,50,60],
    [54,45,52]])
b=np.array([
    [30,70,80],
    [30,40,80],
    [51,55,71]])
print("The Martix of a :\n",a)
print("The Martix of b :\n",b)
print("Select an operation :\n1.add \n2.subtract\n3.multiply\n4.dot")
s =input("Enter the name of operation:")
if s=='add':
    print("the Addition of Two Matrix is :\n",np.add(a,b))
elif s=='subtract':
    print("the Subtraction of Two Matrix is :\n",np.subtract(a,b))
elif s=="multiply":
    print("the element wise Multiplication of Two Matrix is :\n",np.multiply(a,b))
elif s=="dot":
    print("the Matrix multiplication bu dot is :\n",np.dot(a,b))
else:
    print("invalid input error")