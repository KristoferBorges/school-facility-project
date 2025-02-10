from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud
from app.support.modulo import FunctionsCase
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.popup import Popup

class ConsultaOrcamento(MDScreen):
    """
    Classe responsável por gerenciar a tela de consulta de orçamentos
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
        self.filter = None
    
    def consultOrcamentoFilter(self):
        """
        Classe responsável por gerencia a tela de consulta de orçamentos
        """
        try:
            if self.system_crud.read_client_service() == False:
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_search_error()
            else:
                data_from_database = self.system_crud.read_client_service(self.filter)

                # Criando um ScrollView
                scroll_view = ScrollView()

                # Layout para conter os itens da lista
                content_layout = BoxLayout(orientation="vertical", padding="10dp", spacing="5dp", size_hint_y=None)

                # Adicionando o cabeçalho
                header_layout = BoxLayout(orientation="horizontal", padding="13dp", spacing="13dp", size_hint_y=None, height="30dp")
                header_layout.add_widget(Label(text="ID", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Nome", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Serviço", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Valor", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Contratação", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Entrega", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Pendência", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Status", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))

                content_layout.add_widget(header_layout)

                # Adicionando itens ao layout
                for item in data_from_database:
                    # Criando rótulos para cada coluna
                    id_label = Label(text=str(item[0]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                    nome_label = Label(text=str(FunctionsCase.formatNome(item[1])), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                    servico_label = Label(text=str(item[2]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                    valor_cobrado_label = Label(text=str(item[3]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                    contratacao_label = Label(text=str(item[4]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                    entrega_label = Label(text=str(item[5]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                    pendencia_label = Label(text=str(item[6]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                    status_label = Label(text=str(item[7]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                
                    row_layout = BoxLayout(orientation="horizontal", padding="13dp", spacing="13dp", size_hint_y=None, height="20dp")
                    row_layout.add_widget(id_label)
                    row_layout.add_widget(nome_label)
                    row_layout.add_widget(servico_label)
                    row_layout.add_widget(valor_cobrado_label)
                    row_layout.add_widget(contratacao_label)
                    row_layout.add_widget(entrega_label)
                    row_layout.add_widget(pendencia_label)
                    row_layout.add_widget(status_label)

                    content_layout.add_widget(row_layout)

                # Ajustando o tamanho da altura dinamicamente
                content_layout.height = len(data_from_database) * (23 + 3)  # Altura de uma linha + espaçamento entre as linhas

                # Adicionando um botão para fechar o popup
                close_button = MDFillRoundFlatButton(text="VOLTAR", font_size="15dp", size_hint=(0.2, None), font_name="app/support/fonts/monofonto.otf", height="15dp", pos_hint={"center_x": 0.5, "center_y": 0.1}, text_color=(0, 0, 0, 1), md_bg_color=[1, 3, 3, 0.7])

                # Adicionando o layout ao ScrollView
                scroll_view.add_widget(content_layout)

                # Criando o layout do popup
                popup_layout = BoxLayout(orientation="vertical")
                popup_layout.add_widget(scroll_view)
                popup_layout.add_widget(close_button)

                # Criando o popup
                popup = Popup(title="Consulta de Orçamentos", content=popup_layout, size_hint=(0.98, 0.98), auto_dismiss=True)
                close_button.bind(on_release=popup.dismiss)

                # Exibindo o popup
                popup.open()

        except Exception as erro:
            print(f"Exceção consultaOrçamento: {erro}")
    
    def filterRA(self):
        """
        Função ligada ao botão para filtrar por RA
        """
        self.ids.ra_filter.opacity = 1
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 0
        self.ids.servico_filter.opacity = 0
        self.ids.valor_cobrado_filter.opacity = 0
        self.ids.contratacao_filter.opacity = 0
        self.ids.entrega_filter.opacity = 0
        self.ids.pendencia_filter.opacity = 0
        self.ids.status_filter.opacity = 0
        self.filter = "RA"

    def filterNome(self):
        """
        Função ligada ao botão para filtrar por Nome
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 1
        self.ids.semestre_filter.opacity = 0
        self.ids.servico_filter.opacity = 0
        self.ids.valor_cobrado_filter.opacity = 0
        self.ids.contratacao_filter.opacity = 0
        self.ids.entrega_filter.opacity = 0
        self.ids.pendencia_filter.opacity = 0
        self.ids.status_filter.opacity = 0
        self.filter = "Nome"

    def filterServico(self):
        """
        Função ligada ao botão para filtrar por Serviço
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 0
        self.ids.servico_filter.opacity = 1
        self.ids.valor_cobrado_filter.opacity = 0
        self.ids.contratacao_filter.opacity = 0
        self.ids.entrega_filter.opacity = 0
        self.ids.pendencia_filter.opacity = 0
        self.ids.status_filter.opacity = 0
        self.filter = "Serviço"

    def filterValorCobrado(self):
        """
        Função ligada ao botão para filtrar por Valor Cobrado
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 0
        self.ids.servico_filter.opacity = 0
        self.ids.valor_cobrado_filter.opacity = 1
        self.ids.contratacao_filter.opacity = 0
        self.ids.entrega_filter.opacity = 0
        self.ids.pendencia_filter.opacity = 0
        self.ids.status_filter.opacity = 0
        self.filter = "ValorCobrado"

    def filterContratacao(self):
        """
        Função ligada ao botão para filtrar por Contratação
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 0
        self.ids.servico_filter.opacity = 0
        self.ids.valor_cobrado_filter.opacity = 0
        self.ids.contratacao_filter.opacity = 1
        self.ids.entrega_filter.opacity = 0
        self.ids.pendencia_filter.opacity = 0
        self.ids.status_filter.opacity = 0
        self.filter = "DataContratação"

    def filterEntrega(self):
        """
        Função ligada ao botão para filtrar por Entrega
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 0
        self.ids.servico_filter.opacity = 0
        self.ids.valor_cobrado_filter.opacity = 0
        self.ids.contratacao_filter.opacity = 0
        self.ids.entrega_filter.opacity = 1
        self.ids.pendencia_filter.opacity = 0
        self.ids.status_filter.opacity = 0
        self.filter = "DataEntrega"

    def filterPendencia(self):
        """
        Função ligada ao botão para filtrar por Pendência
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 0
        self.ids.servico_filter.opacity = 0
        self.ids.valor_cobrado_filter.opacity = 0
        self.ids.contratacao_filter.opacity = 0
        self.ids.entrega_filter.opacity = 0
        self.ids.pendencia_filter.opacity = 1
        self.ids.status_filter.opacity = 0
        self.filter = "Pendência"

    def filterStatus(self):
        """
        Função ligada ao botão para filtrar por Status
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 0
        self.ids.servico_filter.opacity = 0
        self.ids.valor_cobrado_filter.opacity = 0
        self.ids.contratacao_filter.opacity = 0
        self.ids.entrega_filter.opacity = 0
        self.ids.pendencia_filter.opacity = 0
        self.ids.status_filter.opacity = 1
        self.filter = "Status"