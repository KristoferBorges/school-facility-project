from datetime import datetime
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
from app.support.modulo import FunctionsCase
from app.support.setup import System_Crud
from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

class NewService(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
        self.data_entrega = None
        self.data_atual = datetime.now().strftime("%Y-%m-%d")

    def on_save(self, instance, value, date_range):
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

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.title = "DATA DE ENTREGA"
        date_dialog.radius = [20, 7, 20, 7]
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        self.ids.data_registro.text = datetime.now().strftime("%d/%m/%Y")
        date_dialog.open()

    def show_date(self):
        """
        Mostra a data atual ao clicar no botão
        """
        self.ids.data_registro.text = datetime.now().strftime("%d/%m/%Y")

    def consultarClientes(self):
        """
        Aplica a função de consulta de clientes mostrando os dados em um popup
        """
        try:
            if self.system_crud.read_clients() == False:
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_search_error()
            else:
                data_from_database = self.system_crud.read_clients()

                # Criando um ScrollView
                scroll_view = ScrollView()

                # Layout para conter os itens da lista
                content_layout = BoxLayout(orientation="vertical", padding="10dp", spacing="5dp", size_hint_y=None)

                # Adicionando o cabeçalho
                header_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="30dp")
                header_layout.add_widget(Label(text="RA", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Nome", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Semestre", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Data_Registro", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))

                content_layout.add_widget(header_layout)

                # Adicionando itens ao layout
                for item in data_from_database:
                    # Criando rótulos para cada coluna
                    ra_label = Label(text=str(item[0]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    nome_label = Label(text=str(item[1]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    semestre_label = Label(text=str(item[2]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    data_registro_label = Label(text=str(item[3]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")

                    # Adicionando rótulos ao layout
                    row_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="20dp")
                    row_layout.add_widget(ra_label)
                    row_layout.add_widget(nome_label)
                    row_layout.add_widget(semestre_label)
                    row_layout.add_widget(data_registro_label)

                    content_layout.add_widget(row_layout)

                # Ajustando o tamanho da altura dinamicamente
                content_layout.height = len(data_from_database) * (25 + 3)  # Altura de uma linha + espaçamento entre as linhas

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
            print(f"Exceção newService: {erro}")

    def consultarServices(self):
        """
        Aplica a função de consulta de serviços mostrando os dados em um popup
        """
        try:
            if self.system_crud.read_services() == False:
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_search_error()
            else:
                data_from_database = self.system_crud.read_services()

                # Criando um ScrollView
                scroll_view = ScrollView()

                # Layout para conter os itens da lista
                content_layout = BoxLayout(orientation="vertical", padding="10dp", spacing="5dp", size_hint_y=None)

                # Adicionando o cabeçalho
                header_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="30dp")
                header_layout.add_widget(Label(text="ID", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Nome", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Valor", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                header_layout.add_widget(Label(text="Status", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))

                content_layout.add_widget(header_layout)

                # Adicionando itens ao layout
                for item in data_from_database:
                    # Criando rótulos para cada coluna
                    id_label = Label(text=str(item[0]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    nome_label = Label(text=str(item[1]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    valor_label = Label(text=str(item[2]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                    status_label = Label(text=str(item[3]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")

                    # Adicionando rótulos ao layout
                    row_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="20dp")
                    row_layout.add_widget(id_label)
                    row_layout.add_widget(nome_label)
                    row_layout.add_widget(valor_label)
                    row_layout.add_widget(status_label)

                    content_layout.add_widget(row_layout)

                # Ajustando o tamanho da altura dinamicamente
                content_layout.height = len(data_from_database) * (30 + 3)  # Altura de uma linha + espaçamento entre as linhas

                # Adicionando um botão para fechar o popup
                close_button = MDFillRoundFlatButton(text="VOLTAR", font_size="15dp", size_hint=(0.2, None), font_name="app/support/fonts/monofonto.otf", height="15dp", pos_hint={"center_x": 0.5, "center_y": 0.1}, text_color=(0, 0, 0, 1), md_bg_color=[1, 3, 3, 0.7])

                # Adicionando o layout ao ScrollView
                scroll_view.add_widget(content_layout)

                # Criando o layout do popup
                popup_layout = BoxLayout(orientation="vertical")
                popup_layout.add_widget(scroll_view)
                popup_layout.add_widget(close_button)

                # Criando o popup
                popup = Popup(title="Consulta de serviços", content=popup_layout, size_hint=(0.8, 0.8), auto_dismiss=True)
                close_button.bind(on_release=popup.dismiss)

                # Exibindo o popup
                popup.open()

        except Exception as erro:
            print(f"Exceção newService: {erro}")

    def finalizarRegistro(self):
        """
        Função responsável por analisar os campos preenchidos e utilizar a função de cadastro do sistema
        """
        try:
            if (self.ids.busca_ra_cliente.text == "") or (self.ids.busca_service.text == "") or (self.ids.valor_cobrado.text == "") or (self.ids.valor_pendente.text == "") or (self.data_entrega == None) or (self.data_atual == None):
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_preenchimento()

            elif (self.system_crud.read_RA(self.ids.busca_ra_cliente.text) == False):
                # Pop-up de RA não encontrado
                FunctionsCase.popup_ra_nao_encontrado()

            elif (self.system_crud.read_ID_service(self.ids.busca_service.text) == False):
                # Pop-up de ID Service não encontrado
                FunctionsCase.popup_id_nao_encontrado()

            else:
                self.system_crud.conectar_banco()
                print(self.data_atual, self.data_entrega)
                if self.system_crud.registerNewService(self.ids.busca_ra_cliente.text, self.ids.busca_service.text, self.data_atual, self.data_entrega, self.ids.valor_cobrado.text, self.ids.valor_pendente.text) == True:
                    self.ids.busca_ra_cliente.text = ""
                    self.ids.busca_service.text = ""
                    self.ids.valor_cobrado.text = ""
                    self.ids.valor_pendente.text = ""
                    self.ids.data_entrega.text = "00/00/0000"
                    self.ids.data_registro.text = "00/00/0000"
                    FunctionsCase.popup_cadastro_sucesso()
        except Exception as erro:
            print(f"Exceção newService: {erro}")