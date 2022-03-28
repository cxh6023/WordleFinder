# Problem List: Double letters in a word confuse the shit out of it

from english_words import english_words_lower_set

words = []
for word in english_words_lower_set:
    if len(word) == 5:
        words.append(word)


def main():
    used = ["dREad", "th_E", "wo_sE", "b__Ry", "p__il"]
    # Capital means the letter isn't in the spot
    # Lowercase means the letter isn't in the word
    # UnderScore means the letter is in the right spot


    possibleWordsList, notUsed, notInWord = possibleWords("_ER__", used) # Capital letter(we know it's here)
                                     # Lowercase Letter (we know it's in a different spot)
                                     # Underscore(_) (we know it's a new letter)
    print(notUsed)
    print("Not In Word: " + str(notInWord))
    print(likelyWord(possibleWordsList, used))


def possibleWords(str, used):

    notThere = [[], [], [], [], []]  # this stores the letters are not in the spot
    notInWord = []

    for word in used:
        for index, ch in enumerate(word):
            if ch.isupper() and (ch.lower() not in notThere[index]):  # if we know the letter isn't there
                print(ch)
                print(notThere[index])
                notThere[index].append(ch.lower())
            elif ch.islower() and (ch.lower() not in notInWord):
                notInWord.append(ch)

    useableWords = []
    for word in words:
        for i, ch in enumerate(word):
            # if not ((str[i].isupper() and str[i].lower() == ch) or (str[i].islower() and str[i].lower() in word) or (str[i] == '_')):  # if the potential word is no longer valid
            if (not ((str[i].isupper() and str[i].lower() == ch) or (str[i].islower() and str[i].lower() in word) or (str[i] == '_'))) or (ch in notInWord) or (ch in notThere[i]):  # if the potential word is no longer valid
                break
            if i == 4:
                useableWords.append(word)
    return useableWords, notThere, notInWord


def likelyWord(words, used):
    startingLetters = ['t', 'a', 'o', 'd', 'w']
    endingLetters = ['e', 's', 'd', 't']
    commonLetters = ['e', 't', 'a', 'i', 'o', 'n', 's', 'h', 'r']
    bestValue = 0 # one point for a common letter,
                  # 2 points for a common starting letter,
                  # or a common ending letter
    bestWord = ""
    currentValue = 0
    for word in words:
        if not (word in used):
            if word[0] in startingLetters:
                currentValue += 2
            if word[1] in commonLetters:
                currentValue += 1
            if word[2] in commonLetters:
                currentValue += 1
            if word[3] in commonLetters:
                currentValue += 1
            if word[4] in endingLetters:
                currentValue += 2
            if currentValue > bestValue:
                bestValue = currentValue
                bestWord = word
        currentValue = 0
    print(bestValue)
    return bestWord

main()