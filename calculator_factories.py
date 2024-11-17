import tkinter as tk

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculator') # Define o título da janela como "Calculator".

    root.config(padx=10, pady=10, background='#fff')#Adiciona espaçamento interno (padding) horizontal (padx) e vertical (pady) de 10 pixels.
    root.resizable(False, False) #Impede que o usuário redimensione a janela horizontalmente ou verticalmente.

    return root


def make_label(root) -> tk.Label:
    label = tk.label(
        root, text = 'Sem conta ainda',
        anchor = 'e', justify = 'right', background = '#fff'
    )
    
    label.grid(row=0, column = 0, columnspan = 5, sticky='news')
    return label


'''
Essa função cria o campo de entrada onde o usuário pode digitar números ou expressões
'''
def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column = 0, columnspan = 5, sticky='news', padx=(0, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right', bd=1, relief='flat', 
        highlightthickness=1,  highlightcolor='#ccc'
    )
    display.bind('Control-a', display_control_a) #Associa o atalho Ctrl+A à função display_control_a.
    return display


'''
Essa função manipula o atalho Ctrl+A para selecionar todo o texto no campo de entrada:
'''
def display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('event')
    return 'break'