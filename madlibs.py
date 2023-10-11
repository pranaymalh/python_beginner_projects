adj  = input("Adjective: ")
foods1 = input("Foods (plural): ")
verb = input("Verb: ")
saying = input("Saying: ")
noun = input("Noun: ")
foods2 = input("Foods (plural): ")
color = input("Color: ")
ride = input("Something you would ride in: ")
animal = input("Animal: ")
person = input("Person: ")

madlib = f"Today I went to my favorite Taco Stand called the {adj} {animal}. \
Unlike most food stands, they cook and prepare the food in a {ride} while you {verb}. \
The best thing on the menu is the {color} {noun}. \
Instead of ground beef they fill the taco with {foods2}, cheese, and top it off with a salsa made from {foods1}. \
If that doesn't make your mouth water, then it's just like {person} always says: {saying}!"

print(madlib)