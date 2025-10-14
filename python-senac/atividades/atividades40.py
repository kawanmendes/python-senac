import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


janela = ctk.CTk()
janela.title("Exercício 1 - Frames e Menu")
janela.geometry("600x400")


entrada = ctk.CTkEntry(janela, width=250)
entrada.grid(row=0, column=1, sticky="n", padx=70)

janela.grid_rowconfigure(1, weight=0)
janela.grid_columnconfigure(1, weight=1)

botao = ctk.CTkButton(janela, text="Enviar", width=100, fg_color="#018D8D",
    hover_color="#027448",
    text_color="white")
botao.grid(row=3, column=1, sticky="n", padx=40)

botao.grid_rowconfigure(1, weight=1)
botao.grid_columnconfigure(1, weight=1)

escrita = ctk.CTkTextbox(janela, width=500, height=100)
escrita.grid(row=16, column=1, sticky="n", padx=10)
escrita.grid_rowconfigure(6, weight=3)
escrita.grid_columnconfigure(0, weight=1)

def enviar():
    texto = entrada.get()
    escrita.insert("end", "Texto enviado: " + texto + "\n")
    entrada.delete(0, "end")

botao.configure(command=enviar)

janela.mainloop()