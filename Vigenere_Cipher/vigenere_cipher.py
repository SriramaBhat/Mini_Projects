import tkinter
from tkinter import messagebox


class Vigenere:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Vigenere Cipher")
        self.window.configure(background="light blue")
        self.window.resizable(width=False, height=False)
        self.window.geometry("500x400")
        self.title = tkinter.Label()
        self.title.configure(text="Vigenere Cipher Encoder", background="light blue", font=("arial", 20))
        self.title.place(x=105, y=20)
        self.input_label = tkinter.Label()
        self.input_label.configure(text="Message : ", background="light blue", font=("arial bold", 13))
        self.input_label.place(x=17, y=75)
        self.input_text = tkinter.Entry()
        self.input_text.configure(font=("arial", 13), width=50)
        self.input_text.place(x=25, y=115)
        self.key_label = tkinter.Label()
        self.key_label.configure(text="Key : ", background="light blue", font=("arial bold", 13))
        self.key_label.place(x=20, y=165)
        self.key_input = tkinter.Entry()
        self.key_input.configure(font=("arial", 13), width=40)
        self.key_input.place(x=105, y=165)
        self.enc_label = tkinter.Label()
        self.enc_label.configure(text="Encrypted Text : ", background="light blue", font=("arial bold", 13))
        self.enc_label.place(x=10, y=225)
        self.enc_disp = tkinter.Entry()
        self.enc_disp.configure(font=("arial", 13), width=50, state="readonly")
        self.enc_disp.place(x=25, y=260)
        self.enc_btn = tkinter.Button()
        self.enc_btn.configure(text="Encrypt", background="black", foreground="white", font=("arial", 15), width=20)
        self.enc_btn.place(x=125, y=325)
        self.enc_btn.configure(command=self.encrypt)

    # Method for the input submission and result display
    def encrypt(self):
        text = self.input_text.get().strip()
        key = self.key_input.get().strip()
        if text == "" or key == "":
            messagebox.showerror("Error", "Enter the message and key!!")
        else:
            enc_msg = self.encryption()
            self.enc_disp.configure(state="normal")
            self.enc_disp.delete(0, tkinter.END)
            self.enc_disp.insert(0, enc_msg)
            self.enc_disp.configure(state="readonly")

    # Method for key generation
    def generate_key(self):
        text = self.input_text.get().strip()
        key = self.key_input.get().strip()
        if len(key) == len(text):
            return key
        elif len(key) > len(text):
            return key[:len(text)+1]
        else:
            key = list(key)
            for i in range(len(text) - len(key)):
                key.append(key[i % len(key)])

            return "".join(key)

    # Method for the generation of cipher text
    def encryption(self):
        text = self.input_text.get().strip().upper()
        key = self.generate_key().upper()
        cipher_text = []
        for i in range(len(text)):
            x = (ord(text[i]) + ord(key[i])) % 26
            x += ord("A")
            cipher_text.append(chr(x))

        cipher_text = "".join(cipher_text)
        return cipher_text.casefold()


if __name__ == "__main__":
    vig = Vigenere()
    vig.window.mainloop()
