
def get_user_age():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return [name, age]

def print_message(name, age):
    if age >= 18:
        print(f"Hello {name}, you are an adult.")
    else:
        print(f"Hello {name}, you are under 18.")

details = get_user_age()
print_message(details[0], details[1])