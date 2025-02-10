from kivy.uix.screenmanager import Screen
from app.support.setup import System_Crud
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime
from app.support.modulo import FunctionsCase

class AlterarRegistro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
        self.data_from_database = None
        self.situacao = None
        self.data_contratacao = None
        self.data_entrega = None
    
    def situacaoPendente(self):
        """
        Método responsável por mostrar o ícone de check
        """
        self.ids.icon_pendente.opacity = 1
        self.ids.icon_concluido.opacity = 0
        self.ids.icon_indeferido.opacity = 0
        self.situacao = "PENDENTE"
    
    def situacaoConcluido(self):
        """
        Método responsável por mostrar o ícone de check
        """
        self.ids.icon_pendente.opacity = 0
        self.ids.icon_concluido.opacity = 1
        self.ids.icon_indeferido.opacity = 0
        self.situacao = "CONCLUIDO"
    
    def situacaoIndeferido(self):
        """
        Método responsável por mostrar o ícone de check
        """
        self.ids.icon_pendente.opacity = 0
        self.ids.icon_concluido.opacity = 0
        self.ids.icon_indeferido.opacity = 1
        self.situacao = "INDEFERIDO"

    def on_save_contratacao(self, instance, value, date_range):
        """
        Evento chamado quando o botão "OK" da caixa de diálogo é clicado.
        """
        valueFormated = value.strftime("%d/%m/%Y")
        self.ids.data_contratacao.text = valueFormated
        self.data_contratacao = value.strftime("%Y-%m-%d")

        instance.dismiss()

    def on_save_entrega(self, instance, value, date_range):
        """
        Evento chamado quando o botão "OK" da caixa de diálogo é clicado.
        """
        valueFormated = value.strftime("%d/%m/%Y")
        self.ids.data_entrega.text = valueFormated
        self.data_entrega = value.strftime("%Y-%m-%d")

        instance.dismiss()

    def on_cancel(self, instance, value):
        """
        Evento chamado quando o botão "CANCELAR" da caixa de diálogo é clicado (sem evento).
        """
        pass
    
    def show_date_contratacao(self):
        date_dialog = MDDatePicker()
        date_dialog.title = "CONTRATAÇÃO"
        date_dialog.radius = [20, 7, 20, 7]
        date_dialog.bind(on_save=self.on_save_contratacao, on_cancel=self.on_cancel)
        date_dialog.open()
    
    def show_date_entrega(self):
        date_dialog = MDDatePicker()
        date_dialog.title = "ENTREGA"
        date_dialog.radius = [20, 7, 20, 7]
        date_dialog.bind(on_save=self.on_save_entrega, on_cancel=self.on_cancel)
        date_dialog.open()
    
    def consultarOrcamento(self):
        """
        Método responsável por fazer a busca do RA do cliente no banco de dados.
        """
        try:
            if self.system_crud.read_ID_orcamento_nofilter(self.ids.id_orcamento.text) == False:
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_id_registro_nao_encontrado()
            else:
                self.data_from_database = self.system_crud.read_ID_orcamento_nofilter(self.ids.id_orcamento.text)
                
                # Preenchendo os campos com os dados do cliente
                self.ids.ra_cliente.text = str(self.data_from_database[0][1])
                self.ids.id_servico.text = str(self.data_from_database[0][2])
                self.ids.data_contratacao.text = self.data_from_database[0][3].strftime("%d/%m/%Y")
                self.ids.data_entrega.text = self.data_from_database[0][4].strftime("%d/%m/%Y")
                self.ids.valor_cobrado.text = str(self.data_from_database[0][5])
                self.ids.valor_pendente.text = str(self.data_from_database[0][6])

                situacao = self.data_from_database[0][7]

                if situacao == "PENDENTE":
                    self.situacaoPendente()
                elif situacao == "CONCLUIDO":
                    self.situacaoConcluido()
                elif situacao == "INDEFERIDO":
                    self.situacaoIndeferido()
                else:
                    pass
                
                # Libera os campos para edição
                self.ids.id_orcamento.readonly = True
                self.ids.ra_cliente.readonly = False
                self.ids.id_servico.readonly = False
                self.ids.data_contratacao.readonly = False
                self.ids.data_entrega.readonly = False
                self.ids.valor_cobrado.readonly = False
                self.ids.valor_pendente.readonly = False
                self.ids.btn_data_contratacao.disabled = False
                self.ids.btn_data_entrega.disabled = False
                self.ids.btn_pendente.disabled = False
                self.ids.btn_concluido.disabled = False
                self.ids.btn_indeferido.disabled = False

        except Exception as erro:
            if "NoneType" in str(erro):
                FunctionsCase.popup_id_registro_nao_encontrado()
            print(f"Exceção alterarRegistro: {erro}")

    def finalizarAlteracao(self):
        """
        Método responsável por finalizar a alteração do serviço no banco de dados.
        """
        try:
            if self.ids.ra_cliente == "" or self.ids.id_servico == "" or self.data_contratacao == "" or self.data_entrega == "" or self.ids.valor_cobrado == "" or self.ids.valor_pendente == "" or self.situacao == None:
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_preenchimento()
            else:
                # Verifica/Formata informações
                self.data_contratacao = datetime.strptime(self.ids.data_contratacao.text, "%d/%m/%Y").strftime("%Y-%m-%d")
                self.data_entrega = datetime.strptime(self.ids.data_entrega.text, "%d/%m/%Y").strftime("%Y-%m-%d")
                self.valor_cobrado = self.ids.valor_cobrado.text.replace(",", ".")
                self.valor_pendente = self.ids.valor_pendente.text.replace(",", ".")

                if self.system_crud.update_orcamento(self.ids.id_orcamento.text, self.ids.ra_cliente.text, self.ids.id_servico.text, self.data_contratacao, self.data_entrega, self.valor_cobrado, self.valor_pendente, self.situacao) == True:
                    FunctionsCase.popup_alteracao_sucesso()
                    self.ids.id_orcamento.text = ""
                    self.ids.ra_cliente.text = ""
                    self.ids.id_servico.text = ""
                    self.ids.data_contratacao.text = ""
                    self.ids.data_entrega.text = ""
                    self.ids.valor_cobrado.text = ""
                    self.ids.valor_pendente.text = ""
                    self.ids.icon_pendente.opacity = 0
                    self.ids.icon_concluido.opacity = 0
                    self.ids.icon_indeferido.opacity = 0
                    self.situacao = None

                    # Bloqueia os campos para edição
                    self.ids.id_orcamento.readonly = False
                    self.ids.ra_cliente.readonly = True
                    self.ids.id_servico.readonly = True
                    self.ids.data_contratacao.readonly = True
                    self.ids.data_entrega.readonly = True
                    self.ids.valor_cobrado.readonly = True
                    self.ids.valor_pendente.readonly = True
                    self.ids.btn_data_contratacao.disabled = True
                    self.ids.btn_data_entrega.disabled = True
                    self.ids.btn_pendente.disabled = True
                    self.ids.btn_concluido.disabled = True
                    self.ids.btn_indeferido.disabled = True

                else:
                    FunctionsCase.popup_change_error(self.system_crud.error)
                    self.ids.id_orcamento.text = ""
                    self.ids.ra_cliente.text = ""
                    self.ids.id_servico.text = ""
                    self.ids.data_contratacao.text = ""
                    self.ids.data_entrega.text = ""
                    self.ids.valor_cobrado.text = ""
                    self.ids.valor_pendente.text = ""
                    self.ids.icon_pendente.opacity = 0
                    self.ids.icon_concluido.opacity = 0
                    self.ids.icon_indeferido.opacity = 0
                    self.situacao = None

                    # Bloqueia os campos para edição
                    self.ids.id_orcamento.readonly = False
                    self.ids.ra_cliente.readonly = True
                    self.ids.id_servico.readonly = True
                    self.ids.data_contratacao.readonly = True
                    self.ids.data_entrega.readonly = True
                    self.ids.valor_cobrado.readonly = True
                    self.ids.valor_pendente.readonly = True
                    self.ids.btn_data_contratacao.disabled = True
                    self.ids.btn_data_entrega.disabled = True
                    self.ids.btn_pendente.disabled = True
                    self.ids.btn_concluido.disabled = True
                    self.ids.btn_indeferido.disabled = True

        except Exception as erro:
            print(f"Exceção alterarRegistro: {erro}")

    def resetarCampos(self):
        """
        Método responsável por resetar os campos do formulário.
        """
        self.ids.id_orcamento.text = ""
        self.ids.ra_cliente.text = ""
        self.ids.id_servico.text = ""
        self.ids.data_contratacao.text = ""
        self.ids.data_entrega.text = ""
        self.ids.valor_cobrado.text = ""
        self.ids.valor_pendente.text = ""
        self.ids.icon_pendente.opacity = 0
        self.ids.icon_concluido.opacity = 0
        self.ids.icon_indeferido.opacity = 0
        self.situacao = None

        # Bloqueia os campos para edição
        self.ids.id_orcamento.readonly = False
        self.ids.ra_cliente.readonly = True
        self.ids.id_servico.readonly = True
        self.ids.data_contratacao.readonly = True
        self.ids.data_entrega.readonly = True
        self.ids.valor_cobrado.readonly = True
        self.ids.valor_pendente.readonly = True
        self.ids.btn_data_contratacao.disabled = True
        self.ids.btn_data_entrega.disabled = True
        self.ids.btn_pendente.disabled = True
        self.ids.btn_concluido.disabled = True
        self.ids.btn_indeferido.disabled = True