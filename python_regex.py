import re

txt = "The rain in Spain"


def search():
    x = re.search("^The.*Spain$", txt)
    if x:
        print("YES! We have a match!")
    else:
        print("No match")


def find_all():
    x = re.findall("ai", txt)
    print(x)


def split():
    x = re.split('\s', txt, 1)
    print(x)


def replace_with(org_str, rep_str):
    x = re.sub(org_str, rep_str, txt, 1)
    print(x)


def return_string_start_with(my_char):
    # Search for an upper case "S" character in the beginning of a word, and print the word:
    x = re.search(r"\b" + my_char + "\w+", txt)
    print(x.group())


search()
find_all()
split()
return_string_start_with("T")
replace_with("ai", "ia")