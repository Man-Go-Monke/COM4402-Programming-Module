Name = "Sam"
Age = 19
CourseName = "CM4402"
#using plus adv common in any language
#disadv You have to change data types to str if they already aren't.
print("Your Details: "
      "\nName = " + Name +
      "\nAge = " + str(Age) +
      "\nCourse = " + CourseName)

#Using commas
#adv simple to use its very similar to plus and you don't have to change data types in text
#disadv can be tedious to use
print("Your Details: "
      "\nName = ", Name,
      "\nAge = ", Age,
      "\nCourse = ", CourseName)
#Using f""
#adv easy to use, don't need to change data types
print(f"Your Details:"
      f"\nName: {Name.title()} "
      f"\nAge: {Age}"
      f"\nCourse: ({CourseName.upper()})")