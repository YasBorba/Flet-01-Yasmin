import flet as ft

def main(page: ft.Page):
    """
    Função principal que será executada quando o app iniciar.
    O parâmetro 'page' representa a tela/pagina do nosso app.
    """

    # Configuraçoes básicas da página
    page.title = "Meu Primeiro App Flet" # Titulo que aparece na aba do navegador 
    page.padding = 20 # Espaçamento interno da página
    page.bgcolor= ft.Colors.BLACK # Fundo escuro para destacar o container

    # Criando nosso primeiro elemento: um texto 
    meu_texto = ft.Text(
        value="🤯 Hello word! (Primeiro app com Flet)", # O texto que sera exbido
        size=28, # Tamanho da fonte
        color=ft.Colors.PINK_400, # Cor do texto
        weight=ft.FontWeight.BOLD, # Texto em negrito
        text_align=ft.TextAlign.CENTER # Centralizar o texto
    )

    subtitulo = ft.Text(
        "Bem-Vindo ao mundo do desenvolvimento mobile!", 
            size=18,
            color=ft.Colors.AMBER_200,
            italic=True,
            text_align=ft.TextAlign.CENTER
    )

    mensagem = ft.Text(
         "Com Flet, você pode criar apps incriveis! 📱", 
            size=18, 
            color=ft.Colors.PURPLE_200,
            weight=ft.FontWeight.W_600,
            text_align=ft.TextAlign.CENTER
    )

    # Container 
    container = ft.Container(
        content= ft.Column(
            controls=[meu_texto, subtitulo, mensagem],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=500,
        padding=20,
        border_radius=15,
        bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
        alignment=ft.alignment.center
    )

    # Adicionando o texto à nossa pagina
    page.add(
        ft.Row(
                controls=[container],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
# Esta linha inicia nosso aplicativo, chamando a função main
ft.app(target=main)

