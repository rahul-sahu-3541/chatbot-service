from flask import Flask, jsonify, request
from flask_restful import Api, Resource

import ChatterBot

app = Flask(__name__)
api = Api(app)


class response(Resource):
    def get(self):
        message = request.args.get('message')
        result = str(ChatterBot.chatbot.get_response(message))
        return jsonify({'chatbotResponse': result})


api.add_resource(response, '/chatbot')

if __name__ == '__main__':
    app.run(debug=True)
