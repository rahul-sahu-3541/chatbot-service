from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Slate')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.custom.myown")

# while True:
#     request = input('You: ')
#     response = chatbot.get_response(request)
#     print('Bot: '+ str(response))
