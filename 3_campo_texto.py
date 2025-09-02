import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.bgcolor = ft.Colors.WHITE
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Titulo estilizado
    titulo = ft.Text(
        "Vamos nos conhecer! 😆",
        size=26,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.PURPLE_700,
        text_align=ft.TextAlign.CENTER
    )
    # Criando campos para o usuario digitar o nome e a idade
    campo_nome = ft.TextField(
        label="Digite seu nome aqui", # Texto de orientação
        width=350, #Largura do campo
        border_color=ft.Colors.PURPLE, # Cor da borda
        focused_border_color=ft.Colors.PURPLE_500,
        cursor_color=ft.Colors.PURPLE_700,
        bgcolor=ft.Colors.PURPLE_50,
        border_radius=10,
        text_style=ft.TextStyle(color=ft.Colors.PURPLE_900)
    )
   
    campo_idade = ft.TextField(
        label="Digite sua idade aqui",
        width=350,
        border_color=ft.Colors.PURPLE_300,
        focused_border_color=ft.Colors.PURPLE_500,
        cursor_color=ft.Colors.PURPLE_700,
        bgcolor=ft.Colors.PURPLE_50,
        border_radius=10,
        text_style=ft.TextStyle(color=ft.Colors.PURPLE_900)
    )

    # Texto que mostrara a resposta 
    resposta = ft.Text(value="", size=18, text_align=ft.TextAlign.CENTER,  color=ft.Colors.PURPLE_700)

    # Processar as informações obtidas 
    def processar(evento):

        # Pegando os valores digitados no campo
        nome = campo_nome.value
        idade_txt = campo_idade.value

        # validação do nome
        if not nome or len(nome) < 2:
            resposta.value = "⚠️ Digite um nome válido!"
            resposta.color = ft.Colors.RED_400
            page.update()
            return

        # validação da idade
        if not idade_txt.isdigit():
            resposta.value = "⚠️ Digite uma idade válida!"
            resposta.color = ft.Colors.RED_400
            page.update()
            return

        idade = int(idade_txt)

        # monta mensagem com nome + idade de acordo com a idade digitada
        if idade < 12: # menor de 12 anos 
            resposta.value = f"🩷 Olá {nome}, você tem {idade} anos e é uma criança!"
        elif idade < 18: # menor de 18 anos
            resposta.value = f"💙 Olá {nome}, você tem {idade} anos e é adolescente!"
        elif idade < 60: # menor de 60 anos 
            resposta.value = f"💛 Olá {nome}, você tem {idade} anos e é adulto!"
        else: # mais que 60 anos 
            resposta.value = f"💚 Olá {nome}, você tem {idade} anos e é idoso!"

        # Resposta mostrada para o usuario
        resposta.color = ft.Colors.PURPLE
        # Atualiza a pagina
        page.update()

    # Botão para processar as informações
    botao_ok = ft.ElevatedButton(
        text="Confirmar ✨",
        on_click=processar,  # apenas uma função
        width=180,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PURPLE_500,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
            elevation=4
        )
    )

    # Adicionando os elementos à pagina
    page.add(
        ft.Column(
            controls=[campo_nome, campo_idade, botao_ok, resposta],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )        
ft.app(target=main)
