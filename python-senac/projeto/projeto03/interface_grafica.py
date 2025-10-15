import customtkinter as ctk

# Aparência e tema
ctk.set_appearance_mode("dark")  # Define modo escuro
ctk.set_default_color_theme("blue")  # Define tema azul

# Janela principal
app = ctk.CTk()
app.geometry("600x400")
app.title("Atividades Pendentes")

# Coluna: Lista de tarefas
# Armazena as tarefas e seu status
tarefas = [
    {"nome": "estudar html", "feito": True},
    {"nome": "estudar css", "feito": False},
    {"nome": "estudar javascript", "feito": True},
]

# Coluna: Atualização visual da lista
# Atualiza a exibição das tarefas e seus botões
def atualizar_lista():
    for widget in lista_frame.winfo_children():
        widget.destroy()

    for i, tarefa in enumerate(tarefas):
        linha = ctk.CTkFrame(lista_frame)
        linha.pack(fill="x", pady=5, padx=5)

        nome_label = ctk.CTkLabel(linha, text=tarefa["nome"])
        nome_label.pack(side="left", padx=10)

        status = "✅" if tarefa["feito"] else "❌"
        botao_status = ctk.CTkButton(
             fg_color="#778EA5" if tarefa["feito"] else "#708090",
            master=linha, text=status, width=40,
            command=lambda i=i: alternar_status(i)
        )
        botao_status.pack(side="right", padx=10)

        botao_apagar = ctk.CTkButton(
            fg_color="#A71D1D",
            master=linha, text="🗑️", width=40,
            command=lambda i=i: apaguar_tarefa(i)
        )
        botao_apagar.pack(side="right", padx=10)

# Coluna: Alternar status
# Alterna entre feito e não feito
def alternar_status(index):
    tarefas[index]["feito"] = not tarefas[index]["feito"]
    atualizar_lista()

# Coluna: Apagar tarefa
# Remove a tarefa da lista
def apaguar_tarefa(index):
    del tarefas[index]
    atualizar_lista()    

# Coluna: Adicionar tarefa
# Adiciona uma nova tarefa à lista
def adicionar_tarefa():
    nome = entrada.get()
    if nome.strip():
        tarefas.append({"nome": nome.strip(), "feito": False})
        entrada.delete(0, "end")
        atualizar_lista()

# Coluna: Layout principal
main_frame = ctk.CTkFrame(app)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Coluna: Frame da lista de tarefas
lista_frame = ctk.CTkScrollableFrame(main_frame, label_text="atividades pendentes")
lista_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Coluna: Frame de entrada de nova tarefa
entrada_frame = ctk.CTkFrame(main_frame)
entrada_frame.pack(side="right", fill="y", padx=10, pady=10)

entrada_label = ctk.CTkLabel(entrada_frame, text="atividades pendentes")
entrada_label.pack(pady=(10, 5))

entrada = ctk.CTkEntry(entrada_frame, placeholder_text="insira o nome da matéria")
entrada.pack(pady=10)

botao_add = ctk.CTkButton(entrada_frame, text="✔", width=40, command=adicionar_tarefa, fg_color="#778EA5")
botao_add.pack(pady=10)

# Coluna: Inicialização da lista visual
atualizar_lista()

# Coluna: Loop principal da interface
app.mainloop()


