def sao_anagramas(string1, string2):
    string1_limpa = string1.replace(" ", "").lower()
    string2_limpa = string2.replace(" ", "").lower() 
    if len(string1_limpa) != len(string2_limpa):
             return False
    return sorted(string1_limpa) == sorted(string2_limpa)
