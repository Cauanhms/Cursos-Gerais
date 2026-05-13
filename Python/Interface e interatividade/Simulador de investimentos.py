# =========================================================
#                EXPLICAÇÃO DAS BIBLIOTECAS
# =========================================================

# import tkinter as tk
#
# Importa a biblioteca Tkinter.
#
# Tkinter é a biblioteca responsável por criar
# interfaces gráficas no Python.
#
# Com ela você consegue criar:
#
# - janelas
# - botões
# - textos
# - menus
# - campos de digitação
# - caixas de seleção
#
# "as tk" cria um apelido para a biblioteca.
#
# Sem apelido:
# tkinter.Label()
#
# Com apelido:
# tk.Label()
#
# Isso deixa o código menor e mais organizado.



# from tkinter import ttk
#
# ttk significa:
# themed tk
#
# É uma extensão do Tkinter que possui
# componentes mais modernos visualmente.
#
# Exemplo:
#
# ttk.Combobox()
#
# Cria uma caixa de seleção mais bonita
# e mais profissional.



# from tkinter import messagebox
#
# Importa janelas prontas de mensagens.
#
# Serve para mostrar:
#
# - erros
# - alertas
# - confirmações
#
# Exemplo:
#
# messagebox.showerror()
#
# Mostra uma janela de erro.



# =========================================================
#              EXPLICAÇÃO DOS COMPONENTES
# =========================================================

# tk.Tk()
#
# Cria a janela principal do programa.
#
# Pense como:
# "ligar a interface gráfica".



# .title()
#
# Define o nome da janela.
#
# Esse texto aparece na barra superior.



# .geometry()
#
# Define o tamanho inicial da janela.
#
# Exemplo:
#
# "650x650"
#
# largura x altura



# .minsize()
#
# Define o tamanho mínimo permitido.
#
# Mesmo diminuindo a janela,
# ela nunca ficará menor que isso.



# .resizable()
#
# Define se a janela pode ser redimensionada.
#
# True = pode aumentar/diminuir
# False = tamanho fixo



# .configure(bg="")
#
# Muda a cor do fundo da janela.
#
# bg significa:
# background



# tk.Label()
#
# Cria textos na interface.
#
# Pode ser usado para:
#
# - títulos
# - descrições
# - resultados
# - avisos



# tk.Entry()
#
# Cria um campo de digitação.
#
# O usuário pode escrever nele.



# ttk.Combobox()
#
# Cria uma lista suspensa.
#
# O usuário escolhe uma opção.



# tk.Button()
#
# Cria um botão clicável.



# tk.Frame()
#
# Funciona como uma caixa organizadora.
#
# Serve para separar partes da interface.



# .pack()
#
# Coloca o componente na tela.
#
# Sem pack():
# o componente existe,
# mas não aparece.



# .config()
#
# Altera propriedades de um componente
# depois que ele já foi criado.
#
# Exemplo:
#
# mudar texto
# mudar cor
# mudar fonte



# .get()
#
# Pega informações digitadas pelo usuário.



# .mainloop()
#
# Mantém a janela aberta.
#
# Sem isso:
# o programa fecha imediatamente.



# =========================================================
#                    IMPORTAÇÕES
# =========================================================

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# =========================================================
#                FUNÇÃO DE SIMULAÇÃO
# =========================================================

def simular_investimento():

    try:

        # Pega o valor digitado
        valor = float(campo_valor.get())

        # Pega o investimento escolhido
        tipo = combo_investimento.get()

        # Taxas fictícias
        taxas = {
            "Poupança": 0.005,
            "CDB": 0.010,
            "LCI/LCA": 0.012,
            "Tesouro Direto": 0.015
        }

        # Seleciona a taxa correta
        taxa = taxas[tipo]

        # Fórmula de juros compostos
        montante = valor * ((1 + taxa) ** 12)

        # Atualiza o texto do resultado
        label_resultado.config(
            text=f"Valor após 12 meses:\nR$ {montante:.2f}"
        )

    except:

        # Mostra erro se o usuário digitar algo inválido
        messagebox.showerror(
            "Erro",
            "Digite um valor válido!"
        )


# =========================================================
#                CRIAÇÃO DA JANELA
# =========================================================

janela = tk.Tk()

janela.title("Simulador de Investimentos - Sicredi")

janela.geometry("650x650")

janela.minsize(500, 500)

janela.resizable(True, True)

janela.configure(bg="white")


# =========================================================
#                     TÍTULO
# =========================================================

titulo = tk.Label(

    janela,

    text="SICREDI - INVEST",

    font=("Arial", 18, "bold"),

    bg="#005c36",

    fg="white",

    pady=15
)

titulo.pack(fill="x")


# =========================================================
#                  TEXTO EXPLICATIVO
# =========================================================

texto = tk.Label(

    janela,

    text="Digite um valor e escolha um investimento",

    font=("Arial", 11),

    bg="white"
)

texto.pack(pady=20)


# =========================================================
#                   LABEL VALOR
# =========================================================

label_valor = tk.Label(

    janela,

    text="Valor Inicial:",

    font=("Arial", 12),

    bg="white"
)

label_valor.pack()


# =========================================================
#                CAMPO DE DIGITAÇÃO
# =========================================================

campo_valor = tk.Entry(

    janela,

    font=("Arial", 12),

    width=25
)

campo_valor.pack(pady=10)


# =========================================================
#              LABEL TIPO INVESTIMENTO
# =========================================================

label_tipo = tk.Label(

    janela,

    text="Tipo de Investimento:",

    font=("Arial", 12),

    bg="white"
)

label_tipo.pack()


# =========================================================
#                    COMBOBOX
# =========================================================

combo_investimento = ttk.Combobox(

    janela,

    values=[
        "Poupança",
        "CDB",
        "LCI/LCA",
        "Tesouro Direto"
    ],

    font=("Arial", 11),

    width=22
)

combo_investimento.pack(pady=10)

combo_investimento.current(0)


# =========================================================
#                     BOTÃO
# =========================================================

botao = tk.Button(

    janela,

    text="Simular",

    font=("Arial", 12, "bold"),

    bg="#005c36",

    fg="white",

    width=20,

    command=simular_investimento
)

botao.pack(pady=20)


# =========================================================
#                   RESULTADO
# =========================================================

label_resultado = tk.Label(

    janela,

    text="",

    font=("Arial", 14, "bold"),

    bg="white",

    fg="#005c36"
)

label_resultado.pack(pady=20)


# =========================================================
#              FRAME DAS EXPLICAÇÕES
# =========================================================

frame_explicacao = tk.Frame(

    janela,

    bg="#f2f2f2",

    bd=1,

    relief="solid"
)

frame_explicacao.pack(
    pady=20,
    padx=20,
    fill="both",
    expand=True
)


# =========================================================
#           TÍTULO DA ÁREA DE EXPLICAÇÃO
# =========================================================

titulo_exp = tk.Label(

    frame_explicacao,

    text="Tipos de Investimentos",

    font=("Arial", 13, "bold"),

    bg="#f2f2f2",

    fg="#005c36"
)

titulo_exp.pack(pady=10)


# =========================================================
#          TEXTO EXPLICATIVO DOS INVESTIMENTOS
# =========================================================

explicacao = tk.Label(

    frame_explicacao,

    text=
    "• Poupança:\n"
    "Baixo risco e baixo rendimento.\n\n"

    "• CDB:\n"
    "Renda fixa emitida por bancos.\n\n"

    "• LCI/LCA:\n"
    "Isento de imposto de renda.\n\n"

    "• Tesouro Direto:\n"
    "Títulos públicos do governo.",

    font=("Arial", 10),

    bg="#f2f2f2",

    justify="left",

    wraplength=550,

    padx=15,

    pady=10
)

explicacao.pack(fill="both")


# =========================================================
#                    MAINLOOP
# =========================================================

janela.mainloop()