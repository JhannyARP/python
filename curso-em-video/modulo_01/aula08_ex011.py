import winsound
import time

# Substitua pelo nome do seu arquivo. O winsound funciona melhor se o arquivo estiver na mesma pasta!
# Nota: O winsound prefere arquivos .wav, mas dependendo do Windows ele lê .mp3.
# Se puder converter seu ex11.mp3 para ex11.wav, o sucesso é 100% garantido.

print("Tocando música...")
winsound.PlaySound("ex11.wav", winsound.SND_FILENAME)