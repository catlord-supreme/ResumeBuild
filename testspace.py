category_list = []

class Category:
    def __init__(self, name):
        self.name = name
        self.skills = []

    def set_skill(self, skill):
        self.skills.append(skill)


for i in range (3):
    name = input("Enter the name of the category: ")
    category_list.append(Category(name))
    for i in range(3):
        skill = input(f"Enter a skill for category {name}: ")
        category_list[-1].set_skill(skill)

for category in category_list:
    print(f"Category: {category.name}")
    print("Skills:")
    for skill in category.skills:
        print(f"- {skill}")




