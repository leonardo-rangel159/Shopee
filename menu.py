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

def calcular1(*args):
    try:
        global preco_var, lucro_var, taxa2_checkbox_var, resultado_label
        preco = preco_var.get()
        lucro = lucro_var.get()

       # Verifica se o Checkbutton está selecionado (marcado)
        if taxa2_checkbox_var.get() == 1:
            taxa1 = (preco+lucro) * 0.20
            taxa1 = 100 if taxa1 >= 100 else taxa1
        else:
            taxa1 = (preco+lucro) * 0.14
            taxa1 = 100 if taxa1 >= 100 else taxa1

        taxa2 = preco * 0.02

        preco_total = preco + lucro + taxa1 + taxa2

        resultado_label.config(
            text=f"Se comprou o produto por {formatar_moeda(preco)}\nEntão terá que vender por {formatar_moeda(preco_total)}\n\nPreço: {formatar_moeda(preco)}\nLucro: {formatar_moeda(lucro)}\nTaxa de venda e frete grátis: {formatar_moeda(taxa1)}\nTaxa de serviço de transações: {formatar_moeda(taxa2)}")

    except ValueError:
        resultado_label.config(text="Insira apenas números válidos.")

def calcular2(*args):
    try:
        global preco_var, taxa2_checkbox_var, resultado_label
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

def criar_janela1():
    global janela1, preco_var, lucro_var, taxa2_checkbox_var, resultado_label
    janela.destroy()

    # Cria uma nova janela
    janela1 = tk.Tk()
    janela1.title("Shopee")

    # Adicione widgets e configurações específicas da nova janela aqui
    label = tk.Label(janela1, text="Cacular por quanto vender")
    label.pack()

    # Criar as variáveis de controle
    preco_var = tk.DoubleVar()
    lucro_var = tk.DoubleVar()

    # Inicializa as variáveis de controle com o valor "0.00"
    preco_var.set(formatar_moeda(0))
    lucro_var.set(formatar_moeda(0))

    # Criar o Checkbutton para adicionar ou não a taxa2
    taxa2_checkbox_var = tk.IntVar()
    taxa2_checkbox = tk.Checkbutton(
        janela1, text="Adicionar Taxa2", variable=taxa2_checkbox_var, command=calcular1) 
    taxa2_checkbox.pack()

    # Criar os frames para agrupar os widgets do preço e do lucro
    frame_preco_label = tk.Frame(janela1)
    frame_preco_label.pack(pady=5, padx=5)
    frame_preco = tk.Frame(janela1)
    frame_preco.pack(pady=5, padx=5)
    frame_lucro_label = tk.Frame(janela1)
    frame_lucro_label.pack(pady=5, padx=5)
    frame_lucro = tk.Frame(janela1)
    frame_lucro.pack(pady=5, padx=5)

    # Criar os widgets do preço
    preco_label = tk.Label(
        frame_preco_label, text="Qual valor você pagará pelo produto:")
    preco_label.pack(side=tk.LEFT)
    preco_label_r = tk.Label(frame_preco, text="R$ ")
    preco_label_r.pack(side=tk.LEFT)
    preco_entry = tk.Entry(frame_preco, textvariable=preco_var)
    preco_entry.pack(side=tk.LEFT)

    # Criar os widgets do lucro
    lucro_label = tk.Label(
        frame_lucro_label, text="Quanto deseja ganhar de lucro em cima do produto:")
    lucro_label.pack(side=tk.LEFT)
    lucro_label_r = tk.Label(frame_lucro, text="R$ ")
    lucro_label_r.pack(side=tk.LEFT)
    lucro_entry = tk.Entry(frame_lucro, textvariable=lucro_var)
    lucro_entry.pack(side=tk.LEFT)

    # Adicionar o evento para atualização automática ao digitar o valor do produto ou lucro
    preco_var.trace_add("write", calcular1)
    lucro_var.trace_add("write", calcular1)

    # Adicionar o evento para formatar o campo de lucro e preco como uma quantia monetária
    preco_entry.bind("<KeyRelease>", lambda event: formatar_preco(preco_entry))
    lucro_entry.bind("<KeyRelease>", lambda event: formatar_preco(lucro_entry))

    # Adicionar o evento de clique ao Checkbutton para chamar a função calcular
    taxa2_checkbox.bind("<Button-1>", calcular1)

    resultado_label = tk.Label(janela1, text="")
    resultado_label.pack()

    # Botão para voltar à janela principal
    btn_voltar = tk.Button(
        janela1, text="Voltar para Janela Principal", command=lambda:voltar_janela_principal(1))
    btn_voltar.pack(pady=5)

def criar_janela2():
    janela.destroy()  # Destroi a janela atual
    global janela2, preco_var, taxa2_checkbox_var, resultado_label

    # Cria uma nova janela
    janela2 = tk.Tk()
    janela2.title("Shoppe")

    # Adicione widgets e configurações específicas da nova janela aqui
    label = tk.Label(janela2, text="Cacular por quanto estão vendendo")
    label.pack()

    # Criar as variáveis de controle
    preco_var = tk.DoubleVar()

    # Inicializa as variáveis de controle com o valor "0.00"
    preco_var.set(formatar_moeda(0))

    # Criar o Checkbutton para adicionar ou não a taxa2
    taxa2_checkbox_var = tk.IntVar()
    taxa2_checkbox = tk.Checkbutton(
        janela2, text="Frete gratis", variable=taxa2_checkbox_var, command=calcular2) 
    taxa2_checkbox.pack()

    # Criar os frames para agrupar os widgets do preço e do lucro
    frame_preco_label = tk.Frame(janela2)
    frame_preco_label.pack(pady=5, padx=5)
    frame_preco = tk.Frame(janela2)
    frame_preco.pack(pady=5, padx=5)

    # Criar os widgets do preço
    preco_label = tk.Label(frame_preco_label, text="Qual valor do produto:")
    preco_label.pack(side=tk.LEFT)
    preco_label_r = tk.Label(frame_preco, text="R$ ")
    preco_label_r.pack(side=tk.LEFT)
    preco_entry = tk.Entry(frame_preco, textvariable=preco_var)
    preco_entry.pack(side=tk.LEFT)

    # Adicionar o evento para atualização automática ao digitar o valor do produto ou lucro
    preco_var.trace_add("write", calcular2)

    # Adicionar o evento para formatar o campo de lucro e preco como uma quantia monetária
    preco_entry.bind("<KeyRelease>", lambda event: formatar_preco(preco_entry))

    # Adicionar o evento de clique ao Checkbutton para chamar a função calcular
    taxa2_checkbox.bind("<Button-1>", calcular2)

    resultado_label = tk.Label(janela2, text="")
    resultado_label.pack()

    # Botão para voltar à janela principal
    btn_voltar = tk.Button(
        janela2, text="Voltar", command=lambda: voltar_janela_principal(2))
    btn_voltar.pack(pady=5)

def voltar_janela_principal(valor):
    # Destroi a janela atual
    if (valor == 1):
        janela1.destroy()
    else:
        janela2.destroy()

    # Cria uma nova janela principal
    criar_janela_principal()

def criar_janela_principal():
    global janela
    janela = tk.Tk()
    janela.title("Shopee")

    # Largura: 800 pixels, Altura: 600 pixels, Posição inicial: (100, 100)
    janela.geometry("400x120+100+100")

    # Janela não redimensionável em nenhum eixo (horizontal e vertical)
    janela.resizable(False, False)

    # Botões para abrir as janelas 1 e 2
    btn_janela1 = tk.Button(
        janela, text="Cacular por quanto vender", command=criar_janela1)
    btn_janela1.pack(pady=10)

    btn_janela2 = tk.Button(
        janela, text="Saber por quanto estão vendendo", command=criar_janela2)
    btn_janela2.pack(pady=10)

# Iniciar com a janela principal
criar_janela_principal()

# Executar a interface gráfica
janela.mainloop()
