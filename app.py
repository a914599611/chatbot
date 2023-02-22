from flask import Flask, jsonify, request, render_template
from chatbot.bot import ChatBot
from chatbot.message import Message

app = Flask(__name__)
bot = ChatBot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    message = Message(content=content, is_user=True)
    bot_response = bot.get_response(content)
    response = Message(content=str(bot_response), is_user=False)
    return jsonify({"messages": [message.to_dict(), response.to_dict()]})
