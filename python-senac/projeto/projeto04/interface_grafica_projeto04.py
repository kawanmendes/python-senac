import sys
import os
from typing import Optional

import customtkinter as ctk

# garante import do módulo projeto04 (não alterar projeto04)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
import projeto04 as modelo  # não alterar este módulo

# Inicialização do tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Janela principal responsiva
app = ctk.CTk()
app.title("Área - Projeto 04")
app.geometry("1200x750")
app.minsize(900, 600)

# Layout principal: coluna 0 = sidebar, coluna 1 = conteúdo
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# ---------- Sidebar (ícone vertical) ----------
sidebar = ctk.CTkFrame(app, width=96, fg_color="#5f7cff", corner_radius=0)
sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)
sidebar.grid_rowconfigure(0, weight=1)

logo_circle = ctk.CTkLabel(sidebar, text="", width=72, height=72, corner_radius=36, fg_color="#2b53d6")
logo_circle.place(relx=0.5, rely=0.06, anchor="n")

# ---------- Top navigation (dentro da área principal) ----------
main_area = ctk.CTkFrame(app, fg_color="transparent")
main_area.grid(row=0, column=1, sticky="nsew", padx=(12, 18), pady=12)
main_area.grid_rowconfigure(1, weight=1)
main_area.grid_columnconfigure(0, weight=1)

top_nav = ctk.CTkFrame(main_area, fg_color="#0f52a0", height=64)
top_nav.grid(row=0, column=0, sticky="ew")
top_nav.grid_propagate(False)
top_nav.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

btn_area_livros = ctk.CTkButton(
    top_nav, text="área livros", fg_color="#7aa2ff", hover_color="#84b0ff",
    corner_radius=14, font=ctk.CTkFont(size=16, weight="bold")
)
btn_area_livros.grid(row=0, column=0, padx=12, pady=12, sticky="w")

btn_area_leitores = ctk.CTkButton(
    top_nav, text="área leitores", fg_color="#7aa2ff", hover_color="#84b0ff",
    corner_radius=14, font=ctk.CTkFont(size=16, weight="bold")
)
btn_area_leitores.grid(row=0, column=1, padx=12, pady=12)

btn_area_emprestimos = ctk.CTkButton(
    top_nav, text="área emprestimos", fg_color="#7aa2ff", hover_color="#84b0ff",
    corner_radius=14, font=ctk.CTkFont(size=16, weight="bold")
)
btn_area_emprestimos.grid(row=0, column=2, padx=12, pady=12)

# espaço e avatar
ctk.CTkLabel(top_nav, text="").grid(row=0, column=3)
avatar = ctk.CTkLabel(top_nav, text="", width=42, height=42, corner_radius=21, fg_color="#000000")
avatar.grid(row=0, column=4, padx=12, pady=8, sticky="e")

# ---------- Content holder e frames por área ----------
content_holder = ctk.CTkFrame(main_area)
content_holder.grid(row=1, column=0, sticky="nsew", pady=(12, 0))
content_holder.grid_rowconfigure(0, weight=1)
content_holder.grid_columnconfigure(0, weight=1)

frame_inicio = ctk.CTkFrame(content_holder)
frame_livros = ctk.CTkFrame(content_holder)
frame_leitores = ctk.CTkFrame(content_holder)
frame_emprestimos = ctk.CTkFrame(content_holder)

for f in (frame_inicio, frame_livros, frame_leitores, frame_emprestimos):
    f.grid(row=0, column=0, sticky="nsew")

# ---------- Helper: cartão grande (bordas e header) ----------
def make_card(parent, title):
    outer = ctk.CTkFrame(parent, fg_color="#6b86ff", corner_radius=12)  # borda roxa
    outer.grid_rowconfigure(0, weight=0)
    outer.grid_rowconfigure(1, weight=1)
    outer.grid_columnconfigure(0, weight=1)
    outer.pack_propagate(False)

    header = ctk.CTkLabel(outer, text=title, font=ctk.CTkFont(size=20, weight="bold"),
                          fg_color="#d9d9d9", corner_radius=8)
    header.grid(row=0, column=0, sticky="ew", padx=18, pady=(14, 6))

    inner = ctk.CTkFrame(outer, fg_color="#ffffff", corner_radius=10)
    inner.grid(row=1, column=0, sticky="nsew", padx=12, pady=(6, 12))
    inner.grid_rowconfigure(0, weight=1)
    inner.grid_columnconfigure(0, weight=1)

    return outer, inner

# ---------- Tela Inicial ----------
welcome = ctk.CTkLabel(frame_inicio, text="bem vindo ao nosso\nsite", font=ctk.CTkFont(size=56, weight="bold"),
                       text_color="#9a9a9a")
welcome.place(relx=0.5, rely=0.5, anchor="center")

# ---------- Área Livros (uso do projeto04) ----------
card_livros, inner_livros = make_card(frame_livros, "lista livros")
# area scroll
scroll_livros = ctk.CTkScrollableFrame(inner_livros, fg_color="#ffffff")
scroll_livros.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
scroll_livros.grid_columnconfigure(0, weight=1)
# actions
acoes_livros = ctk.CTkFrame(inner_livros, fg_color="transparent")
acoes_livros.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 12))
acoes_livros.grid_columnconfigure(0, weight=1)

# cadastrar button (estilo foto)
btn_cadastrar_livro = ctk.CTkButton(
    acoes_livros, text="cadastrar livro", fg_color="#ff4d4d", corner_radius=12,
    font=ctk.CTkFont(size=20, weight="bold")
)
btn_cadastrar_livro.grid(row=0, column=0, sticky="w", padx=(6, 0), pady=6)

# ---------- Área Leitores (placeholder funcional) ----------
card_leitores, inner_leitores = make_card(frame_leitores, "lista leitores")
scroll_leitores = ctk.CTkScrollableFrame(inner_leitores, fg_color="#ffffff")
scroll_leitores.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
scroll_leitores.grid_columnconfigure(0, weight=1)
acoes_leitores = ctk.CTkFrame(inner_leitores, fg_color="transparent")
acoes_leitores.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 12))
acoes_leitores.grid_columnconfigure(0, weight=1)
btn_cadastrar_leitor = ctk.CTkButton(acoes_leitores, text="cadastrar leitor", fg_color="#ff4d4d", corner_radius=12,
                                     font=ctk.CTkFont(size=16, weight="bold"))
btn_cadastrar_leitor.grid(row=0, column=0, sticky="w", padx=(6, 0), pady=6)

# ---------- Área Empréstimos (placeholder funcional) ----------
card_emprestimos, inner_emprestimos = make_card(frame_emprestimos, "lista de empréstimos")
scroll_emprestimos = ctk.CTkScrollableFrame(inner_emprestimos, fg_color="#ffffff")
scroll_emprestimos.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
scroll_emprestimos.grid_columnconfigure(0, weight=1)
acoes_emprestimos = ctk.CTkFrame(inner_emprestimos, fg_color="transparent")
acoes_emprestimos.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 12))
acoes_emprestimos.grid_columnconfigure(0, weight=1)
btn_registrar_emprestimo = ctk.CTkButton(acoes_emprestimos, text="registrar empréstimo", fg_color="#ff4d4d",
                                         corner_radius=12, font=ctk.CTkFont(size=16, weight="bold"))
btn_registrar_emprestimo.grid(row=0, column=0, sticky="w", padx=(6, 0), pady=6)

# ---------- Funções core (livros) ----------
def apagar_livro(isbn: str):
    for l in list(modelo.Livro.livros):
        if str(l.isbn) == str(isbn):
            modelo.Livro.livros.remove(l)
            break
    carregar_livros()

def carregar_livros():
    # limpa
    for w in scroll_livros.winfo_children():
        w.destroy()

    # popula
    for livro in modelo.Livro.livros:
        linha = ctk.CTkFrame(scroll_livros, fg_color="#88a6ff", corner_radius=12)
        linha.grid_columnconfigure(0, weight=1)
        linha.pack(fill="x", pady=12, padx=20)

        texto = f"ISBN: {livro.isbn}, Título: {livro.titulo}, Autores: {livro.autores}, Edição: {livro.edicao}, Quantidade de Exemplares: {livro.qtd_exemplar}"
        lbl = ctk.CTkLabel(linha, text=texto, anchor="w", width=800, wraplength=900)
        lbl.grid(row=0, column=0, sticky="w", padx=(12, 8), pady=12)

        btn_del = ctk.CTkButton(linha, text="X", width=40, fg_color="#ff6060", hover_color="#ff3a3a",
                                corner_radius=12, command=lambda i=livro.isbn: apagar_livro(i))
        btn_del.grid(row=0, column=1, sticky="e", padx=8, pady=8)

# ---------- Popup cadastro livro (estilizado para se assemelhar à imagem) ----------
def abrir_cadastro_livro():
    # cria top-level e camadas (sombra/efeito)
    popup = ctk.CTkToplevel(app)
    popup.transient(app)
    popup.grab_set()
    popup.geometry("420x420")
    popup.title("cadastrar livro")

    # centraliza popup na janela principal
    app.update_idletasks()
    px = app.winfo_rootx() + (app.winfo_width() // 2) - 210
    py = app.winfo_rooty() + (app.winfo_height() // 2) - 210
    popup.geometry(f"+{px}+{py}")

    # camada sombra (escura)
    layer_shadow = ctk.CTkFrame(popup, fg_color="#2b2b2b", corner_radius=12)
    layer_shadow.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    layer_blue = ctk.CTkFrame(popup, fg_color="#0f52a0", corner_radius=12)
    # deslocamento da camada azul
    layer_blue.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.96)

    inner = ctk.CTkFrame(popup, fg_color="#ffffff", corner_radius=10)
    inner.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

    # título
    lbl_title = ctk.CTkLabel(inner, text="cadastrar livro", font=ctk.CTkFont(size=20, weight="bold"))
    lbl_title.grid(row=0, column=0, pady=(12, 6))

    # entradas estilizadas (cinza claro como na imagem)
    e_isbn = ctk.CTkEntry(inner, placeholder_text="isbn do livro:", fg_color="#dcdcdc", height=36)
    e_isbn.grid(row=1, column=0, sticky="ew", padx=24, pady=(8, 6))
    e_titulo = ctk.CTkEntry(inner, placeholder_text="titulo do livro:", fg_color="#dcdcdc", height=36)
    e_titulo.grid(row=2, column=0, sticky="ew", padx=24, pady=6)
    e_autores = ctk.CTkEntry(inner, placeholder_text="autores do livro:", fg_color="#dcdcdc", height=36)
    e_autores.grid(row=3, column=0, sticky="ew", padx=24, pady=6)
    e_edicao = ctk.CTkEntry(inner, placeholder_text="edicao do livro:", fg_color="#dcdcdc", height=36)
    e_edicao.grid(row=4, column=0, sticky="ew", padx=24, pady=6)
    e_qtd = ctk.CTkEntry(inner, placeholder_text="qtd_exemplar do livro:", fg_color="#dcdcdc", height=36)
    e_qtd.grid(row=5, column=0, sticky="ew", padx=24, pady=6)

    # botão finalizar (vermelho estilo foto) no canto inferior direito
    def confirmar():
        isbn = e_isbn.get().strip() or None
        titulo = e_titulo.get().strip() or "Sem título"
        autores = e_autores.get().strip() or "Desconhecido"
        edicao = e_edicao.get().strip() or "N/A"
        try:
            qtd = int(e_qtd.get().strip()) if e_qtd.get().strip() else 1
        except Exception:
            qtd = 1
        # cria livro usando modelo (não altera projeto04)
        modelo.Livro(isbn, titulo, autores, edicao, qtd)
        carregar_livros()
        popup.destroy()

    btn_finish = ctk.CTkButton(inner, text="finalizar", command=confirmar, fg_color="#ff4d4d",
                               corner_radius=12, font=ctk.CTkFont(size=18, weight="bold"))
    btn_finish.grid(row=6, column=0, sticky="e", padx=24, pady=(12, 18))

# conecta botão cadastrar ao popup
btn_cadastrar_livro.configure(command=abrir_cadastro_livro)

# ---------- Funções leitores / empréstimos (reaproveitando projeto04) ----------
def apagar_leitor(id_):
    for l in list(modelo.Leitor.leitores):
        if l.id == id_:
            modelo.Leitor.leitores.remove(l)
            break
    carregar_leitores()

def carregar_leitores():
    for w in scroll_leitores.winfo_children():
        w.destroy()
    for leitor in modelo.Leitor.leitores:
        linha = ctk.CTkFrame(scroll_leitores, fg_color="#88a6ff", corner_radius=8)
        linha.grid_columnconfigure(0, weight=1)
        linha.pack(fill="x", pady=8, padx=12)

        texto = f"ID: {leitor.id}, Nome: {leitor.nome}, Telefone: {leitor.telefone}"
        lbl = ctk.CTkLabel(linha, text=texto, anchor="w", wraplength=900)
        lbl.grid(row=0, column=0, sticky="w", padx=(12, 8), pady=8)

        btn_del = ctk.CTkButton(linha, text="X", width=40, fg_color="#ff6060", hover_color="#ff3a3a",
                                corner_radius=12, command=lambda i=leitor.id: apagar_leitor(i))
        btn_del.grid(row=0, column=1, sticky="e", padx=8, pady=8)

def apagar_emprestimo(emp):
    try:
        emp.livro.qtd_exemplar += 1
    except Exception:
        pass
    if emp in modelo.Emprestimo.Emprestimos:
        modelo.Emprestimo.Emprestimos.remove(emp)
    carregar_emprestimos()
    carregar_livros()

def carregar_emprestimos():
    for w in scroll_emprestimos.winfo_children():
        w.destroy()
    for emp in modelo.Emprestimo.Emprestimos:
        linha = ctk.CTkFrame(scroll_emprestimos, fg_color="#88a6ff", corner_radius=8)
        linha.grid_columnconfigure(0, weight=1)
        linha.pack(fill="x", pady=8, padx=12)

        texto = f"{emp}"
        lbl = ctk.CTkLabel(linha, text=texto, anchor="w", wraplength=900)
        lbl.grid(row=0, column=0, sticky="w", padx=(12, 8), pady=8)

        btn_del = ctk.CTkButton(linha, text="X", width=40, fg_color="#ff6060", hover_color="#ff3a3a",
                                corner_radius=12, command=lambda e=emp: apagar_emprestimo(e))
        btn_del.grid(row=0, column=1, sticky="e", padx=8, pady=8)

# ---------- Navegação entre frames e comportamento dos botões ----------
def show_frame(frame_name: str):
    mapping = {
        "inicio": frame_inicio,
        "livros": frame_livros,
        "leitores": frame_leitores,
        "emprestimos": frame_emprestimos,
    }

    # recarrega dados conforme necessário
    if frame_name == "livros":
        carregar_livros()
    elif frame_name == "leitores":
        carregar_leitores()
    elif frame_name == "emprestimos":
        carregar_emprestimos()

    # oculta todos e mostra só o solicitado
    for name, fr in mapping.items():
        if name == frame_name:
            fr.lift()
        else:
            fr.lower()

def set_active_nav(active: str):
    btn_map = {
        "livros": btn_area_livros,
        "leitores": btn_area_leitores,
        "emprestimos": btn_area_emprestimos,
    }
    for name, btn in btn_map.items():
        if name == active:
            btn.configure(fg_color="#3f7bff", hover_color="#3f7bff")
        else:
            btn.configure(fg_color="#7aa2ff", hover_color="#84b0ff")

def on_area_livros():
    set_active_nav("livros")
    show_frame("livros")

def on_area_leitores():
    set_active_nav("leitores")
    show_frame("leitores")

def on_area_emprestimos():
    set_active_nav("emprestimos")
    show_frame("emprestimos")

btn_area_livros.configure(command=on_area_livros)
btn_area_leitores.configure(command=on_area_leitores)
btn_area_emprestimos.configure(command=on_area_emprestimos)

# ---------- Carregamento inicial ----------
carregar_livros()
carregar_leitores()
carregar_emprestimos()
set_active_nav("livros")
show_frame("livros")

# Loop principal
if __name__ == "__main__":
    app.mainloop()