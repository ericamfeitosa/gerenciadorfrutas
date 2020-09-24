#!/usr/bin/python 
# encoding: utf-8

from os import chdir, path
chdir(path.dirname(path.abspath(__file__)))
from unipath import Path
from threading import Thread
import kivy
import time
from kivy.app import App
from kivy.app import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from unipath import Path
from kivy.config import Config
from kivy.clock import mainthread
import profig
from threading import Timer

tempo = 0
Config.set('graphics', 'width', 900) #largura1370 800
Config.set('graphics', 'height', 600) #altura700
       
class PaginaInicial(Screen):
    pass

class PaginaCadastro(Screen):
    pass

class PaginaColheita(Screen):
    pass

class PaginaRelatorio(Screen):
    pass
 

class ScreenManagement(ScreenManager):

    def switch_to_paginaInicial(self):
        self.current = 'paginaInicial'

    def switch_to_paginaCadastro(self):
        self.current = 'paginaCadastro'

    def switch_to_paginaColheita(self):
        self.current = 'paginaColheita'

    def switch_to_paginaRelatorio(self):
        self.current = 'paginaRelatorio'
	
#
# Objeto da aplicação Kivy
#
class Gerenciador(App):
    def build(self):
        self.root = ScreenManagement()
        return self.root
    '''
    Implementação da interface GUI em Kivy
    '''
    #
    # Arquivo de configuração a interface
    #
    kv_file = 'tela.kv'
	
    #
    # Construtor
    #
    def __init__(self,args):

        App.__init__(self)
        self.numero_tela = 0

    def conexao_banco():
        print("CONEXAO BANCO")

    def cadastro():
        print("CADASTRO")

    def colheita():
        print("COLHEITA")

    def relatorio():
        print("RELATORIO")
        
        
    def paginicial(self):
        self.numero_tela = 0
        self.root.switch_to_paginaInicial()
	
    def pagcadastro(self):
        self.numero_tela = 1
        self.root.switch_to_paginaCadastro()

    def pagcolheita(self):
        self.numero_tela = 2
        self.root.switch_to_paginaColheita()

    def pagrelatorio(self):
        self.numero_tela = 2
        self.root.switch_to_paginaRelatorio()
        
    def id(self, v):
        'Procura por um identificador definido no arquivo kv'
        # Busca recursivamente pelos objetos
        def find_id(node, v):
            for c in node.children:
                x = find_id(c, v)
                if x: return x
                if v in c.ids: return c.ids[v]
            return None

        # Inicia busca pelo objeto raiz.
        if v in self.root.ids:
            return self.root.ids[v]
        return find_id(self.root, v)

    @mainthread
    def img_fundo(self, valor):
        'Mostrar logo no fundo da tela'
        self.id('img_fundo').source = 'img/LOGO.jpg'

    
    @mainthread
    def especie_arvore(self, valor):
        'Mostra a especie que o usuario cadastrar'
        self.id('especie_arvore').especie_arvore = valor 

    
    @mainthread
    def grupo_arvore(self, valor):
        'Mostra que grupo o usuario cadastrar'
        self.id('grupo_arvore').grupo_arvore = valor 

    
    @mainthread
    def data_arvore(self, valor):
        'Mostra a especie que o usuario cadastrar'
        self.id('data_arvore').data_arvore = valor 
        
def thread_atualizacao():
    global tempo
    while True:
        time.sleep(1)
        tempo = tempo + 1
        print(tempo)
        if app.numero_tela == 0:
            app.img_fundo('img/LOGO.jpg')
        
app = Gerenciador(App)
atualiza = Thread(target=thread_atualizacao)
atualiza.daemon=True
atualiza.start()
app.run()
