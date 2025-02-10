import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud, UserManager
from kivy.lang import Builder
from kivy.clock import Clock
from time import sleep

class TelaPrincipal(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_manager = UserManager()
        

    def logout(self):
        """
        Método responsável por fazer o logout do usuário ao clicar no botão de logout
        """
        self.user_manager.logout()
        if self.user_manager.is_user_logged_in() == False:
            if platform.system() == "Windows":
                Window.size = (900, 394)
        
        # Ativa a função de resetSpinner
        self.manager.get_screen("login_screen").resetSpinner()


    def verificarConexao(self):
        """
        Médoto que verifica a conexão com o banco de dados, caso esteja conectado irá mostrar um icone, e se não estiver, irá mostrar outro icone
        """
        system_crud_instance = System_Crud()
        if system_crud_instance.connected == True:
            self.ids.conexao_icon.text_color = (0, 1, 0, 0.7)
            self.ids.conexao_icon.icon_color = (0, 1, 0, 0.7)
            self.ids.conexao_icon.text = "CONECTADO"
        elif system_crud_instance.connected == False:
            self.ids.conexao_icon.text_color = (0.7, 0, 0, 1)
            self.ids.conexao_icon.icon_color = (0.7, 0, 0, 1)
            self.ids.conexao_icon.text = "DESCONECTADO"
        else:
            self.ids.conexao_icon.text_color = (1, 1, 0, 1)
            self.ids.conexao_icon.icon_color = (1, 1, 0, 1)
            self.ids.conexao_icon.text = "CONECTANDO..."

    def tryConnect(self):
        """
        Método para realizar outra conexão com o banco de dados
        """
        system_crud_instance = System_Crud()

        self.ids.conexao_icon.text_color = (1, 1, 0, 1)
        self.ids.conexao_icon.icon_color = (1, 1, 0, 1)
        self.ids.conexao_icon.text = "CONECTANDO"
        Clock.schedule_once(lambda x: self.verificarConexao(), 1.5)

        system_crud_instance.conectar_banco()

        

