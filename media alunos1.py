# ---------- LEITURA E VALIDAÇÃO ----------

def ler_nota(mensagem):
    """Pede uma nota ao usuário até que ela seja válida (entre 0 e 10)."""
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")


# ---------- CÁLCULOS E DECISÕES ----------

def calcular_media(notas):
    """Recebe uma lista de notas e devolve a média."""
    return sum(notas) / len(notas)


def verificar_aprovacao(media, minimo=7):
    """Devolve True se a média atingir a nota mínima."""
    return media >= minimo


def estatisticas_turma(alunos):
    """Devolve um dicionário com os números gerais da turma."""
    aprovados = sum(1 for aluno in alunos if aluno["aprovado"])
    medias = [aluno["media"] for aluno in alunos]
    # max() com key escolhe o aluno que tem a maior média
    melhor = max(alunos, key=lambda aluno: aluno["media"])
    return {
        "aprovados": aprovados,
        "reprovados": len(alunos) - aprovados,
        "media_turma": calcular_media(medias),
        "melhor_aluno": melhor,
    }


# ---------- CADASTRO ----------

def cadastrar_aluno(disciplinas, minimo):
    """Lê as notas de um aluno e devolve um dicionário com seus dados."""
    nome = input("\nNome do aluno: ")
    notas = {}
    for disciplina in disciplinas:
        notas[disciplina] = ler_nota(f"  Nota de {disciplina}: ")

    media = calcular_media(list(notas.values()))
    return {
        "nome": nome,
        "notas": notas,
        "media": media,
        "aprovado": verificar_aprovacao(media, minimo),
    }


# ---------- RELATÓRIO ----------

def montar_relatorio(alunos, minimo):
    """Monta o relatório da turma e devolve como texto."""
    stats = estatisticas_turma(alunos)
    melhor = stats["melhor_aluno"]

    linhas = []
    linhas.append("=" * 42)
    linhas.append("        RELATÓRIO FINAL DA TURMA")
    linhas.append("=" * 42)
    linhas.append(f"Nota mínima para aprovação: {minimo:.1f}")
    linhas.append("-" * 42)
    for aluno in alunos:
        situacao = "APROVADO" if aluno["aprovado"] else "REPROVADO"
        linhas.append(f"{aluno['nome']:<20} {aluno['media']:>5.2f}  {situacao}")
    linhas.append("-" * 42)
    linhas.append(f"Aprovados.........: {stats['aprovados']}")
    linhas.append(f"Reprovados........: {stats['reprovados']}")
    linhas.append(f"Média da turma....: {stats['media_turma']:.2f}")
    linhas.append(f"Maior média.......: {melhor['nome']} ({melhor['media']:.2f})")
    linhas.append("=" * 42)
    return "\n".join(linhas)


def salvar_relatorio(texto, arquivo="relatorio_turma.txt"):
    """Salva o texto do relatório em um arquivo .txt."""
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(texto)
    print(f"\nRelatório salvo em '{arquivo}'.")


# ---------- PROGRAMA PRINCIPAL ----------

def main():
    minimo = ler_nota("Nota mínima para aprovação: ")
    entrada = input("Disciplinas (separadas por vírgula): ")
    disciplinas = [d.strip() for d in entrada.split(",") if d.strip()]
    quantidade = int(input("Quantos alunos? "))

    alunos = []
    for _ in range(quantidade):          # o laço repete o cadastro
        alunos.append(cadastrar_aluno(disciplinas, minimo))

    relatorio = montar_relatorio(alunos, minimo)
    print("\n" + relatorio)
    salvar_relatorio(relatorio)


main()