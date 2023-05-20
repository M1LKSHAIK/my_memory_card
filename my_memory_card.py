from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Опрос на сколько ты знаешь shadowraze')
window.resize(800, 400)
btn_OK = QPushButton('Ответить)))')
lb_Queshen = QLabel('В каком году была основан Astral Step')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('1945')
rbtn_2 = QRadioButton('1254')
rbtn_3 = QRadioButton('2021')
rbtn_4 = QRadioButton('2022')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Твой результат)))')
lb_Result = QLabel('Ща чекним)))')
lb_Correct = QLabel('Ответ тута)))')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Queshen, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=3)
layout_card.addStretch(1)
layout_card.addSpacing(5)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопросик)))')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить)))')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

from random import shuffle

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Queshen.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Умничка)))')
        window.score += 1
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Попуск')
    print('Статистика')
    print('Всего вопросов:', window.total)
    print('Правельных ответов:', window.score)
    print('Рейтинг:', window.score/window.total*100,'%')

def next_question():
    window.total += 1
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить)))':
        check_answer()
    else:
        next_question()

window.cur_question = -1 
window.total = 0
window.score = 0
question_list = []
question_list.append(Question('В каком году была основан Astral Step', '2021', '1945', '2022', '1367'))
question_list.append(Question('Когда был основан Showdown', '2022', '1835', '2021', '4837'))
question_list.append(Question('Когда выйдет 4060 ti', 'Я че знаю что-ли', '2021', '2022', '2023'))
question_list.append(Question('Сколько стоит 4090', '151105р', '150к', '130к', '120к'))
question_list.append(Question('крым - это', 'Россия', 'Россия', 'Россия', 'Россия'))
question_list.append(Question('где снимался Артур Пирожкой', 'бабушка лёгкого поведения', 'хз', 'хз', 'хз'))
question_list.append(Question('кто такой ivanzolo2004', 'ноунейм', 'топ исполнитель', 'тиктокер', 'хз'))
question_list.append(Question('какой мой любимый fresh bar', 'citrus ice', 'хз', 'персик', 'виноград'))
question_list.append(Question('кто такой shadowraze', 'топ исполнитель', 'хз', 'хз', 'хз'))
question_list.append(Question('самая последняя портативня консоль', 'steam desk', 'nintendo', 'psp', 'msi'))
next_question()
btn_OK.clicked.connect(click_OK)
window.setLayout(layout_card)
window.show()
app.exec_()