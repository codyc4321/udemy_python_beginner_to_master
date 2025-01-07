
def passed_classes():
    math_grade = int(input("What was your grade in math? "))
    physics_grade = int(input("What was your grade in physics? "))
    chem_grade = int(input("What was your grade in chemistry? "))
    if math_grade >= 45 and physics_grade >= 45 and chem_grade >= 45:
        print("you passed the class!")
    else:
        print("you failed at least 1 class")


def admin_access():
    username = input("Please enter username: ")
    if username in ["john", "smith"]:
        print("Authorized")
    else:
        print("Not authorized")


def vowel_or_not():
    VOWELS = ["a", "e", "i", "o", "u"]
    letter = input("Enter a letter to determine if it's a vowel: ")
    if letter in VOWELS:
        print("Is a vowel")
    else:
        print("Not a vowel")



if __name__ == "__main__":
    passed_classes()
    admin_access()
    vowel_or_not()