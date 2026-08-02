import flet as ft
import google.generativeai as genai
import os
import fastapi

# Pega a chave que cadastramos na Vercel
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

def main(page: ft.Page):
    page.title = "Meu App de IA"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.END

    chat = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)
    
    def enviar_mensagem(e):
        if not campo_texto.value:
            return
        
        user_msg = campo_texto.value
        chat.controls.append(ft.Text(f"Você: {user_msg}", color=ft.Colors.BLUE_400, size=16))
        campo_texto.value = ""
        page.update()

        if not api_key:
            chat.controls.append(ft.Text("IA: Erro! Chave API não configurada na Vercel.", color=ft.Colors.RED_400))
            page.update()
            return

        try:
            response = model.generate_content(user_msg)
            ia_response = response.text
        except Exception:
            ia_response = "Erro ao conectar com a IA. Verifique sua internet."

        chat.controls.append(ft.Text(f"IA: {ia_response}", color=ft.Colors.GREEN_400, size=16))
        page.update()

    campo_texto = ft.TextField(hint_text="Digite sua mensagem...", expand=True, on_submit=enviar_mensagem)
    botao_enviar = ft.IconButton(icon=ft.Icons.SEND, on_click=enviar_mensagem)

    linha_input = ft.Row(controls=[campo_texto, botao_enviar])
    page.add(ft.Container(content=chat, expand=True, padding=20), linha_input)

app = ft.app(target=main, export_asgi=True)
