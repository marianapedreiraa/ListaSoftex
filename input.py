notas = []
for aluno in range(1, 3):
    print(f"\nNotas do aluno {aluno}:")
    
    notas_aluno = []
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i}: "))
        notas_aluno.append(nota)
        notas.append(notas_aluno)
        print("\n---")
for i, notas_aluno in enumerate(notas):
    media = sum(notas_aluno) / len(notas_aluno)
    print(f"A média do aluno {i + 1} é: {media:.2f}")