# 📊 Sistema de Notas da Turma

Programa em Python, executado no terminal, que cadastra alunos, calcula a média de cada um, define se foi aprovado ou reprovado e gera um relatório final da turma, exibido na tela e salvo em um arquivo `.txt`.

## ✨ Funcionalidades

- Define a **nota mínima de aprovação** (valor entre 0 e 10)
- Aceita **disciplinas personalizadas** (informadas pelo usuário)
- Cadastra **quantos alunos forem necessários**
- **Valida as notas**: só aceita números entre 0 e 10
- Calcula a **média individual** e a situação (aprovado/reprovado)
- Gera estatísticas da turma: aprovados, reprovados, média geral e aluno com a maior média
- **Salva o relatório** em `relatorio_turma.txt`

## 🛠️ Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa (usa apenas recursos nativos)

## ▶️ Como executar

```bash
python boletim.py
```

> Substitua `boletim.py` pelo nome que você deu ao arquivo.

## 💻 Exemplo de uso

```
Nota mínima para aprovação: 7
Disciplinas (separadas por vírgula): Matemática, Português, História
Quantos alunos? 2

Nome do aluno: Ana
  Nota de Matemática: 8
  Nota de Português: 9.5
  Nota de História: 7

Nome do aluno: Bruno
  Nota de Matemática: 5
  Nota de Português: 6
  Nota de História: 4.5
```

**Saída:**

```
==========================================
        RELATÓRIO FINAL DA TURMA
==========================================
Nota mínima para aprovação: 7.0
------------------------------------------
Ana                   8.17  APROVADO
Bruno                 5.17  REPROVADO
------------------------------------------
Aprovados.........: 1
Reprovados........: 1
Média da turma....: 6.67
Maior média.......: Ana (8.17)
==========================================

Relatório salvo em 'relatorio_turma.txt'.
```

## 🧩 Estrutura do código

| Função | O que faz |
|---|---|
| `ler_nota(mensagem)` | Pede uma nota ao usuário e repete até receber um valor válido (0 a 10) |
| `calcular_media(notas)` | Recebe uma lista de notas e devolve a média |
| `verificar_aprovacao(media, minimo)` | Retorna `True` se a média for maior ou igual ao mínimo (padrão: 7) |
| `estatisticas_turma(alunos)` | Calcula aprovados, reprovados, média da turma e melhor aluno |
| `cadastrar_aluno(disciplinas, minimo)` | Lê nome e notas de um aluno e devolve um dicionário com seus dados |
| `montar_relatorio(alunos, minimo)` | Monta o texto formatado do relatório |
| `salvar_relatorio(texto, arquivo)` | Grava o relatório em um arquivo `.txt` |
| `main()` | Controla o fluxo principal do programa |

### Estrutura de dados de um aluno

```python
{
    "nome": "Ana",
    "notas": {"Matemática": 8.0, "Português": 9.5, "História": 7.0},
    "media": 8.166666666666666,
    "aprovado": True
}
```

## ⚠️ Observações e limitações

- Se o número de alunos for digitado com um valor não numérico (por exemplo, `abc`), o programa encerra com erro, pois essa entrada não é validada.
- Se nenhum aluno for cadastrado (`0`) ou nenhuma disciplina for informada, o programa também gera erro nos cálculos.
- Em caso de empate na maior média, o primeiro aluno cadastrado é o escolhido.
- O arquivo `relatorio_turma.txt` é **sobrescrito** a cada execução.

## 🚀 Ideias de melhorias

- Validar a quantidade de alunos e de disciplinas
- Permitir notas com pesos diferentes por disciplina
- Exportar o relatório em CSV ou PDF
- Adicionar `if __name__ == "__main__":` para permitir importar as funções em outros arquivos

## 📄 Licença

Livre para uso educacional e modificação.
