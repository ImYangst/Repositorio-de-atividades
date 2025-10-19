import pyquotegen
from translate import Translator

def gerar_frase():
    frase = pyquotegen.get_quote("inspirational")
    return frase

def traduzir_frase():
    frase = gerar_frase()
    tradutor = Translator(to_lang="pt-br")
    traducao = tradutor.translate(frase)

    print(f"Sua frase é:\n'{traducao}'")

print("Gerando frase:...")
traduzir_frase()
