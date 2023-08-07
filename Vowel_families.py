def Vowel_families(lst)->list :
    '''This function selects all words that have all the same vowels (in any order and/or number) as the first word, 
       including the first word.'''
    c = 0
    pattern_count = 0
    pattern_vowels = ''
    result = list()
    for letter in lst[0] :
        if letter in 'aeoiu' and letter not in pattern_vowels :
            pattern_count += 1
            pattern_vowels += letter
    for word in lst[1:] :
        for letter in word :
            if letter in 'aeoiu' and letter in pattern_vowels :
                c += 1
            else :
                if letter in 'aeoiu' and letter not in pattern_vowels :
                    c = 0 
                    break
        if c >= pattern_count :
            result.append(word)
            c = 0
        else :
            c = 0
    result.insert(0,lst[0])
    return result

print(Vowel_families.__doc__)
print()
print(Vowel_families(["toe", "ocelot", "maniac"]))
print(Vowel_families(["many", "carriage", "emit", "apricot", "animal"]))
print(Vowel_families(["hoops", "chuff", "bot", "bottom"]))
exit = input('Enter any key to exit :')
