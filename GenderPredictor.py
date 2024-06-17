from tkinter import *
import requests

root = Tk()
root.title("Gender Predictor")
root.geometry("300x400")

def predict_gender():
    value = entry.get()
    api_key = f"https://gender-api.com/get?name={value}&country=IT&key=5dad8787e7bcc5a0b6b45edf6149b9a059815167832b80551a7aa625ca0f3c71"
    api_req = requests.get(api_key)
    api_dic = api_req.json()
    text1.config(text=f"The name is {value}")
    if 'gender' in api_dic and 'accuracy' in api_dic:
        text2.config(text=f"The gender is {api_dic['gender']}")
        text3.config(text=f"I'm {api_dic['accuracy']}% accurate")
    else:
        text2.config(text="Gender information not found")
        text3.config(text="")

text_label = Label(root, text="- GENDER PREDICTOR -\nGive me your name and I will \npredict it!", bg="grey", fg="black", font=('Comic Sans', 16, 'bold'))
text_label.pack()


frame = Frame(root)
frame.pack(pady=10)

name = Label(frame, text="Name:", font=("Arial", 12, 'bold'), compound=LEFT)
name.pack()

entry = Entry(frame, width=25, font=("Comic Sans MS", 15,'bold'),justify=CENTER)
entry.pack()

text1 = Label(root, font=('Comic Sans MS', 14))
text1.pack()
text2 = Label(root, font=('Comic Sans MS', 14))
text2.pack()
text3 = Label(root, font=('Comic Sans MS', 14))
text3.pack()

button = Button(root, text="Predict!", font=('Arial', 14, 'bold'), bg="orange", bd=5, command=predict_gender)
button.pack(padx=10, pady=15)

root.mainloop()