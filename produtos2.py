import tkinter as tk


def contar_casas_decimais(numero):
    # Verifica se o número é uma string, se não for, converte-o em string
    numero_str = str(numero)

    # Divide o número em partes inteira e decimal usando o ponto decimal como separador
    partes = numero_str.split('.')

    # Se o número não tiver parte decimal, retorna 0
    if len(partes) == 1:
        return 0

    # Retorna o número de caracteres após o ponto decimal
    return len(partes[1])


def formatar_moeda(valor):
    # Obtém o valor digitado e formata como moeda
    return "{:.2f}".format(valor)


def formatar_preco(entry):
    try:
        valor_atual = entry.get()

        if contar_casas_decimais(valor_atual) < 2:
            # O campo foi apagado, o valor será dividido por 10
            preco_decimal = float(valor_atual) / 10
        else:
            # O campo não está vazio, então continuamos com a formatação normal
            preco_decimal = float(valor_atual) * 10

        preco_formatado = formatar_moeda(preco_decimal)
        entry.delete(0, tk.END)
        entry.insert(0, preco_formatado)

    except ValueError:
        pass

def calcular(*args):
    try:
        preco = preco_var.get()

        # Verifica se o Checkbutton está selecionado (marcado)
        if taxa2_checkbox_var.get() == 1:
            taxa1 = preco * 0.20
            taxa1 = 100 if taxa1 >= 100 else taxa1
        else:
            taxa1 = preco * 0.14
            taxa1 = 100 if taxa1 >= 100 else taxa1

        taxa2 = preco * 0.02

        valor = preco - (taxa1 + taxa2)

        resultado_label.config(
            text=f"Se o produto está sendo vendido por {formatar_moeda(preco)}\nEntão o valor do produto com o lucro é {formatar_moeda(valor)}\n\nValor do Produto:: {formatar_moeda(preco)}\nTaxa de venda e frete grátis: {formatar_moeda(taxa1)}\nTaxa de serviço de transações: {formatar_moeda(taxa2)}")

    except ValueError:
        resultado_label.config(text="Insira apenas números válidos.")

# Criar a janela
janela = tk.Tk()
janela.title("Calculadora de quanto esta sendo vendido")

# Criar as variáveis de controle
preco_var = tk.DoubleVar()
lucro_var = tk.DoubleVar()

# Inicializa as variáveis de controle com o valor "0.00"
preco_var.set(formatar_moeda(0))

# Criar o Checkbutton para adicionar ou não a taxa2
taxa2_checkbox_var = tk.IntVar()
taxa2_checkbox = tk.Checkbutton(
    janela, text="Frete gratis", variable=taxa2_checkbox_var, command=calcular)
taxa2_checkbox.pack()

# Criar os frames para agrupar os widgets do preço e do lucro
frame_preco_label = tk.Frame(janela)
frame_preco_label.pack(pady=5, padx=5)
frame_preco = tk.Frame(janela)
frame_preco.pack(pady=5, padx=5)

# Criar os widgets do preço
preco_label = tk.Label(frame_preco_label, text="Qual valor do produto:")
preco_label.pack(side=tk.LEFT)
preco_label_r = tk.Label(frame_preco, text="R$ ")
preco_label_r.pack(side=tk.LEFT)
preco_entry = tk.Entry(frame_preco, textvariable=preco_var)
preco_entry.pack(side=tk.LEFT)

# Adicionar o evento para atualização automática ao digitar o valor do produto ou lucro
preco_var.trace_add("write", calcular)

# Adicionar o evento para formatar o campo de lucro e preco como uma quantia monetária
preco_entry.bind("<KeyRelease>", lambda event: formatar_preco(preco_entry))

# Adicionar o evento de clique ao Checkbutton para chamar a função calcular
taxa2_checkbox.bind("<Button-1>", calcular)

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Executar a interface gráfica
janela.mainloop()
