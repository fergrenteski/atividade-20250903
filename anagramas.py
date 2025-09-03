def sao_anagramas(string1, string2):
    """
    Verifica se duas strings são anagramas uma da outra.
    
    Um anagrama é uma palavra ou frase formada pelo rearranjo das letras
    de outra palavra ou frase. Espaços e diferenças entre maiúsculas e 
    minúsculas são ignorados.
    
    Args:
        string1 (str): Primeira string para comparação
        string2 (str): Segunda string para comparação
    
    Returns:
        bool: True se as strings forem anagramas, False caso contrário
    """
    # Remove espaços e converte para minúsculas
    string1_limpa = string1.replace(" ", "").lower()
    string2_limpa = string2.replace(" ", "").lower()
    
    # Se os tamanhos são diferentes, não podem ser anagramas
    if len(string1_limpa) != len(string2_limpa):
        return False
    
    # Ordena as letras de ambas as strings e compara
    return sorted(string1_limpa) == sorted(string2_limpa)
