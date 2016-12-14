## simple camelCase mini program
to_camelCase = input("Please introduce a string to camelCase\n")

stringSplit = to_camelCase.split(' ')## we break the string in several strings, omitting blank spaces

Container=[] ##empty list to store the strings

Index = 0

## method inspired from code from Stack Overflow
for string in stringSplit:
    if Index==0: ##Only one string
        oneString=string.lower()
        Container.append(oneString)
        Index += 1
        continue
    if Index != 0:
        Cameling = string[0].upper()+string[1:].lower()
        Container.append(Cameling)
CamelCaseComplete = ''.join(Container)
print("Your camelCase String is\n")
print(CamelCaseComplete)