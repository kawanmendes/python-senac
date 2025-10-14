import customtkinter as ctk

# Inicializações
ctk.set_appearance_mode("dark")  # ou "light"
ctk.set_default_color_theme("blue")

# Criando janela principal
app = ctk.CTk()
app.geometry("600x400")
app.title("Atividades Pendentes")

# Lista inicial de tarefas
tarefas = [
    {"nome": "estudar html", "feito": True},
    {"nome": "estudar css", "feito": False},
    {"nome": "estudar javascript", "feito": True},
]

# Função para atualizar a lista de tarefas
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
            master=
            linha, text=status, width=40,
            command=lambda i=i: alternar_status(i)
        )
        botao_status.pack(side="right", padx=10)

# Alternar entre feito e não feito
def alternar_status(index):
    tarefas[index]["feito"] = not tarefas[index]["feito"]
    atualizar_lista()

# Adicionar nova tarefa
def adicionar_tarefa():
    nome = entrada.get()
    if nome.strip():
        tarefas.append({"nome": nome.strip(), "feito": False})
        entrada.delete(0, "end")
        atualizar_lista()

# Layout principal
main_frame = ctk.CTkFrame(app)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Parte esquerda: lista de tarefas
lista_frame = ctk.CTkScrollableFrame(main_frame, label_text="atividades pendentes")
lista_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Parte direita: adicionar nova tarefa
entrada_frame = ctk.CTkFrame(main_frame)
entrada_frame.pack(side="right", fill="y", padx=10, pady=10)

entrada_label = ctk.CTkLabel(entrada_frame, text="atividades pendentes")
entrada_label.pack(pady=(10, 5))

entrada = ctk.CTkEntry(entrada_frame, placeholder_text="insira o nome da matéria")
entrada.pack(pady=10)

botao_add = ctk.CTkButton(entrada_frame, text="✔", width=40, command=adicionar_tarefa, fg_color="#778EA5")
botao_add.pack(pady=10)

# Carrega lista inicial
atualizar_lista()

# Loop principal
app.mainloop()


