from Classes.working_with_file import FileWork
from tkinter import *

file = FileWork()

window = Tk()
window.title('ZEN')


def print_text():
    entered_text = text_field_find_words.get()
    result["text"] = file.find_words_containing(entered_text)


def save_zen_to_file():
    file.write_to_file()
    update_file_preview()


def clear_file():
    file.write_to_file('', 'w')
    update_file_preview()


def append_to_file():
    appendix = text_field_append.get()
    file.append_to_file(appendix)
    update_file_preview()


def update_file_preview():
    file_text_label["text"] = f'{file.file_name}:\n{file.read_from_file()}'


def close_window():
    window.destroy()


button_save_zen_to_file = Button(window, text="Save zen to file", command=save_zen_to_file)
button_clear_file = Button(window, text="Clear text from file", command=clear_file)
file_text_label = Label(window, text=f'{file.file_name}:\n{file.read_from_file()}', wraplength=200, justify=LEFT)
label_append = Label(window, text="Enter words to append to file: ")
text_field_append = Entry(window)
button_append = Button(window, text="Append to file", command=append_to_file)
label_find_words = Label(window, text="Enter symbols to find: ")
text_field_find_words = Entry(window)
button_find_words = Button(window, text="Find words", command=print_text)
window.bind("<Return>", lambda event: print_text())
window.bind("<Escape>", lambda event: close_window())
result = Label(window, text="", wraplength=300)


button_save_zen_to_file.grid(row=0, column=0)
button_clear_file.grid(row=1, column=0)
file_text_label.grid(row=2, rowspan=2, column=0, padx=10)
label_append.grid(sticky='n', row=0, column=1)
text_field_append.grid(sticky='n', row=0, column=2)
button_append.grid(sticky='n', row=0, column=3, padx=10)
label_find_words.grid(sticky='n', row=1, column=1)
text_field_find_words.grid(sticky='n', row=1, column=2)
button_find_words.grid(sticky='n', row=1, column=3, padx=10)
result.grid(sticky='n', row=2, column=1, columnspan=3)



window.mainloop()