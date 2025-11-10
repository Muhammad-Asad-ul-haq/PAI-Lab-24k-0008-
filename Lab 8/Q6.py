import matplotlib.pyplot as plt

math_marks = [78, 85, 62, 90, 70, 88, 76, 95, 67, 80]
science_marks = [82, 79, 65, 92, 72, 85, 78, 94, 69, 83]

plt.scatter(math_marks, science_marks, color='blue', label='Students')
plt.title("Comparison of Mathematics and Science Marks")
plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")
plt.legend()
plt.show()
