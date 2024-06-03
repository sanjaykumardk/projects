import tkinter as tk
import sys

class CaesarCipher(tk.Frame):
  def __init__(self, root):
    self.colour1 = '#072b63'
    self.colour2 = '#bfe2ff'
    self.colour3 = '#89b9e1'

    self.letters = 'abcdefghijklmnopqrstuvwxyz'
    self.num_letters = len(self.letters)

    super().__init__(
      root,
      bg=self.colour1
    )

    self.main_frame = self
    self.main_frame.pack(fill=tk.BOTH, expand=TRUE)
    self.main_frame.columnconfigure(0, weight=1)

operating_system = sys.platform
root = tk.Tk()
caesar_cipher_app = CaesarCipher(root)
root.title = 'Caesar Cipher'

if 'win' in operating_system:
  root.geometry('800x450')
elif 'linux' in operating_system:
  root.geometry('800x470')
elif 'darwin' in operating_system:
  root.geometry('800x470')

root.resizable(width=False, height=False)
root.mainloop()
