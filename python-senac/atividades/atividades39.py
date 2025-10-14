import customtkinter as ctk

# Configurações iniciais
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Exercício 4 - Frames e Menu")
janela.geometry("600x400")

# Configurar grid da janela para responsividade
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)  # frame lateral
janela.grid_columnconfigure(1, weight=3)  # frame principal

# Frame lateral (menu)
frame_menu = ctk.CTkFrame(janela, width=150, corner_radius=0)
frame_menu.grid(row=0, column=0, sticky="nsew")

def botao_menu():
    print("Botão do menu clicado!")
def configuracoes():
    print("Configurações clicado!") 
def sobre():
    print("Sobre clicado!")       

# Botões do menu
botao1 = ctk.CTkButton(frame_menu, text="Home", command=botao_menu)
botao1.pack(pady=10, padx=10)

botao2 = ctk.CTkButton(frame_menu, text="Configurações",command=configuracoes)
botao2.pack(pady=10, padx=10)

botao3 = ctk.CTkButton(frame_menu, text="Sobre", command=sobre)
botao3.pack(pady=10, padx=10)

# Frame principal (conteúdo)
frame_conteudo = ctk.CTkFrame(janela)
frame_conteudo.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

# Conteúdo do frame principal
label = ctk.CTkLabel(frame_conteudo, text="Bem-vindo ao painel!")
label.pack(pady=20)

# Loop principal
janela.mainloop()       