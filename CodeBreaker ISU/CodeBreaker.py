# CodeBreaker.py

# Imports
import Tkinter as tk
import ttk

# GUI init
root = tk.Tk()
root.resizable(False, False)
root.geometry("600x450+401+179")
root.title("CaesarBreaker")

# Var and styles init
cipherText = ""
cipher_shift_menu = tk.StringVar()
alpha_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
              "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters = "".join(alpha_list)
combostyle = ttk.Style()
combostyle.theme_create("combostyle", parent="alt",
                        settings={"TButton":
                            {"configure":
                                {
                                    "fieldbackground": "#212121",
                                    "background": "#484848",
                                    "foreground": "white"
                                }}})
combostyle.theme_use("combostyle")
spinstyle = ttk.Style()
spinstyle.theme_create("spinstyle", parent="alt",
                        settings={"TCombobox":
                            {"configure":
                                {
                                    "fieldbackground": "#212121",
                                    "background": "#484848",
                                    "foreground": "white"
                                }}})
spinstyle.theme_use("combostyle")
theme_img = tk.PhotoImage(file="Assets/theme.png")

# Widget init (Many configure methods because PEP-8 doesn't like long lines)
Canvas1 = tk.Canvas(root)
Canvas1.place(relx=-0.017, rely=-0.022, relheight=1.033
    , relwidth=1.025)
Canvas1.configure(background="#303030")
Canvas1.configure(borderwidth="2")
Canvas1.configure(highlightbackground="#d9d9d9")
Canvas1.configure(highlightcolor="black")
Canvas1.configure(insertbackground="black")
Canvas1.configure(relief="ridge")
Canvas1.configure(selectbackground="#c4c4c4")
Canvas1.configure(selectforeground="black")
Canvas1.configure(width=615)
Canvas1.create_image(0, 0, image=theme_img, anchor=tk.NW)

Text1 = tk.Text(Canvas1)
Text1.place(relx=0.211, rely=0.258, relheight=0.219, relwidth=0.566) # Text1.place(relx=0.228, rely=0.258, relheight=0.413, relwidth=0.566)
Text1.configure(background="#212121")
Text1.configure(font="-family {.SF NS Text} -size 13")
Text1.configure(foreground="white")
Text1.configure(highlightbackground="#5e5e5e")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="white")
Text1.configure(selectbackground="#c4c4c4")
Text1.configure(selectforeground="black")
Text1.configure(width=348)
Text1.configure(wrap="word")
Text1.insert(tk.INSERT, "Enter cipher text/plain text...")

Text1 = tk.Text(Canvas1)
Text1.place(relx=0.211, rely=0.258, relheight=0.219, relwidth=0.566)
Text1.configure(background="#212121")
Text1.configure(font="-family {.SF NS Text} -size 13")
Text1.configure(foreground="white")
Text1.configure(highlightbackground="#5e5e5e")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="white")
Text1.configure(selectbackground="#c4c4c4")
Text1.configure(selectforeground="black")
Text1.configure(width=348)
Text1.configure(wrap="word")
Text1.insert(tk.INSERT, "Enter cipher text/plain text...")

Text2 = tk.Text(Canvas1)
Text2.place(relx=0.211, rely=0.473, relheight=0.219, relwidth=0.566)
Text2.configure(background="#212121")
Text2.configure(font="-family {.SF NS Text} -size 13")
Text2.configure(foreground="white")
Text2.configure(highlightbackground="#5e5e5e")
Text2.configure(highlightcolor="black")
Text2.configure(insertbackground="white")
Text2.configure(selectbackground="#c4c4c4")
Text2.configure(selectforeground="black")
Text2.configure(width=348)
Text2.configure(wrap="word")
Text2.insert(tk.INSERT, "Encrypted/decrypted text...")

Label1 = tk.Label(Canvas1)
Label1.place(relx=0.244, rely=0.774, height=24, width=41)
Label1.configure(background="#303030")
Label1.configure(foreground="white")
Label1.configure(text="Shift")

Spinbox1 = tk.Spinbox(Canvas1, from_=1.0, to=100.0)
Spinbox1.configure(from_=1, to=25)
Spinbox1.place(relx=0.309, rely=0.774, relheight=0.06
    , relwidth=0.073)
Spinbox1.configure(activebackground="#f9f9f9")
Spinbox1.configure(background="#212121")
Spinbox1.configure(buttonbackground="#d9d9d9")
Spinbox1.configure(font="-family {.SF NS Text} -size 13")
Spinbox1.configure(foreground="white")
Spinbox1.configure(highlightbackground="#5e5e5e")
Spinbox1.configure(highlightcolor="black")
Spinbox1.configure(insertbackground="black")
Spinbox1.configure(selectbackground="#212121")
Spinbox1.configure(selectforeground="white")
Spinbox1.configure(textvariable=cipher_shift_menu)
Spinbox1.configure(width=35)

def encrypt_text():
    """Encryption function"""
    string_to_encrypt = Text1.get("1.0","end-1c")
    string_to_encrypt = str(string_to_encrypt)
    string_to_encrypt = string_to_encrypt.upper()
    cipher_shift = cipher_shift_menu.get()
    cipher_shift = int(cipher_shift)
    string_encrypted = ""
    
    # Shifts the current letter according to curreny position and indicated cipher shift
    for character in string_to_encrypt:
        position = letters.find(character)
        new_position = position + cipher_shift

        if character in letters:
            if new_position >= 26:
                new_position = new_position - 26
                string_encrypted = string_encrypted + letters[new_position]
            else:
                string_encrypted = string_encrypted + letters[new_position]
        else:
            string_encrypted = string_encrypted + character

    Text2.delete("1.0", "end")
    Text2.insert("1.0", string_encrypted)

# Cipher func init
# TODO: Check function since it only works if encryption is done first, and that is wrong
def decrypt_text():
    """Decryption function"""
    string_to_decrypt = Text1.get("1.0","end-1c")
    string_to_decrypt = str(string_to_decrypt)
    string_to_decrypt = string_to_decrypt.upper()
    cipher_shift = cipher_shift_menu.get()
    cipher_shift = int(cipher_shift)
    string_encrypted = ""
    
    # Shifts the current letter according to curreny position and indicated cipher shift
    for character in string_to_decrypt:
        position = letters.find(character)
        new_position = position - (cipher_shift - cipher_shift)

        if character in letters:
            string_encrypted = string_encrypted + letters[new_position]
        else:
            string_encrypted = string_encrypted + character

    Text2.delete("1.0","end-1c")
    Text2.insert("1.0", string_encrypted)

# Function wouldn't work just saying the command is the function name, so a lambda with it would work
TButton1 = ttk.Button(Canvas1)
TButton1.place(relx=0.407, rely=0.774, height=24, width=87)
TButton1.configure(takefocus="")
TButton1.configure(text="Encrypt")
TButton1.configure(width=87)
TButton1.configure(command=lambda: encrypt_text())

TButton2 = ttk.Button(Canvas1)
TButton2.place(relx=0.602, rely=0.774, height=24, width=87)
TButton2.configure(takefocus="")
TButton2.configure(text="Decrypt")
TButton2.configure(command=lambda: decrypt_text())

root.mainloop() # Basically like a forever lasting while loop until the window is closed
