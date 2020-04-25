from pygame import mixer
# esta e uma biblioteca de jogos mais que tem varias funcionalidade

mixer.init()
mixer.music.load('exe21.mp3')
mixer.music.play()
input('Tá escutando ?')