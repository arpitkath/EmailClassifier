from tkinter import Tk, Text, Button, END, messagebox
from tkinter import *
import pickle

f = open('nb_classifier.pickle', 'rb')
cl = pickle.load(f)


def show_info():
    s = ""
    score = [0.9885, 0.9981203007518797, 0.9781578947368421, 0.9880382775119618]
    info = ["Accuracy: ", "Precision: ", "Recall: ", "F1 score: "]
    for i in range(4):
        s += "{0}{1:.2f}%".format(info[i], score[i]*100)+"\n"
    messagebox.showinfo('Score', s)


def test_classifier():
    dict = {}
    for line in text.get(1.0, END).splitlines():
        for word in line.lower().split():
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    messagebox.showinfo('Result', cl.classify(dict))
title = "Email Filter"
root = Tk()
root.title(title)
text = Text(root, bg='light blue')
text.pack()

classify_button = Button(root, text="CLASSIFY", command=test_classifier, bg='sky blue')
classify_button.pack(side=LEFT)

info_button = Button(root, text="INFO", command=show_info, bg='sky blue')
info_button.pack(side=RIGHT)
root.mainloop()