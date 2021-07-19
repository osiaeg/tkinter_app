from tkinter import *


def rander(elements) -> None:
    for el in elements:
        el.pack()

    result.pack(side='right')
    label_res.pack(side='left')


def show_res(res) -> None:
    result['text'] = res


def plus() -> None:
    a, b = first_num.get(), second_num.get()
    res = str(int(a) + int(b))
    show_res(res)


def div() -> None:
    a, b = first_num.get(), second_num.get()
    res = str(int(a) / int(b))
    show_res(res)


def mul() -> None:
    a, b = first_num.get(), second_num.get()
    res = str(int(a) * int(b))
    show_res(res)


def minus() -> None:
    a, b = first_num.get(), second_num.get()
    res = str(int(a) - int(b))
    show_res(res)


if __name__ == "__main__":
    root = Tk()
    root.iconbitmap('sberbank.ico')
    root.title('Calculator')

    first_num = Entry(root, width=50)
    second_num = Entry(root, width=50)

    btn_plus = Button(root, text='+', width=40, command=plus)
    btn_minus = Button(root, text='-', width=40, command=minus)
    btn_mul = Button(root, text='*', width=40, command=mul)
    btn_div = Button(root, text='/', width=40, command=div)

    result = Label(root, width=25, text='')
    label_res = Label(root, text='Result: ')

    screen_elem = [first_num,
                   second_num,
                   btn_plus,
                   btn_minus,
                   btn_mul,
                   btn_div]

    rander(screen_elem)
    root.mainloop()
