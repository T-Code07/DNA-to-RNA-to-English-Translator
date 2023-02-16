AlphaToRNA = {
    "A" : "TAT",
    "a" : "TAG",
    "B" : "TAA",
    "b" : "GCC",
    "C" : "TCG",
    "c" : "GCG",
    "D" : "GCA",
    "d" : "GTC",
    "E" : "GTE",
    "e" : "GTG",
    "F" : "GTA",
    "f" : "GGC",
    "G" : "GGT",
    "g" : "GGG",
    "H" : "GGA",
    "h" : "GAC",
    "I" : "GAT",
    "i" : "GAG",
    "J" : "GAA",
    "j" : "ACC",
    "K" : "ACG",
    "k" : "ACA",
    "L" : "ATG",
    "l" : "ATA",
    "M" : "AGC",
    "m" : "AGT",
    "N" : "AGG",
    "n" : "AGA",
    "O" : "AAC",
    "o" : "AAT",
    "P" : "AAG",
    "p" : "AAA",
    "Q" : "CCC",
    "q" : "CCT",
    "R" : "CCG",
    "r" : "CCA",
    "S" : "CTC",
    "s" : "CTT",
    "T" : "CTG",
    "t" : "CTA",
    "U" : "CGC",
    "u" : "CGT",
    "V" : "CGG",
    "v" : "CGA",
    "W" : "CAC",
    "w" : "CAT",
    "X" : "CAG",
    "x" : "CAA",
    "Y" : "TCC",
    "y" : "TCT",
    "Z" : "TCG",
    "z" : "TCA"
  
 }

SpecialCharactersDict = {
    "!" : ["TTC", "TTT"],
    "." : ["TTG", "TTA"],
    " " : ["TGC", "TGT", "TGG", "TGA"],
    "start" : "TAC",
    "stop" : ["ACT", "ATT", "ATC"]
}

RNA_Dict_Key = list()
RNA_values = list()
SpecialChar_DictKey = list()
SpecialChar_Values = list()
translatedInput = str()

emmyMessage = "GGA GTG CTA  GTG  CCA AAT  TCA  TCT  GGG AAT TAG CTA CTT TTA TGC TAG ATA ATA GTG ATA GTG TGC CGT AGA GTG CGA GTG AGA TTA"

def compile_RNA_ALPHA_Lists():
    for RNA_key in AlphaToRNA:
        RNA_Dict_Key.append(RNA_key)


    for RNA_value in AlphaToRNA:
        RNA_values.append(AlphaToRNA[RNA_value])



def compile_SpecialChar_Lists():
    for key in SpecialCharactersDict:
        SpecialChar_DictKey.append(key)


    for char in SpecialCharactersDict:
        SpecialChar_Values.append(SpecialCharactersDict[char])

compile_RNA_ALPHA_Lists()
compile_SpecialChar_Lists()

while True:
    userInput = input("Please input the DNA code: ")

    if userInput == "e":
        print("Message: " + emmyMessage)
        userInput = emmyMessage
    
    splitUserInput = userInput.split()        

    for splitInput in splitUserInput:
        if splitInput in RNA_values:
            index = RNA_values.index(splitInput)
            correspondingKeyIndex = RNA_Dict_Key[index]
            translatedInput += correspondingKeyIndex
    
        else:
            index = -1
            for value in SpecialChar_Values:
                if index != -1: 
                    translatedInput += SpecialChar_DictKey[index]
                    break

                if type(value) is list:
                    possibleIndex = SpecialChar_Values.index(value)
                    for code in value:
                        if splitInput == code:
                            index = possibleIndex
                            break
                elif type(value) is str:
                    index = SpecialChar_Values.index(value)
                
    print("Translation: " + translatedInput)
    translatedInput = ""