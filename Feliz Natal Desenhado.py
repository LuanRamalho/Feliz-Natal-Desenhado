import tkinter as tk
from tkinter import CENTER

# Função principal
def criar_interface():
    # Criando a janela principal
    janela = tk.Tk()
    janela.title("Feliz Natal!")
    janela.geometry("800x400")
    janela.configure(bg="#1d3557")  # Cor de fundo azul escuro

    # Criando o canvas para desenhar
    canvas = tk.Canvas(janela, width=800, height=400, bg="#1d3557", highlightthickness=0)
    canvas.pack()

    # Adicionando o texto "Feliz Natal" com estilos vibrantes
    canvas.create_text(
        400, 150, 
        text="Feliz Natal", 
        fill="#e63946",  # Cor vermelha
        font=("Comic Sans MS", 70, "bold"),
        anchor=CENTER
    )

    # Adicionando detalhes decorativos
    canvas.create_oval(50, 50, 120, 120, fill="#f4a261", outline="#f4a261")  # Bola dourada
    canvas.create_oval(680, 50, 750, 120, fill="#2a9d8f", outline="#2a9d8f")  # Bola verde
    canvas.create_polygon(400, 300, 350, 400, 450, 400, fill="#e76f51")  # Triângulo estilizado como base

    # Exibindo a janela
    janela.mainloop()

# Chamando a função principal
if __name__ == "__main__":
    criar_interface()
