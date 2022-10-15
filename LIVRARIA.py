from tkinter import *
from tkinter.ttk import Style, Treeview
from tkinter import messagebox
from matplotlib import style
import pymysql
import pybase64


amarelo='#ffdd00'
cinza='#D9D9D9'
preto='#000000'
branco='#ffffff'


class livraria:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('1280x720')
        self.janela.title('Livraria')
        self.janela.resizable(width=False, height=False)
        self.janela.config(bg=amarelo)

        self.frame0 = Frame(self.janela, bg=amarelo)
        self.frame0.place(x=0, y=0, w=1280, h=720)

    def login(self):
        # frames
        self.frame_login = Frame(self.frame0, bg=branco)
        self.frame_login.place(x=390, y=100, w=500, h=520)

        self.frame_ir_cadastro = Frame(self.frame_login, bg=cinza)
        self.frame_ir_cadastro.place(x=0, y=471, w=500, h= 50)

        self.frame_linha = Frame(self.frame_login, bg=amarelo)
        self.frame_linha.place(x=50, y=191, w=405, h=2)

        self.frame_linha2 = Frame(self.frame_login, bg=amarelo)
        self.frame_linha2.place(x=50, y=276, w=405, h=2)

        self.frame_linha3 = Frame(self.frame_login, bg=amarelo)
        self.frame_linha3.place(x=174, y=343, w=3, h=60)

        self.frame_linha4 = Frame(self.frame_login, bg=amarelo)
        self.frame_linha4.place(x=317, y=343, w=3, h=60)

        self.frame_linha5 = Frame(self.frame_login, bg=amarelo)
        self.frame_linha5.place(x=174, y=342, w=146, h=3)

        self.frame_linha6 = Frame(self.frame_login, bg=amarelo)
        self.frame_linha6.place(x=174, y=401, w=146, h=3)

        # texto
        self.text1 = Label(self.frame_login, text='Bem Vindo!', font='Inter 34', bg=branco, fg=preto)
        self.text1.place(x=71, y=26)

        self.text2 = Label(self.frame_login, text='CPF', font='Inter 15', bg=branco, fg=preto)
        self.text2.place(x=50, y=127)

        self.text3 = Label(self.frame_login, text='Senha', font='Inter 15', bg=branco, fg=preto)
        self.text3.place(x=50, y=215)

        self.text4 = Label(self.frame_ir_cadastro, text='Primeiro acesso?', font='Inter 16', bg=cinza, fg=preto)
        self.text4.place(x=32, y=10)

        # entry
        self.entrada_cpf = Entry(self.frame_login, bg=branco, fg=preto, font='inter 15', borderwidth=0)
        self.entrada_cpf.place(x=55, y=160, w=392, h=30)

        self.entrada_senha = Entry(self.frame_login, bg=branco, fg=preto, font='inter 15', borderwidth=0, show='*')
        self.entrada_senha.place(x=55, y=245, w=392, h=30)

        # botões
        self.botao_login = Button(self.frame_login, text='Login', bg=branco, font='inter 15', borderwidth=3, relief=FLAT, command=self.login_adm)
        self.botao_login.place(x=177, y=345, w=140, h=56)

        self.botao__ir_tela_cadastro = Button(self.frame_ir_cadastro, text='Cadastrar-se', relief=FLAT,bg=cinza, font='inter 16', command=self.ir_tela_cadastro)
        self.botao__ir_tela_cadastro.place(x=200, y=3)

    def cadastro(self):
        # frames
        self.frame_cadastro = Frame(self.frame0, bg=branco)
        self.frame_cadastro.place(x=390, y=100, w=500, h=520)

        self.frame_linha = Frame(self.frame_cadastro, bg=amarelo)
        self.frame_linha.place(x=50, y=171, w=405, h=2)

        self.frame_linha1 = Frame(self.frame_cadastro, bg=amarelo)
        self.frame_linha1.place(x=50, y=256, w=405, h=2)

        self.frame_linha2 = Frame(self.frame_cadastro, bg=amarelo)
        self.frame_linha2.place(x=50, y=341, w=405, h=2)

        self.frame_linha_borda_botao = Frame(self.frame_cadastro, bg=amarelo)
        self.frame_linha_borda_botao.place(x=174, y=385, w=3, h=60)

        self.frame_linha_borda_botao1 = Frame(self.frame_cadastro, bg=amarelo)
        self.frame_linha_borda_botao1.place(x=317, y=385, w=3, h=60)

        self.frame_linha_borda_botao2 = Frame(self.frame_cadastro, bg=amarelo)
        self.frame_linha_borda_botao2.place(x=174, y=382, w=146, h=3)

        self.frame_linha_borda_botao3 = Frame(self.frame_cadastro, bg=amarelo)
        self.frame_linha_borda_botao3.place(x=174, y=442, w=146, h=3)

        self.frame_voltar_login = Frame(self.frame_cadastro, bg=cinza)
        self.frame_voltar_login.place(x=0, y=476, w=500, h= 45)

        # texto
        self.text1 = Label(self.frame_cadastro, text='Cadastrar', font='Inter 34', bg=branco, fg=preto)
        self.text1.place(x=71, y=26)

        self.text2 = Label(self.frame_cadastro, text='Nome', font='Inter 15', bg=branco, fg=preto)
        self.text2.place(x=50, y=107)

        self.text2 = Label(self.frame_cadastro, text='CPF', font='Inter 15', bg=branco, fg=preto)
        self.text2.place(x=50, y=195)

        self.text2 = Label(self.frame_cadastro, text='Senha', font='Inter 15', bg=branco, fg=preto)
        self.text2.place(x=50, y=283)

        # entry
        self.entry_nome = Entry(self.frame_cadastro, bg=branco, fg=preto, font='inter 15', borderwidth=0)
        self.entry_nome.place(x=55, y=140, w=392, h=30)

        self.entry_email = Entry(self.frame_cadastro, bg=branco, fg=preto, font='inter 15', borderwidth=0)
        self.entry_email.place(x=55, y=225, w=392, h=30)

        self.entry_senha = Entry(self.frame_cadastro, bg=branco, fg=preto, font='inter 15', borderwidth=0, show='*')
        self.entry_senha.place(x=55, y=310, w=392, h=30)

        #imagem
        self.imagem_voltar_b64 = PhotoImage(data=pybase64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAQAAACROWYpAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAADmQAAA5kASIwoxwAAAAHdElNRQfmBxUQIyk5E2X/AAABcUlEQVQ4y92Tu08CQRCHP0AFE+ILChJR46MwxAidDZUNUSttbCyN2ttSSiwMiX+EJnbGxsICGyPGxPiAoIUPGhOJD6Ik+AquDXfs4XHe0elvmt2dfDOzO7Pwr+TEg60+NMQGKeatg83McYNAcESbNXSQNT4QCARpvObBJma4KIMCQYoOY8ChrnpZJopP8jXgI4ifRoq8G4WY4lTKKVuJR/aIMqT/+p2sUqiBVuyWOP3V6ATJX0HFMkxLFwVyplGBoEAUVwU+sQQLPonRpDzVLm4C2mIMZWeEFw6UrYtZri1lv2dUjhdkk5IFPEF7ZUhybJNnGLcU8I0srziUG2rUzSXH2qMwCSn6OQH6CLPAOlmd3K3VEb0skVc/hkedwAEWOdPAz0R+FmRjjEMEgiQtGo+fGE8SHtdvRxcr7DCp4xkno8L7tbppw1nDEyrXJbgzPRuatqYRCKNvaqQIDwi+zI+lrCuK9LBVX2aw49Udnr+gb0Y//MctN4yqAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIyLTA3LTIxVDE2OjM1OjIzKzAwOjAwI0qrYQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMi0wNy0yMVQxNjozNToyMyswMDowMFIXE90AAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAAElFTkSuQmCC'))


        # botoes
        self.botao_cadastrar = Button(self.frame_cadastro, text='Cadastrar', bg=branco, font='inter 15', borderwidth=3, relief=FLAT, command=self.cadastrar_adm)
        self.botao_cadastrar.place(x=177, y=385, w=140, h=56)

        self.botao__ir_tela_login = Button(self.frame_voltar_login, text='Voltar', relief=FLAT,bg=cinza, font='inter 16', command=self.ir_tela_login)
        self.botao__ir_tela_login.place(x=60, y=0)

        self.botao__ir_tela_login_img = Button(self.frame_voltar_login, image=self.imagem_voltar_b64, relief=FLAT,bg=cinza, font='inter 16', command=self.ir_tela_login)
        self.botao__ir_tela_login_img.place(x=25, y=5)

    def menu_principal(self):
        # frames
        self.frame_menus = Frame(self.frame0, bg=branco)
        self.frame_menus.place(x=0, y=0, w=300, h=720)

        self.frame_linha1 = Frame(self.frame_menus, bg=preto)
        self.frame_linha1.place(x=0, y=250, w=300, h=1)

        self.frame_linha2 = Frame(self.frame_menus, bg=preto)
        self.frame_linha2.place(x=0, y=314, w=300, h=1)
        
        self.frame_linha3 = Frame(self.frame_menus, bg=preto)
        self.frame_linha3.place(x=0, y=380, w=300, h=1)

        self.frame_linha4 = Frame(self.frame_menus, bg=preto)
        self.frame_linha4.place(x=0, y=445, w=300, h=1)

        self.frame_linha5 = Frame(self.frame_menus, bg=preto)
        self.frame_linha5.place(x=0, y=511, w=300, h=1)

        self.frame_linha6 = Frame(self.frame_menus, bg=preto)
        self.frame_linha6.place(x=0, y=577, w=300, h=1)

        #textos
        self.text1_adm = Label(self.frame_menus, text='Administrador', font='inter 15', bg=branco)
        self.text1_adm.place(x=90, y=63)

        #imagem
        self.imagem1_b64 = PhotoImage(data=pybase64.b64decode('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'))
        self.imagem1 = Label(self.frame_menus, image=self.imagem1_b64, bg=branco)
        self.imagem1.place(x=100, y=120, w=100, h=100)

        self.imagem_sair_b64 = PhotoImage(data=pybase64.b64decode('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'))

        # botões
        self.botao_livros_disponiveis = Button(self.frame_menus, text='Livros Disponíveis', relief=FLAT, bg=branco, fg=preto, font='inter 15', command=self.livros_disponiveis)
        self.botao_livros_disponiveis.place(x=1, y=251, w=300, h=63)

        self.botao_cadastrar_livros = Button(self.frame_menus, text='Cadastrar Livros', relief=FLAT, bg=branco, fg=preto, font='inter 15', command=self.cadastrar_livros)
        self.botao_cadastrar_livros.place(x=1, y=315, w=300, h=64)

        self.botao_fornecedores = Button(self.frame_menus, text='Cadastrar Fornecedores', relief=FLAT, bg=branco, fg=preto, font='inter 15', command=self.cadastrar_fornecedores)
        self.botao_fornecedores.place(x=1, y=381, w=300, h=64)

        self.botao_fornecedores = Button(self.frame_menus, text='Fornecedores', relief=FLAT, bg=branco, fg=preto, font='inter 15', command=self.ver_fornecedores)
        self.botao_fornecedores.place(x=1, y=446, w=300, h=64)

        self.botao_clientes = Button(self.frame_menus, text='Clientes', relief=FLAT, bg=branco, fg=preto, font='inter 15', command=self.clientes_vendas)
        self.botao_clientes.place(x=1, y=512, w=300, h=64)

        self.botao_compras = Button(self.frame_menus, text='Compras', relief=FLAT, bg=branco, fg=preto, font='inter 15')
        self.botao_compras.place(x=1, y=578, w=300, h=64)

        self.botao_sair = Button(self.frame_menus, text='Sair', relief=FLAT, bg=branco, fg=preto, font='inter 15', command=self.ir_tela_login)
        self.botao_sair.place(x=65, y=665)

        self.botao_sair_img = Button(self.frame_menus, image=self.imagem_sair_b64, relief=FLAT, bg=branco, fg=preto, font='inter 15', command=self.ir_tela_login)
        self.botao_sair_img.place(x=22, y=660)
        
    def livros_disponiveis(self):
        self.limprar_janela()
        self.menu_principal()

        self.frame_livros_disponiveis_0 = Frame(self.frame0, bg=amarelo)
        self.frame_livros_disponiveis_0.place(x=300, y=0, w=980, h=720)

        #treeview
        global dados
        self.treeview_livros_disponiveis = Treeview(self.frame_livros_disponiveis_0, columns=('Livro', 'Autores', 'Editora', 'Valor', 'Quantidade', 'Disponibilidade'), show='headings')
        self.treeview_livros_disponiveis.column('Livro', minwidth=0, width=200)
        self.treeview_livros_disponiveis.column('Autores', minwidth=0, width=100)
        self.treeview_livros_disponiveis.column('Editora', minwidth=0, width=100)
        self.treeview_livros_disponiveis.column('Valor', minwidth=0, width=50)
        self.treeview_livros_disponiveis.column('Disponibilidade', minwidth=0, width=100)
        self.treeview_livros_disponiveis.column('Quantidade', minwidth=0, width=50)
        self.treeview_livros_disponiveis.heading('Livro', text='Livro')
        self.treeview_livros_disponiveis.heading('Autores', text='Autores')
        self.treeview_livros_disponiveis.heading('Editora', text='Editora')
        self.treeview_livros_disponiveis.heading('Valor', text='Valor')
        self.treeview_livros_disponiveis.heading('Disponibilidade', text='Disponibilidade')
        self.treeview_livros_disponiveis.heading('Quantidade', text='Quantidade')
        self.treeview_livros_disponiveis.place(x=55, y=30, w=880, h=660)
        self.banco_de_dados()
        self.cursor.execute('SELECT * FROM livros')
        self.lista=self.cursor.fetchall()
        count=0
        for dados in self.lista:
            if count %2 == 0:
                self.treeview_livros_disponiveis.insert('', 'end', values=(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6]))
            else:
                self.treeview_livros_disponiveis.insert('', 'end', values=(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6]))
            count+=1
        self.conn.commit()

    def cadastrar_livros(self):
        self.limprar_janela()
        self.menu_principal()

        #frames
        self.frame_cadastrar_livros_0 = Frame(self.frame0, bg=amarelo)
        self.frame_cadastrar_livros_0.place(x=300, y=0, w=980, h=720)

        self.frame_cadastro_de_livros = Frame(self.frame_cadastrar_livros_0, bg=branco)
        self.frame_cadastro_de_livros.place(x=55, y=30, w=880, h=660)

        self.frame_linha = Frame(self.frame_cadastro_de_livros, bg=preto)
        self.frame_linha.place(x=0, y=70, w=880, h=3)

        self.frame_linha_btn_cad = Frame(self.frame_cadastro_de_livros, bg=amarelo)
        self.frame_linha_btn_cad.place(x=304, y=513, w=274, h=4)

        self.frame_linha_btn1_cad = Frame(self.frame_cadastro_de_livros, bg=amarelo)
        self.frame_linha_btn1_cad.place(x=302, y=513, w=4, h=75)

        self.frame_linha_btn2_cad = Frame(self.frame_cadastro_de_livros, bg=amarelo)
        self.frame_linha_btn2_cad.place(x=302, y=586, w=276, h=4)

        self.frame_linha_btn3_cad = Frame(self.frame_cadastro_de_livros, bg=amarelo)
        self.frame_linha_btn3_cad.place(x=575, y=513, w=4, h=77)
        
        #textos
        self.cadastrar_livro_titulo_janela = Label(self.frame_cadastro_de_livros, text='Cadastrar Livro', font='inter 22', bg=branco)
        self.cadastrar_livro_titulo_janela.place(x=65, y=15)

        self.cadastrar_livro_nome = Label(self.frame_cadastro_de_livros, text='Livro:', font='inter 18', bg=branco)
        self.cadastrar_livro_nome.place(x=60, y=93)

        self.cadastrar_livro_autores = Label(self.frame_cadastro_de_livros, text='Autores:', font='inter 18', bg=branco)
        self.cadastrar_livro_autores.place(x=60, y=159)

        self.cadastrar_livro_editora = Label(self.frame_cadastro_de_livros, text='Editora:', font='inter 18', bg=branco)
        self.cadastrar_livro_editora.place(x=60, y=225)

        self.cadastrar_livro_valor = Label(self.frame_cadastro_de_livros, text='Valor:', font='inter 18', bg=branco)
        self.cadastrar_livro_valor.place(x=60, y=291)

        self.cadastrar_livro_quantidade = Label(self.frame_cadastro_de_livros, text='Quantidade:', font='inter 18', bg=branco)
        self.cadastrar_livro_quantidade.place(x=60, y=357)

        self.cadastrar_livro_disponibilidade = Label(self.frame_cadastro_de_livros, text='Disponibilidade:', font='inter 18', bg=branco)
        self.cadastrar_livro_disponibilidade.place(x=60, y=423)

        #entry
        self.entry_cadastro_de_livros_nome = Entry(self.frame_cadastro_de_livros, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_livros_nome.place(x=200, y=98, w=600, h=26)

        self.entry_cadastro_de_livros_autores = Entry(self.frame_cadastro_de_livros, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_livros_autores.place(x=200, y=164, w=600, h=26)

        self.entry_cadastro_de_livros_editora = Entry(self.frame_cadastro_de_livros, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_livros_editora.place(x=200, y=230, w=600, h=26)

        self.entry_cadastro_de_livros_valor = Entry(self.frame_cadastro_de_livros, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_livros_valor.place(x=200, y=296, w=600, h=26)

        self.entry_cadastro_de_livros_quantidade = Entry(self.frame_cadastro_de_livros, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_livros_quantidade.place(x=200, y=362, w=600, h=26)

        # botoes
        self.escolha = StringVar()
        self.rb_emprestimo = Radiobutton(self.frame_cadastro_de_livros, text='Empréstimo', variable = self.escolha, value='Empréstimo', bg=branco)
        self.rb_emprestimo.place(x=250, y=430)
        self.rb_compra = Radiobutton(self.frame_cadastro_de_livros, text='Compra',variable = self.escolha, value='Compra', bg=branco)
        self.rb_compra.place(x=380, y=430)

        self.botao_cadastrar_livro_no_db = Button(self.frame_cadastro_de_livros, text='Cadastrar Livro', font='inter 12', bg=branco, fg=preto, relief=GROOVE, command=self.cadastrar_livros_db)
        self.botao_cadastrar_livro_no_db.place(x=306, y=517, w=270, h=70)

    def cadastrar_fornecedores(self):
        self.limprar_janela()
        self.menu_principal()

        #frames
        self.frame_cadastrar_fornecedores_0 = Frame(self.frame0, bg=amarelo)
        self.frame_cadastrar_fornecedores_0.place(x=300, y=0, w=980, h=720)

        self.frame_cadastro_de_fornecedores = Frame(self.frame_cadastrar_fornecedores_0, bg=branco)
        self.frame_cadastro_de_fornecedores.place(x=55, y=30, w=880, h=660)

        self.frame_linha = Frame(self.frame_cadastro_de_fornecedores, bg=preto)
        self.frame_linha.place(x=0, y=70, w=880, h=3)

        self.frame_linha_btn_cad = Frame(self.frame_cadastro_de_fornecedores, bg=amarelo)
        self.frame_linha_btn_cad.place(x=304, y=476, w=274, h=4)

        self.frame_linha_btn1_cad = Frame(self.frame_cadastro_de_fornecedores, bg=amarelo)
        self.frame_linha_btn1_cad.place(x=302, y=476, w=4, h=75)

        self.frame_linha_btn2_cad = Frame(self.frame_cadastro_de_fornecedores, bg=amarelo)
        self.frame_linha_btn2_cad.place(x=302, y=549, w=276, h=4)

        self.frame_linha_btn3_cad = Frame(self.frame_cadastro_de_fornecedores, bg=amarelo)
        self.frame_linha_btn3_cad.place(x=575, y=476, w=4, h=77)

        #textos
        self.cadastrar_livro_titulo_janela = Label(self.frame_cadastro_de_fornecedores, text='Cadastrar Fornecedor', font='inter 22', bg=branco)
        self.cadastrar_livro_titulo_janela.place(x=65, y=15)

        self.cadastrar_livro_nome = Label(self.frame_cadastro_de_fornecedores, text='Empresa:', font='inter 18', bg=branco)
        self.cadastrar_livro_nome.place(x=60, y=133)

        self.cadastrar_livro_autores = Label(self.frame_cadastro_de_fornecedores, text='Telefone:', font='inter 18', bg=branco)
        self.cadastrar_livro_autores.place(x=60, y=199)

        self.cadastrar_livro_editora = Label(self.frame_cadastro_de_fornecedores, text='Email:', font='inter 18', bg=branco)
        self.cadastrar_livro_editora.place(x=60, y=265)

        self.cadastrar_livro_valor = Label(self.frame_cadastro_de_fornecedores, text='Sede:', font='inter 18', bg=branco)
        self.cadastrar_livro_valor.place(x=60, y=331)

        # entry
        self.entry_cadastro_de_fornecedor_empresa = Entry(self.frame_cadastro_de_fornecedores, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_fornecedor_empresa.place(x=200, y=140, w=600, h=26)

        self.entry_cadastro_de_fornecedor_telefone = Entry(self.frame_cadastro_de_fornecedores, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_fornecedor_telefone.place(x=200, y=206, w=600, h=26)

        self.entry_cadastro_de_fornecedor_email = Entry(self.frame_cadastro_de_fornecedores, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_fornecedor_email.place(x=200, y=272, w=600, h=26)

        self.entry_cadastro_de_fornecedor_sede = Entry(self.frame_cadastro_de_fornecedores, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_fornecedor_sede.place(x=200, y=338, w=600, h=26)

        # botoes
        self.botao_cadastrar_livro_no_db = Button(self.frame_cadastro_de_fornecedores, text='Cadastrar Fornecedor', font='inter 12', bg=branco, fg=preto, relief=GROOVE, command=self.cadastrar_fornecedor)
        self.botao_cadastrar_livro_no_db.place(x=306, y=480, w=270, h=70)

    def ver_fornecedores(self):
        self.limprar_janela()
        self.menu_principal()

        #frames
        self.frame_ver_fornecedores_0 = Frame(self.frame0, bg=amarelo)
        self.frame_ver_fornecedores_0.place(x=300, y=0, w=980, h=720)

        #treeview
        global dadosf
        self.treeview_fornecedores_disponiveis = Treeview(self.frame_ver_fornecedores_0, columns=('Empresa', 'Telefone', 'Email', 'Sede'), show='headings')
        self.treeview_fornecedores_disponiveis.column('Empresa', minwidth=0, width=150)
        self.treeview_fornecedores_disponiveis.column('Telefone', minwidth=0, width=60)
        self.treeview_fornecedores_disponiveis.column('Email', minwidth=0, width=200)
        self.treeview_fornecedores_disponiveis.column('Sede', minwidth=0, width=200)
        self.treeview_fornecedores_disponiveis.heading('Empresa', text='Empresa')
        self.treeview_fornecedores_disponiveis.heading('Telefone', text='Telefone')
        self.treeview_fornecedores_disponiveis.heading('Email', text='Email')
        self.treeview_fornecedores_disponiveis.heading('Sede', text='Sede')
        self.treeview_fornecedores_disponiveis.place(x=55, y=30, w=880, h=660)
        self.banco_de_dados()
        self.cursor.execute('SELECT * FROM fornecedores')
        self.lista2=self.cursor.fetchall()
        count=0
        for dadosf in self.lista2:
            if count %2 == 0:
                self.treeview_fornecedores_disponiveis.insert('', 'end', values=(dadosf[0], dadosf[1], dadosf[2], dadosf[3]))
            else:
                self.treeview_fornecedores_disponiveis.insert('', 'end', values=(dadosf[0], dadosf[1], dadosf[2], dadosf[3]))
            count+=1
        self.conn.commit()

    def clientes_vendas(self):
        self.limprar_janela()
        self.menu_principal()

        #frames
        self.frame_clientes = Frame(self.frame0, bg=amarelo)
        self.frame_clientes.place(x=300, y=0, w=980, h=720)

        self.frame_clientes_principal = Frame(self.frame_clientes, bg=branco)
        self.frame_clientes_principal.place(x=55, y=30, w=880, h=660)

        self.frame_linha = Frame(self.frame_clientes_principal, bg=preto)
        self.frame_linha.place(x=0, y=68, w=880, h=2)

        #botoes
        self.botao_ver_clientes = Button(self.frame_clientes_principal, text='Ver Clientes', font='inter 12', bg=branco, fg=preto, relief=GROOVE, command=self.ver_clientes)
        self.botao_ver_clientes.place(x=527, y=95, w=270, h=70)

        self.botao_cadastrar_clientes = Button(self.frame_clientes_principal, text='Cadastrar Clientes', font='inter 12', bg=branco, fg=preto, relief=GROOVE, command=self.cadastrar_clientes)
        self.botao_cadastrar_clientes.place(x=141, y=95, w=270, h=70)

        #clientes
        self.text_titulo_janela = Label(self.frame_clientes_principal, text='Clientes', font='inter 20', bg=branco, fg=preto)
        self.text_titulo_janela.place(x=64, y=18)

    def cadastrar_clientes(self):
        self.limpar_frame_clientes()
        
        self.frame_linha = Frame(self.frame_clientes_principal, bg=preto)
        self.frame_linha.place(x=0, y=70, w=880, h=3)

        self.frame_linha_btn_cad = Frame(self.frame_clientes_principal, bg=amarelo)
        self.frame_linha_btn_cad.place(x=304, y=476, w=274, h=4)

        self.frame_linha_btn1_cad = Frame(self.frame_clientes_principal, bg=amarelo)
        self.frame_linha_btn1_cad.place(x=302, y=476, w=4, h=75)

        self.frame_linha_btn2_cad = Frame(self.frame_clientes_principal, bg=amarelo)
        self.frame_linha_btn2_cad.place(x=302, y=549, w=276, h=4)

        self.frame_linha_btn3_cad = Frame(self.frame_clientes_principal, bg=amarelo)
        self.frame_linha_btn3_cad.place(x=575, y=476, w=4, h=77)

        #textos
        self.cadastrar_cliente_titulo_janela = Label(self.frame_clientes_principal, text='Cadastrar Cliente', font='inter 22', bg=branco)
        self.cadastrar_cliente_titulo_janela.place(x=65, y=15)

        self.cadastrar_cliente_nome = Label(self.frame_clientes_principal, text='Nome:', font='inter 18', bg=branco)
        self.cadastrar_cliente_nome.place(x=60, y=133)

        self.cadastrar_cliente_email = Label(self.frame_clientes_principal, text='Email:', font='inter 18', bg=branco)
        self.cadastrar_cliente_email.place(x=60, y=199)

        self.cadastrar_cliente_telefone = Label(self.frame_clientes_principal, text='Telefone:', font='inter 18', bg=branco)
        self.cadastrar_cliente_telefone.place(x=60, y=265)

        self.cadastrar_cliente_endereco = Label(self.frame_clientes_principal, text='Endereço:', font='inter 18', bg=branco)
        self.cadastrar_cliente_endereco.place(x=60, y=331)

        self.cadastrar_cliente_cpf = Label(self.frame_clientes_principal, text='CPF:', font='inter 18', bg=branco)
        self.cadastrar_cliente_cpf.place(x=60, y=397)

        # entry
        self.entry_cadastro_de_cliente_nome = Entry(self.frame_clientes_principal, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_cliente_nome.place(x=200, y=140, w=600, h=26)

        self.entry_cadastro_de_cliente_email = Entry(self.frame_clientes_principal, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_cliente_email.place(x=200, y=206, w=600, h=26)

        self.entry_cadastro_de_cliente_telefone = Entry(self.frame_clientes_principal, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_cliente_telefone.place(x=200, y=272, w=600, h=26)

        self.entry_cadastro_de_cliente_endereco = Entry(self.frame_clientes_principal, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_cliente_endereco.place(x=200, y=338, w=600, h=26)

        self.entry_cadastro_de_cliente_cpf = Entry(self.frame_clientes_principal, bg=branco, fg=preto, font='inter 13', borderwidth=2, relief=GROOVE)
        self.entry_cadastro_de_cliente_cpf.place(x=200, y=404, w=600, h=26)

        #botoes
        self.botao_cadastrar_clientes_db = Button(self.frame_clientes_principal, text='Cadastrar Clientes', font='inter 12', bg=branco, fg=preto, relief=GROOVE, command=self.cadastrar_clientes_db)
        self.botao_cadastrar_clientes_db.place(x=306, y=480, w=270, h=70)
    
    def ver_clientes(self):
        self.limprar_janela()
        self.menu_principal()

        #frames
        self.frame_ver_clientes = Frame(self.frame0, bg=amarelo)
        self.frame_ver_clientes.place(x=300, y=0, w=980, h=720)

        #treeview
        global dadosc
        self.treeview_clientes = Treeview(self.frame_ver_clientes, columns=('Nome', 'Email', 'Telefone', 'Endereço', 'Cpf'), show='headings')
        self.treeview_clientes.column('Nome', minwidth=0, width=100)
        self.treeview_clientes.column('Email', minwidth=0, width=150)
        self.treeview_clientes.column('Telefone', minwidth=0, width=80)
        self.treeview_clientes.column('Endereço', minwidth=0, width=250)
        self.treeview_clientes.column('Cpf', minwidth=0, width=50)
        self.treeview_clientes.heading('Nome', text='Nome')
        self.treeview_clientes.heading('Email', text='Email')
        self.treeview_clientes.heading('Telefone', text='Telefone')
        self.treeview_clientes.heading('Endereço', text='Endereço')
        self.treeview_clientes.heading('Cpf', text='CPF')
        self.treeview_clientes.place(x=55, y=30, w=880, h=660)
        self.banco_de_dados()
        self.cursor.execute('SELECT * FROM clientes')
        self.lista2=self.cursor.fetchall()
        count=0
        for dadosc in self.lista2:
            if count %2 == 0:
                self.treeview_clientes.insert('', 'end', values=(dadosc[0], dadosc[1], dadosc[2], dadosc[3], dadosc[4]))
            else:
                self.treeview_clientes.insert('', 'end', values=(dadosc[0], dadosc[1], dadosc[2], dadosc[3], dadosc[4]))
            count+=1
        self.conn.commit()

    def limpar_frame_clientes(self):
        self.frame_clientes_principal.destroy
        self.frame_clientes_principal = Frame(self.frame_clientes, bg=branco)
        self.frame_clientes_principal.place(x=55, y=30, w=880, h=660)

    def limprar_janela(self):
        self.frame0.destroy
        self.frame0 = Frame(self.janela, bg=amarelo)
        self.frame0.place(x=0, y=0, w=1280, h=720)

    def ir_tela_cadastro(self):
        self.limprar_janela()
        self.cadastro()

    def ir_tela_login(self):
        self.limprar_janela()
        self.login()

    def ir_tela_menu_principal(self):
        self.limprar_janela()
        self.menu_principal()

    def cadastrar_adm(self):
        self.banco_de_dados()
        self.valor_nome = self.entry_nome.get()
        self.valor_email = self.entry_email.get()
        self.valor_senha = self.entry_senha.get()

        if self.valor_nome == '' or self.valor_email == '' or self.valor_senha == '':
            messagebox.showerror('info', 'dados incompletos')

        else: 
            self.cursor.execute(f'''INSERT INTO cadadm (nome, email, senha) 
                            values ('{self.valor_nome}', '{self.valor_email}', '{self.valor_senha}')''')
            self.conn.commit()
            messagebox.showinfo('info', 'cadastro concluído')
        self.ir_tela_cadastro()

    def login_adm(self):
        self.banco_de_dados()
        self.cursor.execute(f"SELECT senha FROM cadadm WHERE Email={self.entrada_cpf.get()} AND Senha={self.entrada_senha.get()}")
        row = self.cursor.fetchall()
        if row:
            messagebox.showinfo('info', 'Login efetuado com sucesso')
            self.conn.commit()
            self.ir_tela_menu_principal()

    def cadastrar_livros_db(self):
        self.banco_de_dados()
        valor1 = self.entry_cadastro_de_livros_nome.get()
        valor2 = self.entry_cadastro_de_livros_autores.get()
        valor3 = self.entry_cadastro_de_livros_editora.get()
        valor4 = self.entry_cadastro_de_livros_valor.get()
        valor5 = self.entry_cadastro_de_livros_quantidade.get()
        valor6 = self.escolha.get()
        if valor1 and valor2 == '' or valor3 == '' or valor4 == '' or valor5 == '' or valor6 == '':
            messagebox.showerror('Tente Novamente', 'Existe uma falta de informações para completar o cadastro do produto')
        else:
            self.cursor.execute(f'''INSERT INTO livros (Livro, Autores, Editora, Valor, Quantidade, Disponibilidade) 
                                VALUES ('{valor1}', '{valor2}', '{valor3}', '{valor4}', '{valor5}', '{valor6}')''')
            self.conn.commit()
            messagebox.showinfo('info', 'cadastro concluído')
            self.limprar_janela()
            self.cadastrar_livros()

    def cadastrar_fornecedor(self):
        self.banco_de_dados()
        valor1 = self.entry_cadastro_de_fornecedor_empresa.get()
        valor2 = self.entry_cadastro_de_fornecedor_telefone.get()
        valor3 = self.entry_cadastro_de_fornecedor_email.get()
        valor4 = self.entry_cadastro_de_fornecedor_sede.get()
        if valor1 and valor2 == '' or valor3 == '' or valor4 == '':
            messagebox.showerror('Tente Novamente', 'Existe uma falta de informações para completar o cadastro do produto')
        else:
            self.cursor.execute(f'''INSERT INTO fornecedores (Empresa, Telefone, Email, Sede)
                                value ('{valor1}', '{valor2}', '{valor3}', '{valor4}')''')
            self.conn.commit()
            messagebox.showinfo('info', 'cadastro concluído')
            self.limprar_janela()
            self.cadastrar_fornecedores()
                                
    def cadastrar_clientes_db(self):
        self.banco_de_dados()
        valor1 = self.entry_cadastro_de_cliente_nome.get()
        valor2 = self.entry_cadastro_de_cliente_email.get()
        valor3 = self.entry_cadastro_de_cliente_telefone.get()
        valor4 = self.entry_cadastro_de_cliente_endereco.get()
        valor5 = self.entry_cadastro_de_cliente_cpf.get()
        if valor1 and valor2 == '' or valor3 == '' or valor4 == '' or valor5 == '':
            messagebox.showerror('Tente Novamente', 'Existe uma falta de informações para completar o cadastro do produto')
        else:
            self.cursor.execute(f'''INSERT INTO clientes (Nome, Email, Telefone, Endereço, Cpf)
                                value ('{valor1}', '{valor2}', '{valor3}', '{valor4}', '{valor5}')''')
            self.conn.commit()
            messagebox.showinfo('info', 'cadastro concluído')
            self.limprar_janela()
            self.clientes_vendas()

    def banco_de_dados(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            db='livraria',
            password='')
        self.cursor = self.conn.cursor()
        self.cursor.execute('use livraria')

app = livraria()
app.login()
app.janela.mainloop()