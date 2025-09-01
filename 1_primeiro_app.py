import flet as ft

def main(page: ft.Page):
    """
    Função principal que será executada quando o app iniciar.
    O parâmetro 'page' representa a tela/pagina do nosso app.
    """

    # Configuraçoes básicas da página
    page.title = "Meu Primeiro App Flet" # Titulo que aparece na aba do navegador 
    page.padding = 20 # Espaçamento interno da página

    # Criando nosso primeiro elemento: um texto 
    meu_texto = ft.Text(
        value="🤯 Hello word! (Primeiro app com Flet)", # O texto que sera exbido
        size=24, # Tamanho da fonte
        color=ft.Colors.BLUE, # Cor do texto
        weight=ft.FontWeight.BOLD, # Texto em negrito
        text_align=ft.TextAlign.CENTER # Centralizar o texto
    )

    # Adicionando o texto à nossa pagina
    page.add(meu_texto)

    # Vamos adicionar mais alguns elementos para tornar mais interessante
    page.add(
        ft.Text("Bem-Vindo ao mundo do desenvolvimento mobile!", size=16),
        ft.Text("Com Flet, você pode criar apps incriveis! 📱", size=16, color=ft.Colors.GREEN)
    )

# Esta linha inicia nosso aplicativo, chamando a função main
ft.app(target=main)

