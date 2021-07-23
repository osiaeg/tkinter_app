import sys, os, json
from datetime import date as dt
from tkinter import W, messagebox, PhotoImage
from tkinter.ttk import Button, Label, Entry
from ttkthemes import ThemedTk


def take_pay() -> None:
    """
    Create order to take pay from the form
    :return: None
    """

    summa = summ.get()
    if ',' in summa:
        summa = summa.replace(',', '.')
    else:
        summa = str(float(summa))

    number = Number.get()
    date = Date.get()
    distr = Distr.get()
    full_name = FullName.get()
    num_doc = NumDoc.get()

    order = {
        'summa': summa,
        'order': {
            'number': number,
            'date': date,
            'distr': distr
        },
        'client': {
            'fullName': full_name,
            'numDoc': num_doc
        },
        'resident': '1'
    }

    for_human = json.dumps(order, ensure_ascii=False, indent=4)
    print(for_human)

    order = json.dumps(order, ensure_ascii=False)
    ans = messagebox.askyesno('', 'Вы уверены ?', icon='warning')

    if ans:
        command = f'join.exe /new {order}'

        # For windows test
        # os.system('calc.exe')
        os.system(command)

        screen.destroy()


if __name__ == '__main__':
    screen = ThemedTk(theme="breeze")
    img = PhotoImage(file='sber_logo.png')
    screen.wm_iconphoto(True, img)

    screen.resizable(0, 0)
    screen.geometry('350x260')
    screen.title('Take pay')

    # Events
    TSumm = Label(text='Сумма перевода:', font='Consolas')
    summ = Entry(screen, font='Consolas')

    TNumber = Label(text='Номер документа:', font='Consolas')
    Number = Entry(screen, font='Consolas')

    TDate = Label(text='Дата:', font='Consolas')
    Date = Entry(screen, font='Consolas')
    Date.insert(0, dt.today().strftime('%d.%m.%y'))

    TDistr = Label(text='Описание:', font='Consolas')
    Distr = Entry(screen, font='Consolas')

    TFullName = Label(text='ФИО:', font='Consolas')
    FullName = Entry(screen, font='Consolas')

    TNumDoc = Label(text='numDoc:', font='Consolas')
    NumDoc = Entry(screen, font='Consolas')

    # Bind command on button
    enter = Button(text='Совершить перевод',  width=18, command=take_pay)

    # Packers
    TSumm.grid(row=0, column=0, sticky=W, padx=1, pady=1)
    summ.grid(row=0, column=1, padx=1, pady=1)

    TNumber.grid(row=1, column=0, sticky=W, padx=1, pady=1)
    Number.grid(row=1, column=1, padx=1, pady=1)

    TDate.grid(row=2, column=0, sticky=W, padx=1, pady=1)
    Date.grid(row=2, column=1, padx=1, pady=1)

    TDistr.grid(row=3, column=0, sticky=W, padx=1, pady=1)
    Distr.grid(row=3, column=1, padx=1, pady=1)

    TFullName.grid(row=4, column=0, sticky=W, padx=1, pady=1)
    FullName.grid(row=4, column=1, padx=1, pady=1)

    TNumDoc.grid(row=5, column=0, sticky=W, padx=1, pady=1)
    NumDoc.grid(row=5, column=1, padx=1, pady=1)

    enter.grid(row=7, column=0, padx=1, pady=1)

    # The end
    screen.mainloop()
