
# Cabeçalho Padrão Gtk parte 1

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# ---

class User():
    def __init__(self, id, nome, email):   # Banco de dados provisório
        self.id = id
        self.nome = nome
        self.email = email

class Manipulador(object):   # Métodos de manipuladores
    def __init__(self):
        self.modelo_armazenamento: Gtk.ListStore = Builder.get_object("liststore1")
        self.Stack = Gtk.Stack = Builder.get_object("stack")
        self.banco_dados = []   # Banco de dados provisório

    def on_main_window_destroy(self,window):
        Gtk.main_quit()

    def on_button_login_clicked(self,button):
        email = Builder.get_object("email").get_text()
        senha = Builder.get_object("senha").get_text()
        lembrar = Builder.get_object("lembrar").get_active()
        self.login(email, senha, lembrar)

    def login(self, email, senha, lembrar):
        if email == 'admin' and senha == 'admin':
            self.mensagem('Bem-vindo', 'Usuario logado com sucesso','emblem-default')
            self.Stack.set_visible_child_name("view_inicial")
            window.props.icon_name = 'avatar-default'
        else:
            self.mensagem('Aviso', 'Email ou senha incorretos','dialog-error')

    def mensagem(self, param, param1, param2):
        mensagem: Gtk.MessageDialog = Builder.get_object("mensagem")
        mensagem.props.text = param
        mensagem.props.secondary_text = param1
        mensagem.props.icon_name = param2
        mensagem.show_all()
        mensagem.run()
        mensagem.hide()

    def on_button_cadastrar_inicial_clicked(self, button):
        self.Stack.set_visible_child_name("view_cadastro")

    def on_button_cad_voltar_clicked(self, button):
        self.Stack.set_visible_child_name("view_inicial")

    def on_button_listar_inicial_clicked(self, button):
        self.Stack.set_visible_child_name("view_listar")

    def on_button_listar_voltar_clicked(self, button):
        self.Stack.set_visible_child_name("view_inicial")

    def on_button_sair_inicial_clicked(self, button):
        self.Stack.set_visible_child_name("view_login")
        window.props.icon_name = 'changes-prevent'

    def on_button_cadastrar_clicked(self, button):
        nome = Builder.get_object("cad_nome").get_text()
        email = Builder.get_object("cad_email").get_text()
        if nome != '':
            self.banco_dados.append(User(len(self.banco_dados)+1, nome, email))  # Banco de dados provisório
            self.mensagem('Aviso', 'Usuário ' + nome + ' cadastrado!', 'dialog-emblem-default')
        else:
            self.mensagem('Aviso', 'Campo "Nome" Obrigatório!', 'dialog-error')

    def on_button_listar_clicked(self, button):
        self.modelo_armazenamento.clear()
        for user in self.banco_dados:
            self.modelo_armazenamento.append((user.id, user.nome, user.email))



# Cabeçalho padrão parte 2

Builder = Gtk.Builder()
Builder.add_from_file("Tela_cadastro.glade")
Builder.connect_signals(Manipulador())
Window: Gtk.Window = Builder.get_object("main_window")
Window.show_all()
Gtk.main()


# --- Fim do cabeçalho ---


