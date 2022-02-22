import csv
import random

while True:
    with open('liste_francais.csv', newline='', encoding='utf-8') as f:
        mots_jeu = [row[0] for row in csv.reader(f)]

    word_len = 6
    mot_secret = random.choice([word for word in mots_jeu if len(word)==word_len])

    list_mot_secret = list(mot_secret)

    list_mot_secret_mute = ["."] * word_len
    list_mot_secret_mute[0] = list_mot_secret[0]
    list_mot_secret_mute[word_len-1] = list_mot_secret[word_len-1]
    tentative = 0
    print(*list_mot_secret_mute, sep=" ")

    while list_mot_secret != list_mot_secret_mute:
        if tentative > 6:
            print("OHHHHHHHHH")
            print("La réponse était " + mot_secret)
            break
        input_word = input("Quel mot ? ")
        if len(input_word) != word_len:
            print('Le mot ne fait pas la bonne taille')
            print(*list_mot_secret_mute, sep="  ")
            tentative += 1
            continue        
        list_input_word = list(input_word)

        for count, value in enumerate(list_input_word):
            if value == list_mot_secret[count]:
                list_input_word[count] = list_mot_secret[count] + "_"
                list_mot_secret_mute[count] = list_mot_secret[count]
            elif value in list_mot_secret:
                list_input_word[count] = list_input_word[count] + "*"
        
        if list_input_word == [x + "_" for x in list_mot_secret]:
            print('Bieng joué')
            break
        print(*list_input_word, sep=" ")
        print(*list_mot_secret_mute, sep="  ")
        tentative += 1
   
    
    if input("Continuer (O/N)? ") == 'N':
        print("Allez à ciao bonsoir")
        break