from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF


def generate_generic():
    generate_name = name.get()
    generate_position = position.get()
    generate_found_through = found_through.get()

    template = 'Dear ' + generate_name + ' Hiring Team,\n\nI am writing to you out of interest for the position of ' + generate_position \
               + ' that I ' \
               'found through ' + generate_found_through + '. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
               'Vivamus placerat eleifend nunc, in rhoncus leo condimentum vitae. Aenean malesuada justo et suscipit ' \
               'gravida. Maecenas id orci pellentesque, finibus elit id, sollicitudin mauris. Aenean faucibus enim purus,' \
               ' a eleifend nisl commodo a. Vivamus finibus neque sed semper placerat. Fusce accumsan urna et tellus facilisis, ' \
               'nec commodo ex congue. Proin ullamcorper tellus sollicitudin, finibus eros id, lobortis est. Morbi ' \
               'egestas nulla eu nulla viverra tristique.\n\nSincerely,\n'
    messagebox.showinfo('info', template)
    generate_pdf(template)


def generate_personal():
    generate_text = text_input.get('1.0', END)
    generate_pdf(generate_text)


def use_template():
    template = 'Dear <name> Hiring Team,\n\nI am writing to you out of interest for the position of <position> that I ' \
               'found through <found-through>. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
               'Vivamus placerat eleifend nunc, in rhoncus leo condimentum vitae. Aenean malesuada justo et suscipit ' \
               'gravida. Maecenas id orci pellentesque, finibus elit id, sollicitudin mauris. Aenean faucibus enim purus,' \
               ' a eleifend nisl commodo a. Vivamus finibus neque sed semper placerat. Fusce accumsan urna et tellus facilisis, ' \
               'nec commodo ex congue. Proin ullamcorper tellus sollicitudin, finibus eros id, lobortis est. Morbi ' \
               'egestas nulla eu nulla viverra tristique.\n Thank you for your time and consideration.\n\nSincerely,\n'
    text_input.delete(1.0, END)
    text_input.insert(END, template)


def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=13)
    pdf.multi_cell(180, 5, txt=text)
    pdf.output("Cover_Letter.pdf")


window = Tk()
window.title("Cover Letter Generator")
window.geometry('500x400')
tab = ttk.Notebook(window)

tab1 = ttk.Frame(tab)
tab2 = ttk.Frame(tab)

tab.add(tab1, text='Generic')
tab.add(tab2, text='Personal')

# generic tab
name = StringVar()
position = StringVar()
found_through = StringVar()

name_label = Label(tab1, text='Company Name:')
name_label.grid(column=0, row=0, padx=15, pady=15)
name_input = Entry(tab1, width=50, textvariable=name)
name_input.grid(column=1, row=0, padx=15, pady=15)

position_label = Label(tab1, text='Position:')
position_label.grid(column=0, row=1, padx=15, pady=15)
position_input = Entry(tab1, width=50, textvariable=position)
position_input.grid(column=1, row=1, padx=15, pady=15)

found_through_label = Label(tab1, text='Found Through:')
found_through_label.grid(column=0, row=2, padx=15, pady=15)
found_through_input = Entry(tab1, width=50, textvariable=found_through)
found_through_input.grid(column=1, row=2, padx=15, pady=15)

tab_one_submit = Button(tab1, text="Generate", command=generate_generic)
tab_one_submit.grid(column=0, row=3, padx=15, pady=15)
tab.pack(expand=1, fill='both')

# personal tab
text_label = Label(tab2, text='Text:')
text_label.grid(column=0, row=0, padx=15, pady=15)

text_input = Text(tab2, width=55, height=10)
text_input.grid(column=0, row=1, padx=15, pady=15)

use_template = Button(tab2, text="Use Template", command=use_template)
use_template.grid(column=0, row=2, padx=15, pady=15)

tab_two_submit = Button(tab2, text="Generate", command=generate_personal)
tab_two_submit.grid(column=0, row=3, padx=15, pady=15)
tab.pack(expand=1, fill='both')

window.mainloop()
