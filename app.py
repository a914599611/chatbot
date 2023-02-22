from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# 从环境变量中获取 OpenAI API 密钥
openai.api_key = os.environ['OPENAI_API_KEY']


@app.route('/')
def index():
    # 根路由返回欢迎消息
    return '欢迎来到 ChatBot！'


@app.route('/chat', methods=['POST'])
def chat():
    # 从请求数据中获取聊天消息
    message = request.json['message']

    # 调用 OpenAI API 生成响应
    response = openai.Completion.create(
        engine='davinci',
        prompt=f'Q: {message}\nA:',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 从 API 响应中提取响应文本
    response_text = response.choices[0].text.strip()

    # 将响应作为 JSON 返回
    return jsonify({'response': response_text})
