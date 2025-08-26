tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]
tabuleiro[0][0] = tabuleiro[0][7] = 'tor'
tabuleiro[0][1] = tabuleiro[0][6] = 'cav'
tabuleiro[0][2] = tabuleiro[0][5] = 'bis'
tabuleiro[0][3] = 'rai'
tabuleiro[0][4] = 'rei'


tabuleiro[1] = ['pea' for _ in range(8)]


tabuleiro[6] = ['pea' for _ in range(8)]


tabuleiro[7][0] = tabuleiro[7][7] = 'tor'
tabuleiro[7][1] = tabuleiro[7][6] = 'cav'
tabuleiro[7][2] = tabuleiro[7][5] = 'bis'
tabuleiro[7][3] = 'rai'
tabuleiro[7][4] = 'rei'


print("Tabuleiro de xadrez inicial:")
for linha in tabuleiro:
    print(' '.join(linha))