from kivy.uix.screenmanager import Screen
from app.support.setup import System_Crud
from app.support.modulo import FunctionsCase

class AlterarService(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
        self.data_from_database = None
        self.dependencia = None
        self.status = None

    def statusAtivo(self):
        """
        Método responsável por mostrar o ícone de check
        """
        self.ids.icon_ativo.opacity = 1
        self.ids.icon_inativo.opacity = 0
        self.status = "ATIVO"
    
    def statusInativo(self):
        """
        Método responsável por mostrar o ícone de check
        """
        self.ids.icon_inativo.opacity = 1
        self.ids.icon_ativo.opacity = 0
        self.status = "INATIVO"

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
    
    def consultarServico(self):
        """
        Método responsável por consultar um serviço
        """
        try:
            if self.system_crud.read_ID_service(self.ids.id_servico.text) == False:
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_id_nao_encontrado()

            else:
                self.data_from_database = self.system_crud.read_ID_service(self.ids.id_servico.text)

                # Preenchendo os campos com os dados do serviço
                self.ids.nome_servico.text = self.data_from_database[0][1]
                self.ids.valor_servico.text = str(self.data_from_database[0][2])
        
                dependencia = self.data_from_database[0][3]
                status = self.data_from_database[0][4]

                if dependencia == "DP":
                    self.mostrarIconComDependencia()
                elif dependencia == "Regular":
                    self.mostrarIconSemDependencia()
                else:
                    pass

                if status == "ATIVO":
                    self.statusAtivo()
                elif status == "INATIVO":
                    self.statusInativo()
                else:
                    pass
                
            
                # Libera os campos para edição
                self.ids.id_servico.readonly = True
                self.ids.nome_servico.readonly = False
                self.ids.valor_servico.readonly = False
                self.ids.btn_sem_dependencia.disabled = False
                self.ids.btn_com_dependencia.disabled = False
                self.ids.btn_ativo.disabled = False
                self.ids.btn_inativo.disabled = False

                
        except Exception as erro:
            if "NoneType" in str(erro):
                FunctionsCase.popup_id_nao_encontrado()
            print(f"Exceção alterarService: {erro}")
        

    def finalizarAlteracao(self):
        """
        Método responsável por finalizar a alteração do serviço no banco de dados.
        """
        try:
            if self.ids.nome_servico == "" or self.ids.valor_servico == "" or self.dependencia == None:
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_preenchimento()
            else:
                # Verifica/Formata informações
                self.ids.nome_servico.text = self.ids.nome_servico.text.upper()
                self.ids.valor_servico.text = self.ids.valor_servico.text.replace(",", ".")
                if self.dependencia == True:
                    self.dependencia = "DP"
                else:
                    self.dependencia = "Regular"

                if self.ids.nome_servico.text == "" or self.ids.valor_servico.text == "" or self.dependencia == None:
                    # Pop-up de erro de preenchimento
                    FunctionsCase.popup_preenchimento()

                else:
                    if self.system_crud.update_service(self.ids.id_servico.text, self.ids.nome_servico.text, self.ids.valor_servico.text, self.dependencia, self.status) == True:
                        FunctionsCase.popup_alteracao_sucesso()
                        self.ids.id_servico.text = ""
                        self.ids.nome_servico.text = ""
                        self.ids.valor_servico.text = ""
                        self.ids.icon_sem_dependencia.opacity = 0
                        self.ids.icon_com_dependencia.opacity = 0
                        self.ids.icon_ativo.opacity = 0
                        self.ids.icon_inativo.opacity = 0

                        # Bloqueia os campos para edição
                        self.ids.id_servico.readonly = False
                        self.ids.nome_servico.readonly = True
                        self.ids.valor_servico.readonly = True
                        self.ids.btn_sem_dependencia.disabled = True
                        self.ids.btn_com_dependencia.disabled = True
                        self.ids.btn_ativo.disabled = True
                        self.ids.btn_inativo.disabled = True

                    else:
                        FunctionsCase.popup_change_error(self.system_crud.error)
                        self.ids.id_servico.text = ""
                        self.ids.nome_servico.text = ""
                        self.ids.valor_servico.text = ""
                        self.ids.icon_sem_dependencia.opacity = 0
                        self.ids.icon_com_dependencia.opacity = 0
                        self.ids.icon_ativo.opacity = 0
                        self.ids.icon_inativo.opacity = 0
                        self.status = None

                        # Bloqueia os campos para edição
                        self.ids.id_servico.readonly = False
                        self.ids.nome_servico.readonly = True
                        self.ids.valor_servico.readonly = True
                        self.ids.btn_sem_dependencia.disabled = True
                        self.ids.btn_com_dependencia.disabled = True
                        self.ids.btn_ativo.disabled = True
                        self.ids.btn_inativo.disabled = True

        except Exception as erro:
            print(f"Exceção alterarServico: {erro}")

    def resetarCampos(self):
        """
        Método responsável por resetar os campos
        """
        self.ids.id_servico.text = ""
        self.ids.nome_servico.text = ""
        self.ids.valor_servico.text = ""
        self.ids.icon_sem_dependencia.opacity = 0
        self.ids.icon_com_dependencia.opacity = 0
        self.ids.icon_ativo.opacity = 0
        self.ids.icon_inativo.opacity = 0
        self.status = None

        # Bloqueia os campos para edição
        self.ids.id_servico.readonly = False
        self.ids.id_servico.line_color_focus = (1, 1, 1, 1)
        self.ids.nome_servico.readonly = True
        self.ids.valor_servico.readonly = True
        self.ids.btn_sem_dependencia.disabled = True
        self.ids.btn_com_dependencia.disabled = True
        self.ids.btn_ativo.disabled = True
        self.ids.btn_inativo.disabled = True