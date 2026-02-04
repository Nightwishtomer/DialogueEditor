# gui.library.save_data_to_file.py

import tkinter as tk
from tkinter import filedialog, messagebox

def library_save_data_to_file(data, filepath):
    print("Сохраняет словарь data в файл в формате [ru:...|en:...|de:...]")

   
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            for topic, phrases in data.items():
                f.write(f"--[{topic}]--\n")
                if not phrases:  # если список пуст
                    f.write("\n")
                    continue

                for phrase in phrases:
                    if isinstance(phrase, dict):
                        parts = [f"[{lang}:{text}]" for lang, text in phrase.items()]
                        f.write("|".join(parts) + "\n")
                    else:
                        # если вдруг старая структура — просто текст
                        f.write(f"[text:{phrase}]\n")
                f.write("\n")
        messagebox.showinfo("Success", f"Data saved to {filepath}")
    except Exception as e:
        print(str(e))
        messagebox.showerror("Error", str(e))


def library_save(data, last_filepath=None):
    """Save - если есть last_filepath, просто сохраняем туда"""
    if last_filepath:
        library_save_data_to_file(data, last_filepath)
    else:
        library_save_as(data)


def library_save_as(data):
    """Save As - выбираем путь через диалог"""
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Save As"
    )
    if filepath:
        library_save_data_to_file(data, filepath)

