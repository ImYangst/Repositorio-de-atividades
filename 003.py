from pytubefix import YouTube
url = input("Informe o url do Youtube:\n>>> ")
try:
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(f"Baixando: {yt.title} na resolução: {stream.resolution}")
    stream.download()
    print("Download concluído!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    print("Certifique-se de que o URL está correto e tente novamente.")