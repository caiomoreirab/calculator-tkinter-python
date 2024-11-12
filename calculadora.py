from tkinter import * 


janela = Tk()
janela.title("Calculadora")
janela.geometry("400x500")

janela.config(background="black")
janela.iconphoto(False, PhotoImage(file="calculadora.icone.png"))


#Back and 

def clique_botao(valor):
    atual = visor["text"]
    visor.config(text=atual + str(valor))



def calcular():
    try:
        expressao = visor["text"]
        resultado = eval(expressao.replace('÷', '/').replace('x', '*'))
        visor.config(text=str(resultado))
    except Exception as e:
        visor.config(text="Erro")

        
def limpar_visor():
    visor.config(text="")

def porcentagem():
    try:
        expressao = visor["text"]
        resultado = eval(expressao.replace('÷', '/').replace('x', '*')) / 100
        visor.config(text=str(resultado))
    except Exception as e:
        visor.config(text="Erro")



#Visor
visor = Label(janela, width=29, height=3, text = "", font = ("Impact 20 "), fg="#575149", bg="#e1e5ed")
visor.place(x=10, y=10)




#Botoes calculo 
botao_divisao = Button(janela, command= lambda: clique_botao("÷"),  width=5, height=2, text = "÷", font = ("Impact 15 "), fg="white", bg="#ff9500")
botao_divisao.place(x=335 , y=120)

botao_multiplicacao = Button(janela, command= lambda: clique_botao("x"), width=5, height=2, text = "x", font = ("Impact 15 "), fg="white", bg="#ff9500")
botao_multiplicacao.place(x=335 , y=192)

botao_subtracao = Button(janela, command= lambda: clique_botao("-"), width=5, height=2, text = "-", font = ("Impact 15 "), fg="white", bg="#ff9500")
botao_subtracao.place(x=335 , y=264)

botao_adicao = Button(janela, command= lambda: clique_botao("+"), width=5, height=2, text = "+", font = ("Impact 15 "), fg="white", bg="#ff9500")
botao_adicao.place(x=335 , y=336)


#Igualdade  >> Resultado 
botao_igualdade = Button(janela, command=calcular, width=5, height=2, text = "=", font = ("Impact 15 "), fg="white", bg="#ff9500")
botao_igualdade.place(x=335 , y=408)

#Botão Limpr >C 
botao_limpar_tela = Button(janela, command=limpar_visor, width=15, height=2, text = "C", font = ("Impact 15 "), fg="black", bg="#f0ece6")
botao_limpar_tela.place(x=10 , y=120)

#Botão porcentagem 
botao_porcentagem = Button(janela, command=porcentagem, width=15, height=2, text = "%", font = ("Impact 15 "), fg="black", bg="#f0ece6")
botao_porcentagem.place(x=172 , y=120)


#Botões Números 
# 7 8 9 
# 4 5 6 
# 1 2 3 
# 0 
botao_7 = Button(janela, command= lambda: clique_botao(7), width=10, height=2, text = "7", font = ("Impact 15 "), fg="white", bg="#575149")
botao_7.place(x=10 , y=192)

botao_4 = Button(janela, command= lambda: clique_botao(4), width=10, height=2, text = "4", font = ("Impact 15 "), fg="white", bg="#575149")
botao_4.place(x=10 , y=264)

botao_1 = Button(janela,command= lambda: clique_botao(1), width=10, height=2, text = "1", font = ("Impact 15 "), fg="white", bg="#575149")
botao_1.place(x=10 , y=336)


botao_8 = Button(janela, command= lambda: clique_botao(8), width=10, height=2, text = "8", font = ("Impact 15 "), fg="white", bg="#575149")
botao_8.place(x=122 , y=192)

botao_5 = Button(janela, command= lambda: clique_botao(5), width=10, height=2, text = "5", font = ("Impact 15 "), fg="white", bg="#575149")
botao_5.place(x=122 , y=264)

botao_2 = Button(janela, command= lambda: clique_botao(2), width=10, height=2, text = "2", font = ("Impact 15 "), fg="white", bg="#575149")
botao_2.place(x=122 , y=336)


botao_9 = Button(janela, command= lambda: clique_botao(9),  width=9, height=2, text = "9", font = ("Impact 15 "), fg="white", bg="#575149")
botao_9.place(x=234 , y=192)

botao_6 = Button(janela, command= lambda: clique_botao(6),  width=9, height=2, text = "6", font = ("Impact 15 "), fg="white", bg="#575149")
botao_6.place(x=234 , y=264)

botao_3 = Button(janela, command= lambda: clique_botao(3), width=9, height=2, text = "3", font = ("Impact 15 "), fg="white", bg="#575149")
botao_3.place(x=234 , y=336)

botao_0 = Button(janela, command= lambda: clique_botao(0), width=31, height=2, text = "0", font = ("Impact 15 "), fg="black", bg="#f0ece6")
botao_0.place(x=10 , y=408)



janela.mainloop()