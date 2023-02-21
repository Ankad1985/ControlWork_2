from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QListWidget, 
                            QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout)
 
app = QApplication([])
notes = []
 
#--------------------------------------------------параметры окна приложения
notes_window = QWidget()
notes_window.setWindowTitle('Заметки')
notes_window.resize(500, 250)
 
#--------------------------------------------------виджеты окна приложения
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')
button_note_create = QPushButton('Новая заметка')
button_note_save = QPushButton('Сохранить')
field_text = QTextEdit()
button_data_add = QPushButton('Добавить данные')
 
#----------------------------------------------------расположение виджетов
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes) 
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
row_3 = QHBoxLayout()
row_3.addWidget(button_data_add)
row_4 = QHBoxLayout()
col_2.addLayout(row_3)
col_2.addLayout(row_4)
layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_window.setLayout(layout_notes)

#-----------------------------------------------------описание функций приложения
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
 
def add_note():
    note_name, ok = QInputDialog.getText(notes_window,"Добавить","Название заметки: ")
    if ok and note_name != "":
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        print(notes)
        with open(str(len(notes)-1)+".txt", "w") as file:
            file.write(note[0]+'\n')
 
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                with open(str(index)+".txt", "w") as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            index += 1
        print(notes)
    else:
        print("Заметка для сохранения не выбрана!")
 

list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)
 
notes_window.show()
name = 0
note = []
while True:
    filename = str(name)+".txt"
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.replace('\n', '')
                note.append(line)
        tags = note[2].split(' ')
        note[2] = tags
        
        notes.append(note)
        note = []
        name += 1
 
    except IOError:
        break
 
print(notes)
for note in notes:
    list_notes.addItem(note[0])
 
app.exec_()
