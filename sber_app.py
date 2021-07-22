from tkinter import Button, Label, Entry, W, Tk, messagebox
import os, sys, json
from datetime import date as dt


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

    ans = messagebox.askyesno('Question', 'Are you sure ?', icon='warning')

    if ans:
        util = os.path.abspath('join.txt')
        command = f"{util} /new {order}"
        print(command)

        # For windows test
        # os.system('calc.exe')

        # For windows test
        os.system('neofetch')
        sys.exit(1)


if __name__ == '__main__':
    screen = Tk()
    #screen.iconbitmap('F:/ /Github/tkinter_app/sberbank.ico')

    screen.resizable(width=False, height=False)
    screen.geometry('410x200')
    screen.title('Take pay')

    # Events
    TSumm = Label(text='Сумма перевода:', font='Consolas')
    summ = Entry(screen, font='Consolas')

    TNumber = Label(text='Number:', font='Consolas')
    Number = Entry(screen, font='Consolas')

    TDate = Label(text='Date:', font='Consolas')
    Date = Entry(screen, font='Consolas')
    Date.insert(0, dt.today().strftime('%d.%m.%y'))

    TDistr = Label(text='Distr:', font='Consolas')
    Distr = Entry(screen, font='Consolas')

    TFullName = Label(text='Full Name:', font='Consolas')
    FullName = Entry(screen, font='Consolas')

    TNumDoc = Label(text='numDoc:', font='Consolas')
    NumDoc = Entry(screen, font='Consolas')

    # Bind command on button
    enter = Button(text='Pay', font='Consolas', width=18, command=take_pay)

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
