import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Criando campos para o usuario digitar o nome e a idade
    campo_nome = ft.TextField(
        label="Digite seu nome aqui", # Texto de orientação
        width=300, #Largura do campo
        border_color=ft.Colors.PINK # Cor da borda
    )

    campo_idade = ft.TextField(
        label="Digite sua idade aqui",
        width=300,
        border_color=ft.Colors.PINK,
    )

    # Texto que mostrara a resposta 
    resposta = ft.Text(value="", size=18, text_align=ft.TextAlign.CENTER)

    # Processar as informações obtidas 
    def processar(evento):

        # Pegando os valores digitados no campo
        nome = campo_nome.value
        idade_txt = campo_idade.value

        # validação do nome
        if not nome or len(nome) < 2:
            resposta.value = "⚠️ Digite um nome válido!"
            resposta.color = ft.Colors.RED
            page.update()
            return

        # validação da idade
        if not idade_txt.isdigit():
            resposta.value = "⚠️ Digite uma idade válida!"
            resposta.color = ft.Colors.RED
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
        color = ft.Colors.CYAN,
        on_click=processar,  # apenas uma função
        width=150
    )

    # Adicionando os elementos à pagina
    page.add(
        ft.Text("Vamos nos conhecer!🍩", size=22, weight=ft.FontWeight.BOLD),
        campo_nome,
        campo_idade,
        botao_ok,
        resposta
    )

ft.app(target=main)
