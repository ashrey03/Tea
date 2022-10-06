character = "X-DSPAM-Confidence:0.8475"

find1 = character.find(":")
print("Indice: "+ str(find1))

find2 = character.find("5")
print("Finaliza en: "+ str(find2))

ultimo = len(character)
substring = character[find1+1:ultimo]
chr = float(substring)

print(chr)
print(type(chr))