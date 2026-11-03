import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()

janela.title("Sistema criado por Michael Vieira Silva")
janela.geometry("450x350")
janela.resizable(False, False)

titulo = ctk.CTkLabel(
    janela,
    text="SISTEMA DE CÁLCULO DE DIÁRIAS",
    font=("Arial", 20, "bold"),
    text_color="#f4f5f8"
)
titulo.pack(padx=40, pady=40)

tipo_diaria = ctk.CTkOptionMenu(
    janela,
    values=["Comum", "Especial", "PA comum", "PA especial"]
)
tipo_diaria.pack(pady=10)

dias = ctk.CTkEntry(
    janela,
    placeholder_text="Digite a quantidade de dias",
    width=166,
    height=30
)
dias.pack(pady=10)

mensagem = ctk.CTkLabel(
    janela,
    text="Aguardando cálculo..."
)
mensagem.pack()

def clicar():
    try:
        quantidade = int(dias.get())
        tipo = tipo_diaria.get()

        if tipo == "Comum":
            diaria = 405
            porcentagem = 141.75
            calculo = quantidade * diaria
            total = calculo + porcentagem
            
        elif tipo == "Especial":
            diaria = 608
            porcentagem = 212.80
            calculo = quantidade * diaria
            total = calculo + porcentagem

        elif tipo == "PA comum":
            total = 141.75

        elif tipo == "PA especial":
            total = 212.80
            
   

        valor = f"{total:,.2f}".replace(",","x").replace(".",",").replace("x",".")
       
        mensagem.configure(
            text=f"Diária {tipo.lower()} - {quantidade} dias\nTotal: R$ {valor}",
            font=("Arial", 16, "bold"),
            text_color = "#00ff7f"

        )

        dias.delete(0, "end")
        
    except ValueError:
        mensagem.configure(text="Digite uma quantidade válida!")

botao = ctk.CTkButton(
    janela,
    text= "CALCULAR DIÁRIA",
    width=200,
    height=40,
    command=clicar
    )
botao.pack(pady=20)



janela.mainloop()