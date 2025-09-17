import customtkinter as ctk

# Configurações iniciais
ctk.set_appearance_mode("light")  # light, dark ou system
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Exercício 3 - Login")
janela.geometry("400x200")  # largura x altura


# Label e Entry para usuário
label_usuario = ctk.CTkLabel(janela, text="Usuário:")
label_usuario.grid(row=0, column=0, sticky="w", padx=20)    

entrada_usuario = ctk.CTkEntry(janela)
entrada_usuario.grid(row=0, column=0, sticky="e", padx=20)

# Label e Entry para senha
label_senha = ctk.CTkLabel(janela, text="Senha:")
label_senha.grid(row=1, column=0, sticky="w", padx=20)

entrada_senha = ctk.CTkEntry(janela, show="*")  # oculta caracteres
entrada_senha.grid(row=1, column=0, sticky="e", padx=20)

# Função chamada ao clicar no botão
def entrar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    print(f"Usuário: {usuario}, Senha: {senha}")

# Botão Entrar
botao_entrar = ctk.CTkButton(janela, text="Entrar", command=entrar)
botao_entrar.grid(row=2, column=0, pady=20)

# Loop principal
janela.mainloop()