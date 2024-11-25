'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kristýna Kaňovská
email: kris7cz@gmail.com
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# user database
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
divider = 40 * "-"

# user login
name = input("username: ")
password = input("password: ")

# cheking for existing user and correct password
correct_password = users.get(name)
if correct_password is None:
    print("unregistered user, terminating the program..")
    quit()
elif  correct_password != password:
    print("wrong password, terminating the program..")
    quit()

print(divider)
print(f"Welcome to the app, {name}\nWe have {len(TEXTS)} texts to be analyzed.")
print(divider)

# choosing text to analyze
number = input(f"Enter a number btw. 1 to {len(TEXTS)} to select: ")
if not number.isdecimal() or (number := int(number)) not in range(1, len(TEXTS) + 1):
    print("wrong input, terminating the program..")
    quit()

total_words = 0
total_titlecase_words = 0
total_lowercase_words = 0
total_uppercase_words = 0
total_number_strings = 0
number_sum = 0

# function for cleaning words
def clean_word(word):
    return word.strip(".,<>?!:")

clean_words = [clean_word(word) for word in TEXTS[number - 1].split()]

#  counting and analyzing the words
word_length_count = {}
for word in clean_words:
    word_length = len(word)
    if word_length in word_length_count.keys():
        word_length_count[word_length] += 1
    else:
        word_length_count[word_length] = 1
    
    if word.istitle():
        total_titlecase_words += 1
    elif word.isupper():
        total_uppercase_words += 1
    elif word.islower():
        total_lowercase_words += 1
    elif word.isdecimal():
        total_number_strings += 1
        number_sum += int(word)

# printing the total counts
print(divider)
print(f"""There are {len(clean_words)} words in the selected text.
There are {total_titlecase_words} titlecase words.
There are {total_uppercase_words} uppercase words.
There are {total_lowercase_words} lowercase words.
There are {total_number_strings} numeric strings.
The sum of all the numbers {number_sum}""")
print(divider)

max_count = max(word_length_count.values())
print(f"LEN|{'OCCURENCES':^{max_count+2}}|NR.")
print(divider)

# function for printing graphics of a single word length count
def print_word_length_count(length, count):
    print(f"{length:3}|{'*'*count:{max_count+2}}|{count}")

# printing all the length counts
for (length, count) in sorted([(length, count)
                               for length, count
                               in word_length_count.items()],
                               key=lambda tup: tup[0]):
    print_word_length_count(length, count)
