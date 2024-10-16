import tkinter as tk

janela = tk.Tk()

janela.title("exemplo de imagem com photoimage")

imagem = tk.PhotoImage(file="png-transparent-sport-sports-woman-business-woman-child-image-file-formats-thumbnail.png")

rotulo = tk.Label(janela, image=imagem)
rotulo.pack()

janela.mainloop()