import random
import time

class MockInterviewAssistant:
    def __init__(self):
        self.questions = [
            "Tell me about yourself.",
            "What are your strengths?",
            "What are your weaknesses?",
            "Why do you want to work for this company?",
            "Why should we hire you?",
            "Describe a challenging situation you faced and how you handled it.",
            "Where do you see yourself in 5 years?",
            "How do you handle stress and pressure?",
            "Describe a time when you worked in a team.",
            "Tell me about a time you failed and what you learned from it."
        ]
        self.feedback = {
            "Tell me about yourself.": "Start with a quick summary of your background and highlight key achievements.",
            "What are your strengths?": "Focus on strengths that align with the job description.",
            "What are your weaknesses?": "Pick a weakness that you're working on improving and show how you're addressing it.",
            "Why do you want to work for this company?": "Research the company's culture, values, and products to align with your interests.",
            "Why should we hire you?": "Summarize your key skills, experience, and how you can contribute to the team.",
            "Describe a challenging situation you faced and how you handled it.": "Use the STAR method (Situation, Task, Action, Result).",
            "Where do you see yourself in 5 years?": "Be honest but also align your answer with career growth within the company.",
            "How do you handle stress and pressure?": "Give an example of a stressful situation and how you managed it effectively.",
            "Describe a time when you worked in a team.": "Highlight a situation where you collaborated effectively to achieve a goal.",
            "Tell me about a time you failed and what you learned from it.": "Focus on a real failure and show how you grew from it."
        }

    def start_interview(self):
        print("Welcome to the Mock Interview Assistant!")
        time.sleep(1)
        print("\nLet's begin your practice interview.\n")
        time.sleep(1)

        # Asking random questions
        for question in random.sample(self.questions, len(self.questions)):
            self.ask_question(question)

    def ask_question(self, question):
        print(f"\nQuestion: {question}")
        print("Please provide your answer: ")

        # Taking the user's answer
        answer = input("\nYour answer: ")
        
        # Provide feedback on the answer
        time.sleep(1)
        print(f"\nFeedback: {self.feedback.get(question, 'No specific feedback for this question.')}")

        # Pause before next question
        time.sleep(2)
        
    def conclude(self):
        print("\nGreat job! You've completed the mock interview. Keep practicing!")
        time.sleep(1)
        print("\nRemember, the key to acing an interview is preparation. Best of luck!")

# Initialize and start the mock interview
if __name__ == "__main__":
    interview = MockInterviewAssistant()
    interview.start_interview()
    interview.conclude()
