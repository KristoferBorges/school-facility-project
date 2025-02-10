from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud
from app.support.modulo import FunctionsCase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.popup import Popup


class ConsultaUnica(MDScreen):
    """
    Classe reposável por gerenciar a tela de consulta única.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
    
    def realizarConsultaUnica(self):
        """
        Método ligado ao botão da interface para realizar a consulta única.
        """
        preenchimento = 0

        try:
            if self.ids.ra_cliente.text != "":
                preenchimento += 1
            if self.ids.id_servico.text != "":
                preenchimento += 1
            if self.ids.id_orcamento.text != "":
                preenchimento += 1
            
            if preenchimento == 0:
                # Popup de preenchimento inválido (Nenhum campo preenchido)
                FunctionsCase.popup_preenchimento_unico()
                preenchimento = 0
                
            elif preenchimento > 1:
                # Popup de preenchimento inválido (Apenas um campo deve ser preenchido)
                FunctionsCase.popup_preenchimento_unico()
                preenchimento = 0
                
            else:
                if self.ids.ra_cliente.text != "":
                    # Popup de preenchimento válido (Apenas uma consulta por vez)
                    if self.system_crud.read_RA(self.ids.ra_cliente.text) == False:
                        FunctionsCase.popup_ra_nao_encontrado()

                    else:
                        data_from_database = self.system_crud.read_RA(self.ids.ra_cliente.text)

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
                        header_layout.add_widget(Label(text="Status", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))

                        content_layout.add_widget(header_layout)

                        # Adicionando itens ao layout
                        # Criando rótulos para cada coluna
                        ra_label = Label(text=str(data_from_database[0][0]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                        nome_label = Label(text=str(data_from_database[0][1]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                        semestre_label = Label(text=str(data_from_database[0][2]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                        data_registro_label = Label(text=str(data_from_database[0][3]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                        status_label = Label(text=str(data_from_database[0][5]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")

                        # Adicionando rótulos ao layout
                        row_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="20dp")
                        row_layout.add_widget(ra_label)
                        row_layout.add_widget(nome_label)
                        row_layout.add_widget(semestre_label)
                        row_layout.add_widget(data_registro_label)
                        row_layout.add_widget(status_label)

                        content_layout.add_widget(row_layout)

                        # Ajustando o tamanho da altura dinamicamente
                        content_layout.height = len(data_from_database) * (66 + 3)  # Altura de uma linha + espaçamento entre as linhas

                        # Adicionando um botão para fechar o popup
                        close_button = MDFillRoundFlatButton(text="VOLTAR", font_size="15dp", size_hint=(0.2, None), font_name="app/support/fonts/monofonto.otf", height="15dp", pos_hint={"center_x": 0.5, "center_y": 0.1}, text_color=(0, 0, 0, 1), md_bg_color=[1, 3, 3, 0.7])

                        # Adicionando o layout ao ScrollView
                        scroll_view.add_widget(content_layout)

                        # Criando o layout do popup
                        popup_layout = BoxLayout(orientation="vertical")
                        popup_layout.add_widget(scroll_view)
                        popup_layout.add_widget(close_button)

                        # Criando o popup
                        popup = Popup(title="Consulta de cliente", content=popup_layout, size_hint=(0.8, 0.3), auto_dismiss=True)
                        close_button.bind(on_release=popup.dismiss)

                        # Exibindo o popup
                        popup.open()

                elif self.ids.id_servico.text != "":
                    # Popup de preenchimento válido (Apenas uma consulta por vez)
                    if self.system_crud.read_ID_service(self.ids.id_servico.text) == False:
                        FunctionsCase.popup_id_nao_encontrado()
                    else:
                        data_from_database = self.system_crud.read_ID_service(self.ids.id_servico.text)

                        # Criando um ScrollView
                        scroll_view = ScrollView()

                        # Layout para conter os itens da lista
                        content_layout = BoxLayout(orientation="vertical", padding="10dp", spacing="5dp", size_hint_y=None)

                        # Adicionando o cabeçalho
                        header_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="30dp")
                        header_layout.add_widget(Label(text="ID", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Nome", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Valor", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Dependência", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf"))

                        content_layout.add_widget(header_layout)

                        # Adicionando itens ao layout
                        # Criando rótulos para cada coluna
                        id_label = Label(text=str(data_from_database[0][0]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                        nome_label = Label(text=str(data_from_database[0][1]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                        valor_label = Label(text=str(data_from_database[0][2]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                        dependencia_label = Label(text=str(data_from_database[0][3]), halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")

                        # Adicionando rótulos ao layout
                        row_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="20dp")
                        row_layout.add_widget(id_label)
                        row_layout.add_widget(nome_label)
                        row_layout.add_widget(valor_label)
                        row_layout.add_widget(dependencia_label)

                        content_layout.add_widget(row_layout)

                        # Ajustando o tamanho da altura dinamicamente
                        content_layout.height = len(data_from_database) * (66 + 3)  # Altura de uma linha + espaçamento entre as linhas

                        # Adicionando um botão para fechar o popup
                        close_button = MDFillRoundFlatButton(text="VOLTAR", font_size="15dp", size_hint=(0.2, None), font_name="app/support/fonts/monofonto.otf", height="15dp", pos_hint={"center_x": 0.5, "center_y": 0.1}, text_color=(0, 0, 0, 1), md_bg_color=[1, 3, 3, 0.7])

                        # Adicionando o layout ao ScrollView
                        scroll_view.add_widget(content_layout)

                        # Criando o layout do popup
                        popup_layout = BoxLayout(orientation="vertical")
                        popup_layout.add_widget(scroll_view)
                        popup_layout.add_widget(close_button)

                        # Criando o popup
                        popup = Popup(title="Consulta de Serviço", content=popup_layout, size_hint=(0.8, 0.3), auto_dismiss=True)
                        close_button.bind(on_release=popup.dismiss)

                        # Exibindo o popup
                        popup.open()

                elif self.ids.id_orcamento.text != "":
                    # Popup de preenchimento válido (Apenas uma consulta por vez)
                    if self.system_crud.read_ID_orcamento(self.ids.id_orcamento.text) == False:
                        FunctionsCase.popup_id_nao_encontrado()
                    else:
                        data_from_database = self.system_crud.read_ID_orcamento(self.ids.id_orcamento.text)

                        # Criando um ScrollView
                        scroll_view = ScrollView()

                        # Layout para conter os itens da lista
                        content_layout = BoxLayout(orientation="vertical", padding="10dp", spacing="5dp", size_hint_y=None)

                        # Adicionando o cabeçalho
                        header_layout = BoxLayout(orientation="horizontal", padding="13dp", spacing="13dp", size_hint_y=None, height="30dp")
                        header_layout.add_widget(Label(text="ID", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Nome", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Serviço", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Cobrado", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Contratação", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Entrega", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Pendência", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))
                        header_layout.add_widget(Label(text="Situação", halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf"))

                        content_layout.add_widget(header_layout)

                        # Adicionando itens ao layout
                        # Criando rótulos para cada coluna
                        id_label = Label(text=str(data_from_database[0][0]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                        nome_label = Label(text=str(data_from_database[0][1]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                        servico_label = Label(text=str(data_from_database[0][2]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                        cobrado_label = Label(text=str(data_from_database[0][3]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                        contratacao_label = Label(text=str(data_from_database[0][4]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                        entrega_label = Label(text=str(data_from_database[0][5]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                        pendencia_label = Label(text=str(data_from_database[0][6]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")
                        situacao_label = Label(text=str(data_from_database[0][7]), halign="center", font_size="12dp", font_name="app/support/fonts/monofonto.otf")

                        # Adicionando rótulos ao layout
                        row_layout = BoxLayout(orientation="horizontal", padding="10dp", spacing="10dp", size_hint_y=None, height="20dp")
                        row_layout.add_widget(id_label)
                        row_layout.add_widget(nome_label)
                        row_layout.add_widget(servico_label)
                        row_layout.add_widget(cobrado_label)
                        row_layout.add_widget(contratacao_label)
                        row_layout.add_widget(entrega_label)
                        row_layout.add_widget(pendencia_label)
                        row_layout.add_widget(situacao_label)


                        content_layout.add_widget(row_layout)

                        # Ajustando o tamanho da altura dinamicamente
                        content_layout.height = len(data_from_database) * (66 + 3)  # Altura de uma linha + espaçamento entre as linhas

                        # Adicionando um botão para fechar o popup
                        close_button = MDFillRoundFlatButton(text="VOLTAR", font_size="15dp", size_hint=(0.2, None), font_name="app/support/fonts/monofonto.otf", height="15dp", pos_hint={"center_x": 0.5, "center_y": 0.1}, text_color=(0, 0, 0, 1), md_bg_color=[1, 3, 3, 0.7])

                        # Adicionando o layout ao ScrollView
                        scroll_view.add_widget(content_layout)

                        # Criando o layout do popup
                        popup_layout = BoxLayout(orientation="vertical")
                        popup_layout.add_widget(scroll_view)
                        popup_layout.add_widget(close_button)

                        # Criando o popup
                        popup = Popup(title="Consulta de Orçamento", content=popup_layout, size_hint=(1, 0.3), auto_dismiss=True)
                        close_button.bind(on_release=popup.dismiss)

                        # Exibindo o popup
                        popup.open()

        except Exception as error:
            preenchimento = 0
            
            if "NoneType" in str(error):
                FunctionsCase.popup_search_error()
                
            print(f"Exceção ConsultaÚnica: {error}")
    