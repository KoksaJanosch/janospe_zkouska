
text = "aaaeioasdihsadisadosidjasdqoi woehq oiqwe kopoasd jasd "

samo = ["a", "e", "i", "o", "u"]

dic = {}
for index in range(len(text)):
    for i in range(len(samo)):
        if text[index] == samo[i]:
            if samo[i] in dic:
                dic[samo[i]] += 1
            else:
                dic[samo[i]] = 1
    
print(dic)


