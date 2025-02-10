import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from app.support.setup import Setup, UserManager
from kivy.clock import Clock

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_manager = UserManager()

    def realizarLogin(self):
        usuario_login = self.ids.text_login.text
        usuario_senha = self.ids.text_senha.text

        if usuario_login == "" and usuario_senha == "":
            self.ids.text_login.text = ""
            self.ids.text_senha.text = ""
            self.ids.result_login.text = ""
            self.ids.text_login.hint_text_color = (0, 0, 0, 1)
            self.ids.text_senha.hint_text_color = (0, 0, 0, 1)
            self.manager.current = "tela_principal"

            # Ativa a função de verificar a coneção com o banco de dados na tela principal
            Clock.schedule_once(lambda x: self.manager.get_screen("tela_principal").verificarConexao(), 2.5)

            self.user_manager.login()
            if self.user_manager.is_user_logged_in() == True:
                if platform.system() == "Windows":
                    Window.size = (900, 754)
        else:
            self.ids.text_login.text = ""
            self.ids.text_senha.text = ""
            self.ids.result_login.text = "Login ou senha incorretos"
            self.ids.text_login.hint_text_color = (1, 0, 0, 1)
            self.ids.text_senha.hint_text_color = (1, 0, 0, 1)
    
    def resetSpinner(self):
        """
        Ativa novamente o Spinner
        """
        self.ids.spinner.active = False
        self.ids.spinner.active = True