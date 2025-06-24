import tkinter as tk

co1 = '#FFFFFF'
co2 = '#1E90FF'
co3 = '#00FFFF'
co4 = '#000000'
co5 = '#00FA9A'

faixas = [
    (18.5, 24.9, "Entre 18,5 e 24,9 – Peso normal"),
    (25, 29.9, "Entre 25 e 29,9 – Sobrepeso"),
    (30, 34.9, "Entre 30 e 34,9 – Obesidade grau 1"),
    (35, 39.9, "Entre 35 e 39,9 – Obesidade grau 2"),
    (40, float('inf'), "Acima de 40 – Obesidade grau 3 (mórbida)")
]

def nivel_imc(imc):
    if imc < 18.5:
        return "Abaixo de 18,5 – Abaixo do peso"
    for minimo, maximo, descricao in faixas:
        if minimo <= imc <= maximo:
            return descricao
    return "Valor inválido"

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)
        resultado['text'] = f"Seu IMC é: {imc:.2f}"
        resultado['bg'] = co3
        resultado['fg'] = co4
        nivel = nivel_imc(imc)
        nivel_label['text'] = f"Nível: {nivel}"
    except ValueError:
        resultado['text'] = "Valores inválidos!"
        resultado['bg'] = co3
        resultado['fg'] = co4
        nivel_label['text'] = ""


janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.configure(bg=co1)
janela.geometry("340x300")


frame = tk.Frame(janela, bg=co2)
frame.pack(pady=20, padx=20, fill='both', expand=True)


tk.Label(frame, text="Peso (kg):", bg=co2, fg=co4, font=("Arial", 10)).pack(pady=5)
entrada_peso = tk.Entry(frame, font=("Arial", 10))
entrada_peso.pack(pady=5)


tk.Label(frame, text="Altura (m):", bg=co2, fg=co4, font=("Arial", 10)).pack(pady=5)
entrada_altura = tk.Entry(frame, font=("Arial", 10))
entrada_altura.pack(pady=5)


botao = tk.Button(janela, text="Calcular IMC", bg=co5, fg=co4, font=("Arial", 12, "bold"), command=calcular_imc)
botao.pack(pady=10)


frame_resultado = tk.Frame(janela, bg=co1)
frame_resultado.pack(pady=5)


resultado = tk.Label(frame_resultado, text="", bg=co1, fg=co4, font=("Arial", 12))
resultado.pack()


nivel_label = tk.Label(frame_resultado, text="", bg=co1, fg=co4, font=("Arial", 10), justify="left")
nivel_label.pack(pady=5)

janela.mainloop()