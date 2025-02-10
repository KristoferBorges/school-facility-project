from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime
from app.support.modulo import FunctionsCase

class AlterarCliente(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
        self.data_registro = None
        self.data_from_database = None
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

    def on_save(self, instance, value, date_range):
        """
        Evento chamado quando o botão "OK" da caixa de diálogo é clicado.
        """
        valueFormated = value.strftime("%d/%m/%Y")
        self.ids.data_registro.text = valueFormated
        self.data_registro = value.strftime("%Y-%m-%d")

        instance.dismiss()

    def on_cancel(self, instance, value):
        """
        Evento chamado quando o botão "CANCELAR" da caixa de diálogo é clicado (sem evento).
        """
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.title = "DATA DE REGISTRO"
        date_dialog.radius = [20, 7, 20, 7]
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        self.ids.data_registro.text = datetime.now().strftime("%d/%m/%Y")
        date_dialog.open()
    
    def consultarCliente(self):
        """
        Método responsável por fazer a busca do RA do cliente no banco de dados.
        """
        try:
            if self.system_crud.read_RA(self.ids.ra_cliente.text) == False:
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_ra_nao_encontrado()

            else:
                self.data_from_database = self.system_crud.read_RA(self.ids.ra_cliente.text)
                
                # Preenchendo os campos com os dados do cliente
                self.ids.nome_cliente.text = self.data_from_database[0][1]
                self.ids.semestre_cliente.text = self.data_from_database[0][2]
                self.ids.data_registro.text = self.data_from_database[0][3].strftime("%d/%m/%Y")
                self.ids.comentario_cliente.text = self.data_from_database[0][4]
                
                status = self.data_from_database[0][5]

                if status == "ATIVO":
                    self.statusAtivo()
                elif status == "INATIVO":
                    self.statusInativo()
                else:
                    pass

                # Libera os campos para edição
                self.ids.ra_cliente.readonly = True
                self.ids.ra_cliente.line_color_focus = (1, 0, 0, 1)
                self.ids.nome_cliente.readonly = False
                self.ids.semestre_cliente.readonly = False
                self.ids.data_registro.readonly = False
                self.ids.comentario_cliente.readonly = False
                self.ids.btn_data_registro.disabled = False
                self.ids.btn_ativo.disabled = False
                self.ids.btn_inativo.disabled = False

        except Exception as erro:
            if "NoneType" in str(erro):
                FunctionsCase.popup_ra_nao_encontrado()
            print(f"Exceção alterarCliente: {erro}")

    def finalizarAlteracao(self):
        """
        Método responsável por finalizar a alteração do cliente no banco de dados.
        """
        try:
            if self.ids.nome_cliente.text == "" or self.ids.semestre_cliente.text == "" or self.ids.data_registro.text == "":
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_preenchimento()

            else:
                # Verifica/Formata informações
                self.ids.nome_cliente.text = self.ids.nome_cliente.text.title()
                self.data_registro = datetime.strptime(self.ids.data_registro.text, "%d/%m/%Y").strftime("%Y-%m-%d")

                if self.system_crud.update_client(self.ids.ra_cliente.text, self.ids.nome_cliente.text, self.ids.semestre_cliente.text, self.data_registro, self.ids.comentario_cliente.text, self.status) == True:
                    FunctionsCase.popup_alteracao_sucesso()
                    self.ids.ra_cliente.text = ""
                    self.ids.nome_cliente.text = ""
                    self.ids.semestre_cliente.text = ""
                    self.ids.data_registro.text = ""
                    self.ids.comentario_cliente.text = ""
                    self.ids.icon_ativo.opacity = 0
                    self.ids.icon_inativo.opacity = 0
                    self.status = None

                    # Bloqueia os campos para edição
                    self.ids.ra_cliente.readonly = False
                    self.ids.ra_cliente.line_color_focus = (1, 1, 1, 1)
                    self.ids.nome_cliente.readonly = True
                    self.ids.semestre_cliente.readonly = True
                    self.ids.data_registro.readonly = True
                    self.ids.comentario_cliente.readonly = True
                    self.ids.btn_data_registro.disabled = True
                    self.ids.btn_ativo.disabled = True
                    self.ids.btn_inativo.disabled = True

                else:
                    FunctionsCase.popup_change_error(self.system_crud.error)
                    self.ids.ra_cliente.text = ""
                    self.ids.nome_cliente.text = ""
                    self.ids.semestre_cliente.text = ""
                    self.ids.data_registro.text = ""
                    self.ids.comentario_cliente.text = ""
                    self.ids.icon_ativo.opacity = 0
                    self.ids.icon_inativo.opacity = 0
                    self.status = None

                    # Bloqueia os campos para edição
                    self.ids.ra_cliente.readonly = False
                    self.ids.ra_cliente.line_color_focus = (1, 1, 1, 1)
                    self.ids.nome_cliente.readonly = True
                    self.ids.semestre_cliente.readonly = True
                    self.ids.data_registro.readonly = True
                    self.ids.comentario_cliente.readonly = True
                    self.ids.btn_data_registro.disabled = True
                    self.ids.btn_ativo.disabled = True
                    self.ids.btn_inativo.disabled = True

        except Exception as erro:
            print(f"Exceção alterarCliente: {erro}")
    
    def resetarCampos(self):
        """
        Método ligado ao botão da interface para resetar os campos preenchidos.
        --> Sem retorno.
        """
        self.ids.ra_cliente.text = ""
        self.ids.nome_cliente.text = ""
        self.ids.semestre_cliente.text = ""
        self.ids.data_registro.text = ""
        self.ids.comentario_cliente.text = ""
        self.ids.icon_ativo.opacity = 0
        self.ids.icon_inativo.opacity = 0
        self.status = None

        # Bloqueia os campos para edição
        self.ids.ra_cliente.readonly = False
        self.ids.ra_cliente.line_color_focus = (1, 1, 1, 1)
        self.ids.nome_cliente.readonly = True
        self.ids.semestre_cliente.readonly = True
        self.ids.data_registro.readonly = True
        self.ids.comentario_cliente.readonly = True
        self.ids.btn_data_registro.disabled = True
        self.ids.btn_ativo.disabled = True
        self.ids.btn_inativo.disabled = True

