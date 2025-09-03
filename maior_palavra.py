import string

def encontrar_maior_palavra(frase):
    """
    Encontra a maior palavra em uma frase, ignorando pontuações.

    :param frase: String contendo a frase.
    :return: A maior palavra encontrada na frase.
    """
    # Remove pontuações da frase
    frase_sem_pontuacao = frase.translate(str.maketrans('', '', string.punctuation))

    # Divide a frase em palavras
    palavras = frase_sem_pontuacao.split()

    # Encontra a maior palavra
    maior_palavra = max(palavras, key=len)

    return palavras