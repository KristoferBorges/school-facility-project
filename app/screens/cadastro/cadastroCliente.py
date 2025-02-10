from datetime import datetime
from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud
from app.support.modulo import FunctionsCase
class CadastroCliente(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()

    def finalizarCadastroCliente(self):
        """
        Método responsável analisar os campos preenchidos e utilizar a função de cadastro do sistema
        """
        try:
            ra_cliente = self.ids.ra_cliente.text
            nome_cliente = FunctionsCase.filtrandoLetras(self.ids.nome_cliente.text)
            semestre_cliente = self.ids.semestre_cliente.text
            data_registro = datetime.now().strftime("%Y-%m-%d")
            comentario_cliente = self.ids.comentario_cliente.text

            if (ra_cliente == "") or (nome_cliente == "" or len(nome_cliente) < 5) or (semestre_cliente == ""):
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_preenchimento()
            else:
                self.system_crud.conectar_banco()
                if self.system_crud.createClients(ra_cliente, nome_cliente, semestre_cliente, data_registro, comentario_cliente) == True:
                    self.ids.ra_cliente.text = ""
                    self.ids.nome_cliente.text = ""
                    self.ids.semestre_cliente.text = ""
                    self.ids.comentario_cliente.text = ""
                    FunctionsCase.popup_cadastro_sucesso()
                else:
                    FunctionsCase.popup_error(f"{self.system_crud.error}")
        except Exception as erro:
            print(f"Exceção cadastroCliente: {erro}")
