import os

"""import pandas as pd
import numpy as np
import transformers
import tensorflow as tf
import torch

from transformers import BertTokenizer, BertModel, BertConfig, AutoTokenizer, DataCollatorWithPadding, AutoModelForSequenceClassification, Trainer, TrainerCallback, TrainingArguments, pipeline
"""
from tkinter import *
import speech_recognition as sr
from tkinter import messagebox

# -------------------Models---------------------------------------
# Because we choose not to push our model to the Hub, we will load the locally-saved best model here.
from transformers import pipeline


model_name = input("Please, enter the name of the classification model you wish to use: ")

classifier = pipeline(
    "text-classification",

        model = os.path.join(model_name),
        tokenizer = os.path.join(model_name))

# -------------------Tkinter---------------------------------------
def record_and_convert_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            preds = classifier(text, top_k=None)
            predictions = str(preds)
            text_widget.insert(END, text + "\n")
            text_widget.insert(END, '\nThis sentence is : ', )
            text_widget.insert(END, predictions + "\n\n")
            # ,' are:', preds,"\n")


        except sr.UnknownValueError:
            text_widget.insert(END, "unclear\n")
        except sr.RequestError as e:
            text_widget.insert(END, "unclear\n".format(e))


def reset_application():
    text_widget.delete("0.0", END)


def exit_application():
    result = messagebox.askquestion("Exiting", "Confirm to Exit")
    if result == 'yes':
        messagebox.showinfo("Bye!", "Goodbye!")
        window.destroy()
        exit()


window = Tk()
window.title("CELF-Classification")
# -------------------lblTitle---------------------------------------
lblTitle = Label(window, font=('arial', 100, 'bold'),
                 text="CELF - Classification",
                 bg='royalblue4',
                 fg='light slate gray',
                 width=20)
lblTitle.pack()
# ------------------text_widget-------------------------------------

text_widget = Text(window, width=66,
                   font=('arial', 30, 'bold'),
                   bg='gray69',
                   height=12)
text_widget.pack()
# ------------------Record_button-----------------------------------
record_button = Button(window, width=20,
                       font=('arial', 30, 'bold'),
                       text="Record",
                       command=record_and_convert_text)
record_button.pack(side=LEFT, padx=2)
# ------------------Reset_button------------------------------------
reset_button = Button(window, width=20,
                      font=('arial', 30, 'bold'),
                      text="Reset",
                      command=reset_application)
reset_button.pack(side=LEFT, padx=2)
# ------------------Exit_button-------------------------------------

exit_button = Button(window, width=20,
                     font=('arial', 30, 'bold'),
                     text="Exit",
                     command=exit_application)
exit_button.pack(side=LEFT, padx=2)
# ------------------Print_Text--------------------------------------

window.protocol('WM_DELETE_WINDOW', exit_application)
window.mainloop()