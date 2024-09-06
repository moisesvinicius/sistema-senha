
import string
import tkinter as tk
import tkinter.messagebox as mb


def logica_do_sistema():
    if entrada_senha.get() == '':
        return mb.showerror('Error', 'Preencha o campo de senha.')
    else:
    # Verifica se a senha é segura ou não
        comprimento_minimo = 8
        tem_letra = any(co in string.ascii_letters for co in entrada_senha.get())
        tem_digitos = any(co in string.digits for co in entrada_senha.get())
        tem_caracteres_especial = any(co in string.punctuation for co in entrada_senha.get())
        comprimento_adequado = len(entrada_senha.get()) >= comprimento_minimo
        if comprimento_adequado and tem_letra and tem_digitos and tem_caracteres_especial:
            mb.showinfo('SENHA FORTE', 'Sua senha está otimá, e sera dificil de ser quebrada.')
            entrada_senha.delete(0, tk.END)
            return
        else:
            mb.showerror('Senha vulneravel', 'Essa senha pode ser vulneravel a ataque de força bruta')
            entrada_senha.delete(0, tk.END)
            return
        



# Janela do sistema
window = tk.Tk()
window.iconbitmap('img/padlock.ico')
window.title('SISTEMA DE SENHA')
window.geometry('520x500')
window.config(bg='#1C1C1C')

texto_principal = tk.Label(window, text='CRIE UMA SENHA SEGURA', font=('Arial', 20), fg='red', bg='#1C1C1C')
texto_principal.place(x=85, y=32)

texto_senha = tk.Label(window, text='DIGITE SUA SENHA ABAIXO:', font='Arial 16', fg='white', bg='#1C1C1C')
texto_senha.place(x=115, y=128)

# Cria um widget Entry para senha com fonte ajustada
entrada_senha = tk.Entry(window, width=30, font=('Arial', 16),bd=5,relief='solid')  # Ajusta a fonte para tamanho 16
entrada_senha.place(x=70, y=220)  # Posiciona o widget na janela

btn = tk.Button(window, text='Envia',width=10, height=1, font=('Arial', 14), cursor='hand2', bg='green', fg='white', command=logica_do_sistema)
btn.place(x=190, y=300)

window.mainloop()