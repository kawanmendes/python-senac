import customtkinter as ctk
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Exercício 1 - Janela Básica")
janela.geometry("400x300")

def botao_branco():
    ctk.set_appearance_mode("light")
def botao_preto():
    ctk.set_appearance_mode("dark") 
botao_branco = ctk.CTkButton(janela, text="Branco", command=botao_branco)
botao_branco.pack(pady=10)
botao_preto = ctk.CTkButton(janela, text="Preto", command=botao_preto)
botao_preto.pack(pady=10)

janela.mainloop()