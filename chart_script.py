import matplotlib.pyplot as plt

categories = ["Python", "Java", "AI", "Web"]
values = [85, 70, 95, 80]

plt.bar(categories, values, color="steelblue")
plt.title("Training Skills Overview")
plt.xlabel("Category")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("training_chart.png")
plt.show()
