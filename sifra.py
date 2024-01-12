import sys, os, base64
from tkinter import Tk, filedialog, messagebox
def encrypt_file(filename):
  try:
      with open(filename, 'rb') as f:
          content = f.read()
      encrypted_content = base64.b64encode(content)
      return encrypted_content
  except Exception as ex:
      messagebox.showerror("Chyba", f"Nastala chyba při dešifrování souboru: {str(ex)}" + "\nPravděpodobně byl vybrán špatný soubor nebo akce.")
      sys.exit(1)
def decrypt_file(filename, encrypted_content):
  try:
      decrypted_content = base64.b64decode(encrypted_content)
      with open(filename, 'wb') as f:
          f.write(decrypted_content)
          decrypted_string = decrypted_content.decode('utf-8', errors='ignore')
          messagebox.showinfo("OK", "Dešifrovaný obsah byl uložen do souboru.\n" + filename +"\n\nObsah: " + decrypted_string)
  except Exception as ex:
      messagebox.showerror("Chyba", f"Nastala chyba při dešifrování souboru: {str(ex)}" + "\nPravděpodobně byl vybrán špatný soubor nebo akce.")
      sys.exit(1)

def get_file():
  try:
      messagebox.showinfo("Vítejte", "Vyberte textový soubor se kterým chcete pracovat.")
      root = Tk()
      root.withdraw()
      filename = filedialog.askopenfilename(initialdir=os.path.join(os.path.dirname(sys.argv[0]), 'priklady'))
      # Check if the file has a .txt extension
      _, file_extension = os.path.splitext(filename)
      if file_extension != ".txt":
         messagebox.showerror("Chyba", "Buď jste vybrali soubor, který není v textovém formátu (.txt)\nnebo jste nevybrali žádný soubor.")
         sys.exit(1)
      if filename:
          action = messagebox.askyesno('Vyberte operaci.', 'Pro šifrování obsahu souboru stisknete Ano\nPro dešifrování obsahu souboru stiskněte Ne.')
          if action:
              encrypted_content = encrypt_file(filename)
              messagebox.showinfo("Informace", "Nyní vyberte kam chce zašifrovaný textový dokument uložit.")
              save_path = filedialog.asksaveasfilename(defaultextension=".txt")
              if save_path:
                 with open(save_path, 'wb') as f:
                    f.write(encrypted_content)
                    messagebox.showinfo("OK", "Obsah dokumentu byl zašifrován a uložen jako " + save_path + ".")
          else:
              with open(filename, 'rb') as f:
                 encrypted_content = f.read()
              messagebox.showinfo("Informace", "Nyní vyberte kam chce odšifrovaný textový dokument uložit.")
              save_path = filedialog.asksaveasfilename(defaultextension=".txt")
              if save_path:
                 decrypt_file(save_path, encrypted_content)
          restart = messagebox.askyesno('', 'Chcete pracovat ještě s dalším souborem?')
          if restart:
              python = sys.executable
              os.execl(python, python, *sys.argv)
  except Exception as ex:
      messagebox.showerror("Chyba", f"Nastala chyba: {str(ex)}")
      sys.exit(1)
if __name__ == "__main__":
   get_file()
