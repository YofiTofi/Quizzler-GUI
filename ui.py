from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg= THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score.grid(sticky="e", row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="This is some sample text!", font=("Arial", 20, "italic"), fill="black", justify=CENTER,
            width=300
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, bg=THEME_COLOR, highlightthickness=0, command=self.right)
        self.right_button.grid(row=2, column=0)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, bg=THEME_COLOR, highlightthickness=0, command=self.wrong)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text=f"Game Over\nYour score is {self.quiz.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right(self):
        if self.quiz.check_answer("True"):
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
            self.window.after(500, func=self.go_white)
        else:
            self.canvas.config(bg="red")
            self.window.after(500, func=self.go_white)
        self.get_next_question()

    def wrong(self):
        if self.quiz.check_answer("False"):
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
            self.window.after(500, func=self.go_white)
        else:
            self.canvas.config(bg="red")
            self.window.after(500, func=self.go_white)
        self.get_next_question()

    def go_white(self):
        self.canvas.config(bg="white")