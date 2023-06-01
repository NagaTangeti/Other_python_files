favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
	print(name.title())

for name in favorite_languages:
	print(name.title())

for name in sorted(favorite_languages):
	print(f"\n{name.title()}, thank u for taking the poll.")

for language in favorite_languages.values():
	print(language.title())

for language in set(favorite_languages.values()):
	print(language.title())

languages = {'python', 'ruby', 'c', 'python'} #this is a set, not to be mistaken with dictionary.
print(languages)

favorite_languages1 = {
	'jen' : ['python', 'ruby'],
	'sarah' : 'c',
	'edward' : ['ruby', 'go'],
	'phil' : ['python', 'haskell'],
}
for name, languages in  favorite_languages1.items():
	if len(languages) == 1:

		print(f"{name.title()}'s favorite languages is:")
		for language in languages:
			print(f"\t{language.title()}")
	else: 
		print(f"{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t{language.title()}")