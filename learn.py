from phrase import Phrase, TranslatedPhrase

a_list = ["ant", "bat", "cat", 42]

t_list = ("ant", "bat", "cat", 42)

for each in a_list:
    print(each)

for i, e in enumerate(a_list):
    print(f"a[{i}] = {e}")
    if e == "bat":
        print("breaking out of the loop")
        break

s2 = {3, 1, 4, 2}

s3 = {"ant", "bat", "cat", 1, 1, "cat"}

print(s2)

print(s3)

print(s2 | s3)
print(s2 & s3)

user = {}
user["first_name"] = "Michael"
user["last_name"] = "Hartl"

print (user["first_name"])

if "first_name" in user:
    print(user["first_name"])

palindrome = Phrase("oooooo")

frase = TranslatedPhrase("recognize", "reconocer")
print ("xxx-------------------")
print (frase.is_palindrome())

# print(palindrome.is_palindrome())