from doctest import OutputChecker
from pytube import YouTube

url = input('Digite a URL do YouTube: ')
download = YouTube(url)
caminho = input('Informe o caminho da pasta que você deseja salvar o download: ')

while True:
    tipo = int(input("Digite '1' para vídeo ou '2' para áudio: "))
    if tipo == 1 or tipo == 2:
        break

if tipo == 1:
    while True:
        resolucao = int(input("Digite '1' para alta resolução ou '2' para baixa resolução: "))
        if resolucao == 1 or resolucao == 2:
            break
    if resolucao == 1:
        download.streams.get_highest_resolution().download(output_path=caminho, filename="pytube")
        print("Download concluído.")
    else:
        download.streams.get_lowest_resolution().download(output_path=caminho)
        print("Download concluído.")
else:
    download.streams.filter(only_audio=True).first().download(output_path=caminho, filename="pytube" + "mp3")
    print("Download concluído.")




    

