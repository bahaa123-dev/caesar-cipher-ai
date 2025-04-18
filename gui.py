import tkinter as tk
from caesar_ai import ai_caesar_crack

def main():
    root = tk.Tk()
    root.title("AI Caesar Cipher Cracker")
    root.geometry("650x300")

    # Input label and entry
    tk.Label(root, text="Enter Caesar-encrypted text:", font=(None, 12)).pack(pady=(20, 5))
    input_entry = tk.Entry(root, width=70, font=(None, 12))
    input_entry.pack(pady=(0, 10))

    # Result display
    result_label = tk.Label(root, text="", font=(None, 12), justify="left", wraplength=600)
    result_label.pack(pady=(10, 20))

    def on_decrypt():
        ciphertext = input_entry.get().strip()
        if not ciphertext:
            result_label.config(text="Please enter some encrypted text.")
            return
        result_label.config(text="Decrypting... (this may take a few seconds)")

        # Run AI brute-force crack
        plaintext, shift, score = ai_caesar_crack(ciphertext)

        result_text = (
            f"Best Decryption:\n"
            f"{plaintext}\n\n"
            f"Detected Shift: {shift}\n"
            f"Score: {score:.2f}"
        )
        result_label.config(text=result_text)

    # Decrypt button
    decrypt_button = tk.Button(root, text="Decrypt", font=(None, 12), command=on_decrypt)
    decrypt_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()