ascii_art = """
███████╗███████╗██████╗  ██████╗ ██████╗ ██╗███╗   ██╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗██║████╗  ██║
  ███╔╝ █████╗  ██████╔╝██║   ██║██████╔╝██║██╔██╗ ██║
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║██║╚██╗██║
███████╗███████╗██║  ██║╚██████╔╝██████╔╝██║██║ ╚████║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
"""

print(ascii_art)

import webbrowser
import os

def open_website(url):
    webbrowser.open(url)

def print_colored_link(link_text, url, color_code):
    print(f"\033[91m{link_text}\033[0m")  # ANSI escape code for red color
    open_website(url)

if __name__ == "__main__":
    link_text = "Click here to visit the website"
    website_url = "https://github.com/ZeroBinOfficial"
    color_code = 91  # ANSI color code for red

    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen

    print_colored_link(link_text, website_url, color_code)

ascii_art = """
███████╗███████╗██████╗  ██████╗ ██████╗ ██╗███╗   ██╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗██║████╗  ██║
  ███╔╝ █████╗  ██████╔╝██║   ██║██████╔╝██║██╔██╗ ██║
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║██║╚██╗██║
███████╗███████╗██║  ██║╚██████╔╝██████╔╝██║██║ ╚████║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
"""

print(ascii_art)
import tkinter as tk
import threading
import socket
from tkinter import messagebox

def start_server(ip, port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip, port))
        server_socket.listen(1)

        print("Așteptând conexiuni...")
        client_socket, client_address = server_socket.accept()
        print(f"Conexiune acceptată de la {client_address}")

        # Poți adăuga cod suplimentar aici pentru a comunica cu clientul

    except Exception as e:
        print(f"Erroare: {e}")
    finally:
        server_socket.close()

def on_start_button_click(ip_entry, port_entry):
    ip = ip_entry.get()
    port = int(port_entry.get())

    if not ip or not port:
        messagebox.showwarning("Avertisment", "Te rugăm să introduci o adresă IP și un port.")
    else:
        start_button["state"] = "disabled"
        threading.Thread(target=start_server, args=(ip, port), daemon=True).start()

# Crearea ferestrei principale
root = tk.Tk()
root.title("Server Conection")

# Crearea etichetelor și câmpurilor de intrare
ip_label = tk.Label(root, text="IP Adress:")
ip_label.grid(row=0, column=0, padx=10, pady=10)

ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=10, pady=10)

port_label = tk.Label(root, text="Port:")
port_label.grid(row=1, column=0, padx=10, pady=10)

port_entry = tk.Entry(root)
port_entry.grid(row=1, column=1, padx=10, pady=10)

# Crearea butonului de start
start_button = tk.Button(root, text="Start Attack", command=lambda: on_start_button_click(ip_entry, port_entry))
start_button.grid(row=2, column=0, columnspan=2, pady=20)

# Pornirea buclei principale a interfeței grafice
root.mainloop()


