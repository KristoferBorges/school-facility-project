from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud
from app.support.modulo import FunctionsCase
class CadastroService(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
        self.dependencia = None
    
    def finalizarCadastroService(self):
        """
        Método responsável analisar os campos preenchidos e utilizar a função de cadastro do sistema
        """
        try:
            nome_service = self.ids.nome_service.text
            valor_service = self.ids.valor_service.text
            if self.dependencia == True:
                dependencia_service = "DP"
            else:
                dependencia_service = "Regular"
            
            if (nome_service == "") or (valor_service == "") or (self.dependencia == None):
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_preenchimento()
            else:
                self.system_crud.conectar_banco()
                if self.system_crud.createService(nome_service, valor_service, dependencia_service) == True:
                    self.ids.nome_service.text = ""
                    self.ids.valor_service.text = ""
                    self.ids.icon_sem_dependencia.opacity = 0
                    self.ids.icon_com_dependencia.opacity = 0
                    FunctionsCase.popup_cadastro_sucesso()
                else:
                    FunctionsCase.popup_error(f"{self.system_crud.error}")
        except Exception as erro:
            print(f"Exceção cadastroService: {erro}")

    def mostrarIconSemDependencia(self):
        """
        Método responsável por mostrar o ícone de check
        """
        self.ids.icon_sem_dependencia.opacity = 1
        self.ids.icon_com_dependencia.opacity = 0
        self.dependencia = False

        return self.dependencia
    def mostrarIconComDependencia(self):
        """
        Método responsável por mostrar o ícone de check
        """
        self.ids.icon_sem_dependencia.opacity = 0
        self.ids.icon_com_dependencia.opacity = 1
        self.dependencia = True

        return self.dependencia
        

    
