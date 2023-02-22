from chatterbot import ChatBot as ChatterBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class ChatBot:
    def __init__(self):
        self.chatbot = ChatterBot("ChatBot")
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        self.chatbot.train("chatterbot.corpus.chinese")

    def get_response(self, text):
        response = self.chatbot.get_response(text)
        return response.text
