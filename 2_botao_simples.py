import flet as ft
import random  # Biblioteca do Python para gerar valores aleatórios
import asyncio    # Biblioteca do Python para manipular o tempo

def main(page: ft.Page):
    page.title = "Jogo do Clique Rápido"
    page.padding = 20

    alvo = random.randint(5, 20)  # Número de cliques necessários
    tempo = random.randint(5, 15)  # Tempo limite em segundos
    cliques = 0
    jogo_ativo = True  # Indica se o jogo ainda está em andamento

    mensagem = ft.Text(f"👇 Clique {alvo} vezes em {tempo} segundos!", size=30, text_align=ft.TextAlign.CENTER)
    resultado = ft.Text("", size=20, weight=ft.FontWeight.BOLD)

    async def iniciar_timer(): # Usamos 'async' para que o jogo possa esperar o tempo acabar sem travar a tela.
        nonlocal jogo_ativo
        await asyncio.sleep(tempo)  # Espera o tempo acabar
        if jogo_ativo:  # Só mostra se o jogo ainda não terminou
            jogo_ativo = False
            resultado.value = "⏳ Tempo esgotado! Você perdeu!"
            resultado.color = ft.Colors.RED
            page.update()

    def botao_clicado(e):
        nonlocal cliques, jogo_ativo
        if not jogo_ativo:
            return
        cliques += 1
        mensagem.value = f"🤩 Você clicou {cliques}/{alvo}!"
        if cliques >= alvo:
            jogo_ativo = False
            resultado.value = "🎊 Parabéns! Você venceu!"
            resultado.color = ft.Colors.GREEN
        page.update()  # Atualiza a interface
    
    def resetar_jogo(e):
        nonlocal cliques, jogo_ativo, alvo, tempo
        cliques = 0
        alvo = random.randint(5, 20)
        tempo = random.randint(5, 15)
        jogo_ativo = True
        mensagem.value = f"👇 Clique {alvo} vezes em {tempo} segundos!"
        resultado.value = ""
        resultado.color = ft.Colors.BLACK
        page.update()
        page.run_task(iniciar_timer)


    meu_botao = ft.ElevatedButton(
        text="Clique aqui!",
        on_click=botao_clicado,
        width=200,
        height=50,
        bgcolor=ft.Colors.PINK,
        color=ft.Colors.WHITE
    )

    botao_reset = ft.ElevatedButton(
        text="🔄 Resetar Jogo",
        on_click=resetar_jogo,
        width=200,
        height=50,
        bgcolor=ft.Colors.YELLOW,
        color=ft.Colors.BLACK
    )


    page.add(
        ft.Container(
            content=ft.Column(
            controls=[ mensagem, meu_botao, botao_reset, resultado],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            expand=True 
        )
    )  

    page.run_task(iniciar_timer)

ft.app(target=main)
