def introduce(name, age, profession):
    print("Hello I am", name)
    print("I am", age, "years old")
    print("I am a", profession)


name = input()
# introduce("Peter Parker", 20, "Photographer")

# Keyword arguments
introduce(age=20, profession="Photographer", name=name)
