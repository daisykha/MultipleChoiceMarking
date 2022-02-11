import tkinter as tk
from tkinter import simpledialog, messagebox


class MarkSchemeDialog:
    def __init__(self, valid_answers: str = "ABCDE") -> None:
        self.valid_answers = valid_answers
        self.cols = len(valid_answers)
        self.root = tk.Tk()
        self.root.withdraw()

        self.num_questions = int(
            simpledialog.askstring(
                title="Number of Questions",
                prompt="Please enter the number of questions on the test",
            )
        )

        self.answers = [tk.IntVar() for _ in range(self.num_questions)]

    def create_screen(self):
        self.root.deiconify()
        for n in range(self.num_questions):
            tk.Label(
                self.root,
                text=f"Question {n+1} answer: ",
                justify=tk.LEFT,
                padx=20,
            ).grid(row=n * 2, column=0, columnspan=self.cols)

            for index, question in enumerate(self.valid_answers):
                tk.Radiobutton(
                    self.root,
                    text=question,
                    padx=20,
                    variable=self.answers[n],
                    value=index,
                ).grid(row=n * 2 + 1, column=index)

        tk.Button(self.root, text="Submit", command=self.get_answers).grid(
            row=self.num_questions * 2 + 1, column=0, columnspan=self.cols
        )

        self.root.mainloop()

    def get_answers(self):
        if messagebox.askyesno("Confirmation", "Are you sure?"):
            messagebox.showinfo("Success", "Successfully saved mark scheme")
            self.root.destroy()

    def get_mark_scheme(self):
        return [x.get() for x in self.answers]
