class Message:
    def __init__(self, content, is_user):
        self.content = content
        self.is_user = is_user

    def to_dict(self):
        return {"content": self.content, "is_user": self.is_user}

class ChatBot:
    def __init__(self):
        self.chatbot = ChatterBot("ChatBot")
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        self.chatbot.train("chatterbot.corpus.chinese")

    def get_response(self, text):
        response = self.chatbot.get_response(text)
        return response.text
