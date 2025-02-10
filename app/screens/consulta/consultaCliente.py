from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.popup import Popup
from app.support.modulo import FunctionsCase

class ConsultaCliente(MDScreen):
    """
    Classe responsável por gerenciar a tela de consulta de clientes
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
        self.filter = None

    def consultClientFilter(self):
        """
        Aplica a função de consulta de clientes mostrando os dados em um popup
        """
        try:
            if self.system_crud.read_clients() == False:
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_search_error()
            else:
                data_from_database = self.system_crud.read_clients(self.filter)

                # Criando um ScrollView
                scroll_view = ScrollView()

                # Layout para conter os itens da lista
                content_layout = BoxLayout(orientation="vertical", padding="10dp", spacing="5dp", size_hint_y=None)

                # Adicionando o cabeçalho
                header_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="30dp")
                header_layout.add_widget(Label(text="RA", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Nome", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Semestre", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Registro", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Status", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))

                content_layout.add_widget(header_layout)

                # Adicionando itens ao layout
                for item in data_from_database:
                    # Criando rótulos para cada coluna
                    ra_label = Label(text=str(item[0]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    nome_label = Label(text=str(FunctionsCase.formatNome(item[1])), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    semestre_label = Label(text=str(item[2]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    data_registro_label = Label(text=str(item[3]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    status_label = Label(text=str(item[5]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")

                    # Adicionando rótulos ao layout
                    row_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="20dp")
                    row_layout.add_widget(ra_label)
                    row_layout.add_widget(nome_label)
                    row_layout.add_widget(semestre_label)
                    row_layout.add_widget(data_registro_label)
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
                popup = Popup(title="Consulta de clientes", content=popup_layout, size_hint=(0.8, 0.8), auto_dismiss=True)
                close_button.bind(on_release=popup.dismiss)

                # Exibindo o popup
                popup.open()

        except Exception as erro:
            print(f"Exceção consultaCliente: {erro}")
    
    def filterRA(self):
        """
        Função ligada ao botão para filtrar por RA
        """
        self.ids.ra_filter.opacity = 1
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 0
        self.ids.registro_filter.opacity = 0
        self.filter = "RA"

    def filterNome(self):
        """
        Função ligada ao botão para filtrar por Nome
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 1
        self.ids.semestre_filter.opacity = 0
        self.ids.registro_filter.opacity = 0
        self.filter = "Nome"

    def filterSemestre(self):
        """
        Função ligada ao botão para filtrar por Semestre
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 1
        self.ids.registro_filter.opacity = 0
        self.filter = "Semestre"

    def filterRegistro(self):
        """
        Função ligada ao botão para filtrar por Registro
        """
        self.ids.ra_filter.opacity = 0
        self.ids.nome_filter.opacity = 0
        self.ids.semestre_filter.opacity = 0
        self.ids.registro_filter.opacity = 1
        self.filter = "Registro"