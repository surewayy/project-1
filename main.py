from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("sure.kv")
class LoginPage(Screen):
    def show_call_instructor_popup(self):
        popup = Popup(
            title='       Call the Admin for assistance        ',
            content=Label(text="08062942039"),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()
class HomePage(Screen):
    def start_quiz(self):
        self.manager.current = "quiz"

    def reset_inputs(self):
        pass

    def logout(self):
        login_page = self.manager.get_screen("login")
        password_input = login_page.ids.passw

        # Reset the text in the password TextInput widget
        password_input.text = ""

        self.manager.current = "login"

    def start_quiz2(self):
        quiz_screen2 = self.manager.get_screen("quiz2")
        quiz_screen2.current_question = 0
        quiz_screen2.score = 0
        quiz_screen2.load_question()
        quiz_screen2.clear_buttons()
        self.manager.current = "quiz2"
class ResultScreen(Screen):
    pass

class ResultScreen2(Screen):
    pass
class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginPage())
        sm.add_widget(HomePage())
        sm.add_widget(ResultScreen())
        sm.add_widget(QuizScreen(name="quiz"))
        sm.add_widget(QuizScreen2(name="quiz2"))

        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"

        sm.current = "login"

        return sm

    def reset_quiz_and_go_home(self):
        screen_manager = self.root
        quiz_screen = screen_manager.get_screen("quiz")
        home_screen = screen_manager.get_screen("home")

        quiz_screen.reset_quiz_state()
        screen_manager.transition.direction = "right"
        home_screen.manager.current = "home"

    def set_username(self, username):
        self.username = username
class QuizScreen(Screen):
    current_question = 0
    score = 0

    questions = [
        {
            "question": "______ is an example of woodwind instrument?",
            "options": ["Piano", "Clarinet", "Trumpet", "Drum"],
            "correct_answer": 1
        },
        {
            "question": "Treble clef is also known as.... ?",
            "options": ["G Clef", "C Clef", "F Clef", "B Clef"],
            "correct_answer": 0
        },
        {
            "question": "The two types of Piano are Upright Piano and ____",
            "options": ["Down right", "Grand Piano", "Ground Piano", "standing Piano"],
            "correct_answer": 1
        },
        {
            "question": "Who Invented the Piano?",
            "options": ["Bartolomeo Cristofori", "Thomas Henry", " Thomas James", "Isaac Newton"],
            "correct_answer": 0
        },
        {
            "question": "A Stave has ______ lines",
            "options": ["four", "five", "six", "two"],
            "correct_answer": 1
        }
    ]

    def on_pre_enter(self):
        self.load_question()
    def load_question(self):
        question = self.questions[self.current_question]
        self.ids.question_label.text = question["question"]
        for i, option in enumerate(question["options"]):
            self.ids[f'option_{i + 1}'].text = option

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]

        if selected_option == correct_answer:
            self.ids[f'option_{selected_option + 1}'].background_color = (0, 1, 0, 1)  # Green for correct
            self.score += 1
        else:
            self.ids[f'option_{selected_option + 1}'].background_color = (1, 0, 0, 1)  # Red for incorrect

        # Disable buttons after an option is selected
        for i in range(4):
            self.ids[f'option_{i + 1}'].disabled = False

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()
    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False
    def show_result(self):
        result_label = self.manager.get_screen("result_screen").ids.result_label
        result_label.text = f"Result: {self.score}/5"
        self.manager.current = "result_screen"
    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0
        self.load_question()
        self.clear_buttons()

class QuizScreen2(Screen):
    current_question = 0
    score = 0

    questions = [
        {
            "question": "Question 1: What is 2 + 2?",
            "options": ["4", "3", "5", "6"],
            "correct_answer": 0
        },
        {
            "question": "Question 2: What is the capital of Italy?",
            "options": ["Paris", "Rome", "Madrid", "Berlin"],
            "correct_answer": 1
        },
        {
            "question": "Question 3: Who wrote 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
            "correct_answer": 0
        },
        {
            "question": "Question 4: What is the chemical symbol for oxygen?",
            "options": ["Ox", "O", "Oxg", "Oy"],
            "correct_answer": 1
        },
        {
            "question": "Question 5: What is the largest mammal on Earth?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
            "correct_answer": 1
        }
    ]

    def on_pre_enter(self):
        self.load_question()

    def load_question(self):
        question = self.questions[self.current_question]
        self.ids.question_label.text = question["question"]
        for i, option in enumerate(question["options"]):
            self.ids[f'option_{i + 1}'].text = option

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]

        if selected_option == correct_answer:
            self.ids[f'option_{selected_option + 1}'].background_color = (0, 1, 0, 1)  # Green for correct
            self.score += 1
        else:
            self.ids[f'option_{selected_option + 1}'].background_color = (1, 0, 0, 1)  # Red for incorrect

        # Disable buttons after an option is selected
        for i in range(4):
            self.ids[f'option_{i + 1}'].disabled = False

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()
    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False
    def show_result(self):
        result_label = self.manager.get_screen("result_screen").ids.result_label
        result_label.text = f"Result: {self.score}/5"
        self.manager.current = "result_screen"
    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0
        self.load_question()
        self.clear_buttons()
    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = "home"

if __name__ == '__main__':
    MainApp().run()





