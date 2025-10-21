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
top_nav.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

btn_inicio = ctk.CTkButton(
    top_nav, text="início", fg_color="#7aa2ff", hover_color="#84b0ff",
    corner_radius=14, font=ctk.CTkFont(size=16, weight="bold")
)
btn_inicio.grid(row=0, column=0, padx=12, pady=12, sticky="w")

btn_area_livros = ctk.CTkButton(
    top_nav, text="área livros", fg_color="#7aa2ff", hover_color="#84b0ff",
    corner_radius=14, font=ctk.CTkFont(size=16, weight="bold")
)
btn_area_livros.grid(row=0, column=1, padx=12, pady=12)

btn_area_leitores = ctk.CTkButton(
    top_nav, text="área leitores", fg_color="#7aa2ff", hover_color="#84b0ff",
    corner_radius=14, font=ctk.CTkFont(size=16, weight="bold")
)
btn_area_leitores.grid(row=0, column=2, padx=12, pady=12)

btn_area_emprestimos = ctk.CTkButton(
    top_nav, text="área emprestimos", fg_color="#7aa2ff", hover_color="#84b0ff",
    corner_radius=14, font=ctk.CTkFont(size=16, weight="bold")
)
btn_area_emprestimos.grid(row=0, column=3, padx=12, pady=12)

# espaço e avatar
ctk.CTkLabel(top_nav, text="").grid(row=0, column=4)
avatar = ctk.CTkLabel(top_nav, text="", width=42, height=42, corner_radius=21, fg_color="#000000")
avatar.grid(row=0, column=5, padx=12, pady=8, sticky="e")

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
welcome = ctk.CTkLabel(frame_inicio, text="bem vindo ao nosso site", font=ctk.CTkFont(size=56, weight="bold"),
                       text_color="#c0c0c0")
welcome.place(relx=0.5, rely=0.5, anchor="center")

# ---------- Área Livros ----------
frame_livros.grid_rowconfigure(0, weight=1)
frame_livros.grid_columnconfigure(0, weight=1)

# Container principal dos livros
container_livros = ctk.CTkFrame(frame_livros, fg_color="#6b86ff", corner_radius=12)
container_livros.pack(fill="both", expand=True, padx=20, pady=20)
container_livros.grid_rowconfigure(1, weight=1)
container_livros.grid_columnconfigure(0, weight=1)

# Título
titulo_livros = ctk.CTkLabel(container_livros, text="Lista de Livros", 
                            font=ctk.CTkFont(size=24, weight="bold"),
                            fg_color="#d9d9d9", corner_radius=8)
titulo_livros.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 10))

# Área de scroll para lista
scroll_livros = ctk.CTkScrollableFrame(container_livros, fg_color="#ffffff", corner_radius=10)
scroll_livros.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 10))

# Botão adicionar
btn_cadastrar_livro = ctk.CTkButton(container_livros, text="Adicionar Livro", 
                                   fg_color="#ff4d4d", hover_color="#ff3333",
                                   corner_radius=12, font=ctk.CTkFont(size=16, weight="bold"))
btn_cadastrar_livro.grid(row=2, column=0, sticky="w", padx=15, pady=(0, 15))

# ---------- Área Leitores (placeholder funcional) ----------
welcome = ctk.CTkLabel(frame_inicio, text="bem vindo ao nosso site", font=ctk.CTkFont(size=56, weight="bold"),
                       text_color="#c0c0c0")
welcome.place(relx=0.5, rely=0.5, anchor="center")

# ---------- Área Livros ----------
frame_leitores.grid_rowconfigure(0, weight=1)
frame_leitores.grid_columnconfigure(0, weight=1)

# Container principal dos livros
container_leitores = ctk.CTkFrame(frame_leitores, fg_color="#6b86ff", corner_radius=12)
container_leitores.pack(fill="both", expand=True, padx=20, pady=20)
container_leitores.grid_rowconfigure(1, weight=1)
container_leitores.grid_columnconfigure(0, weight=1)

# Título
titulo_leitores = ctk.CTkLabel(container_leitores, text="Lista de leitores", 
                            font=ctk.CTkFont(size=24, weight="bold"),
                            fg_color="#d9d9d9", corner_radius=8)
titulo_leitores.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 10))

# Área de scroll para lista
scroll_leitores = ctk.CTkScrollableFrame(container_leitores, fg_color="#ffffff", corner_radius=10)
scroll_leitores.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 10))

# Botão adicionar
btn_cadastrar_leitor = ctk.CTkButton(container_leitores, text="Adicionar Leitor", 
                                   fg_color="#ff4d4d", hover_color="#ff3333",
                                   corner_radius=12, font=ctk.CTkFont(size=16, weight="bold"))
btn_cadastrar_leitor.grid(row=2, column=0, sticky="w", padx=15, pady=(0, 15))

# ---------- Área Empréstimos ----------
frame_emprestimos.grid_rowconfigure(0, weight=1)
frame_emprestimos.grid_columnconfigure(0, weight=1)

# Container principal dos empréstimos
container_emprestimos = ctk.CTkFrame(frame_emprestimos, fg_color="#6b86ff", corner_radius=12)
container_emprestimos.pack(fill="both", expand=True, padx=20, pady=20)
container_emprestimos.grid_rowconfigure(1, weight=1)
container_emprestimos.grid_columnconfigure(0, weight=1)

# Título
titulo_emprestimos = ctk.CTkLabel(container_emprestimos, text="Lista de Empréstimos", 
                                 font=ctk.CTkFont(size=24, weight="bold"),
                                 fg_color="#d9d9d9", corner_radius=8)
titulo_emprestimos.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 10))

# Área de scroll para lista
scroll_emprestimos = ctk.CTkScrollableFrame(container_emprestimos, fg_color="#ffffff", corner_radius=10)
scroll_emprestimos.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 10))

# Botão adicionar
btn_registrar_emprestimo = ctk.CTkButton(container_emprestimos, text="Registrar Empréstimo", 
                                        fg_color="#ff4d4d", hover_color="#ff3333",
                                        corner_radius=12, font=ctk.CTkFont(size=16, weight="bold"))
btn_registrar_emprestimo.grid(row=2, column=0, sticky="w", padx=15, pady=(0, 15))

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

# ---------- Funções de Leitores ----------
def carregar_leitores():
    # Limpa a lista atual
    for widget in scroll_leitores.winfo_children():
        widget.destroy()
    
    # Adiciona cada leitor na lista
    for leitor in modelo.Leitor.leitores:
        # Frame para cada leitor
        frame_leitor = ctk.CTkFrame(scroll_leitores, fg_color="#88a6ff", corner_radius=8)
        frame_leitor.pack(fill="x", padx=10, pady=5)
        frame_leitor.grid_columnconfigure(0, weight=1)
        
        # Informações do leitor
        info_texto = f"ID: {leitor.id} | Nome: {leitor.nome} | Telefone: {leitor.telefone}"
        label_info = ctk.CTkLabel(frame_leitor, text=info_texto, anchor="w", 
                                 font=ctk.CTkFont(size=12), wraplength=600)
        label_info.grid(row=0, column=0, sticky="w", padx=10, pady=8)
        
        # Botão deletar
        btn_deletar = ctk.CTkButton(frame_leitor, text="Deletar", width=80, height=30,
                                   fg_color="#ff4444", hover_color="#ff2222",
                                   command=lambda id_=leitor.id: deletar_leitor(id_))
        btn_deletar.grid(row=0, column=1, padx=10, pady=8)

def deletar_leitor(id_leitor):
    # Remove o leitor da lista
    for leitor in modelo.Leitor.leitores[:]:
        if str(leitor.id) == str(id_leitor):
            modelo.Leitor.leitores.remove(leitor)
            break
    carregar_leitores()

def abrir_cadastro_leitor():
    popup = ctk.CTkToplevel(app)
    popup.title("Cadastrar Novo Leitor")
    popup.geometry("400x300")
    popup.transient(app)
    popup.grab_set()
    
    # Centralizar popup
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (400 // 2)
    y = (popup.winfo_screenheight() // 2) - (300 // 2)
    popup.geometry(f"400x300+{x}+{y}")
    
    # Título
    titulo = ctk.CTkLabel(popup, text="Cadastrar Leitor", font=ctk.CTkFont(size=20, weight="bold"))
    titulo.pack(pady=20)
    
    # Campos de entrada
    entry_id = ctk.CTkEntry(popup, placeholder_text="ID", width=300)
    entry_id.pack(pady=5)
    
    entry_nome = ctk.CTkEntry(popup, placeholder_text="Nome", width=300)
    entry_nome.pack(pady=5)
    
    entry_telefone = ctk.CTkEntry(popup, placeholder_text="Telefone", width=300)
    entry_telefone.pack(pady=5)
    
    def salvar_leitor():
        id_leitor = entry_id.get().strip()
        nome = entry_nome.get().strip()
        telefone = entry_telefone.get().strip()
            
        if id_leitor and nome:
            modelo.Leitor(id_leitor, nome, telefone)
            carregar_leitores()
            popup.destroy()
    
    # Botões
    frame_botoes = ctk.CTkFrame(popup, fg_color="transparent")
    frame_botoes.pack(pady=20)
    
    btn_salvar = ctk.CTkButton(frame_botoes, text="Salvar", command=salvar_leitor,
                              fg_color="#4CAF50", hover_color="#45a049")
    btn_salvar.pack(side="left", padx=10)
    
    btn_cancelar = ctk.CTkButton(frame_botoes, text="Cancelar", command=popup.destroy,
                                fg_color="#f44336", hover_color="#da190b")
    btn_cancelar.pack(side="left", padx=10)

# Conectar botão
btn_cadastrar_leitor.configure(command=abrir_cadastro_leitor)

# ---------- Funções de Empréstimos ----------
def carregar_emprestimos():
    # Limpa a lista atual
    for widget in scroll_emprestimos.winfo_children():
        widget.destroy()
    
    # Adiciona cada empréstimo na lista
    for emprestimo in modelo.Emprestimo.Emprestimos:
        # Frame para cada empréstimo
        frame_emprestimo = ctk.CTkFrame(scroll_emprestimos, fg_color="#88a6ff", corner_radius=8)
        frame_emprestimo.pack(fill="x", padx=10, pady=5)
        frame_emprestimo.grid_columnconfigure(0, weight=1)
        
        # Informações do empréstimo
        info_texto = f"Livro: {emprestimo.livro.titulo} | Leitor: {emprestimo.leitor.nome} | Empréstimo: {emprestimo.data_emprestimo} | Devolução: {emprestimo.data_devolucao}"
        label_info = ctk.CTkLabel(frame_emprestimo, text=info_texto, anchor="w", 
                                 font=ctk.CTkFont(size=12), wraplength=600)
        label_info.grid(row=0, column=0, sticky="w", padx=10, pady=8)
        
        # Botão deletar
        btn_deletar = ctk.CTkButton(frame_emprestimo, text="Devolver", width=80, height=30,
                                   fg_color="#ff4444", hover_color="#ff2222",
                                   command=lambda emp=emprestimo: deletar_emprestimo(emp))
        btn_deletar.grid(row=0, column=1, padx=10, pady=8)

def deletar_emprestimo(emprestimo):
    # Devolve o livro (aumenta quantidade)
    try:
        emprestimo.livro.qtd_exemplar += 1
    except:
        pass
    
    # Remove o empréstimo da lista
    if emprestimo in modelo.Emprestimo.Emprestimos:
        modelo.Emprestimo.Emprestimos.remove(emprestimo)
    
    carregar_emprestimos()
    carregar_livros()

def abrir_registrar_emprestimo():
    popup = ctk.CTkToplevel(app)
    popup.title("Registrar Empréstimo")
    popup.geometry("450x450")
    popup.transient(app)
    popup.grab_set()
    
    # Centralizar popup
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (450 // 2)
    y = (popup.winfo_screenheight() // 2) - (450 // 2)
    popup.geometry(f"450x450+{x}+{y}")
    
    # Título
    titulo = ctk.CTkLabel(popup, text="Registrar Empréstimo", font=ctk.CTkFont(size=20, weight="bold"))
    titulo.pack(pady=20)
    
    # Seleção de Livro
    label_livro = ctk.CTkLabel(popup, text="Selecione o Livro (ISBN):")
    label_livro.pack(pady=5)
    
    livros_disponiveis = [f"{l.isbn} - {l.titulo}" for l in modelo.Livro.livros if l.qtd_exemplar > 0]
    combo_livro = ctk.CTkComboBox(popup, values=livros_disponiveis if livros_disponiveis else ["Nenhum livro disponível"], width=300)
    combo_livro.pack(pady=5)
    
    # Seleção de Leitor
    label_leitor = ctk.CTkLabel(popup, text="Selecione o Leitor (ID):")
    label_leitor.pack(pady=5)
    
    leitores_lista = [f"{l.id} - {l.nome}" for l in modelo.Leitor.leitores]
    combo_leitor = ctk.CTkComboBox(popup, values=leitores_lista if leitores_lista else ["Nenhum leitor cadastrado"], width=300)
    combo_leitor.pack(pady=5)
    
    # Datas
    entry_data_emp = ctk.CTkEntry(popup, placeholder_text="Data Empréstimo (ex: 2024-01-15)", width=300)
    entry_data_emp.pack(pady=5)
    
    entry_data_dev = ctk.CTkEntry(popup, placeholder_text="Data Devolução (ex: 2024-01-30)", width=300)
    entry_data_dev.pack(pady=5)
    
    def salvar_emprestimo():
        if not livros_disponiveis or not leitores_lista:
            popup.destroy()
            return
            
        # Pega ISBN do livro selecionado
        isbn_selecionado = combo_livro.get().split(" - ")[0]
        livro_selecionado = None
        for l in modelo.Livro.livros:
            if str(l.isbn) == isbn_selecionado:
                livro_selecionado = l
                break
        
        # Pega ID do leitor selecionado
        id_selecionado = combo_leitor.get().split(" - ")[0]
        leitor_selecionado = None
        for l in modelo.Leitor.leitores:
            if str(l.id) == id_selecionado:
                leitor_selecionado = l
                break
        
        data_emp = entry_data_emp.get().strip() or "2024-01-01"
        data_dev = entry_data_dev.get().strip() or "2024-01-15"
        
        if livro_selecionado and leitor_selecionado and livro_selecionado.qtd_exemplar > 0:
            modelo.Emprestimo(data_emp, data_dev, livro_selecionado, leitor_selecionado)
            livro_selecionado.qtd_exemplar -= 1
            carregar_emprestimos()
            carregar_livros()
            popup.destroy()
    
    # Botões
    frame_botoes = ctk.CTkFrame(popup, fg_color="transparent")
    frame_botoes.pack(pady=20)
    
    btn_salvar = ctk.CTkButton(frame_botoes, text="Registrar", command=salvar_emprestimo,
                              fg_color="#4CAF50", hover_color="#45a049")
    btn_salvar.pack(side="left", padx=10)
    
    btn_cancelar = ctk.CTkButton(frame_botoes, text="Cancelar", command=popup.destroy,
                                fg_color="#f44336", hover_color="#da190b")
    btn_cancelar.pack(side="left", padx=10)

# Conectar botão
btn_registrar_emprestimo.configure(command=abrir_registrar_emprestimo)

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

def  set_active_nav(active: str):
    btn_map = {
        "inicio": btn_inicio,
        "livros": btn_area_livros,
        "leitores": btn_area_leitores,
        "emprestimos": btn_area_emprestimos,
    }
    for name, btn in btn_map.items():
        if name == active:
            btn.configure(fg_color="#3f7bff", hover_color="#3f7bff")
        else:
            btn.configure(fg_color="#7aa2ff", hover_color="#84b0ff")

def on_inicio():
    set_active_nav("inicio")
    show_frame("inicio")

def on_area_livros():
    set_active_nav("livros")
    show_frame("livros")

def on_area_leitores():
    set_active_nav("leitores")
    show_frame("leitores")

def on_area_emprestimos():
    set_active_nav("emprestimos")
    show_frame("emprestimos")

btn_inicio.configure(command=on_inicio)
btn_area_livros.configure(command=on_area_livros)
btn_area_leitores.configure(command=on_area_leitores)
btn_area_emprestimos.configure(command=on_area_emprestimos)

# ---------- Carregamento inicial ----------
carregar_livros()
carregar_leitores()
carregar_emprestimos()
set_active_nav("inicio")
show_frame("inicio")

# Loop principal
if __name__ == "__main__":
    app.mainloop()