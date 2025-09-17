import customtkinter as ctk

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")  

janela = ctk.CTk()
janela.title("Exercício 1 - Janela Básica")
janela.geometry("400x300") 

def ao_clicar():
    print("Você clicou no botão!")

botao = ctk.CTkButton(janela, text="Clique Aqui", command=ao_clicar)
botao.pack(pady=50)  

janela.mainloop()