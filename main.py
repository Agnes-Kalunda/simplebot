from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('My Chatbot')

#new chatbot trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.english.greetings',
            ' chatterbot.corpus.english.conversations')

#gerating response from user input

response = bot.get_response('Hi, how can i help you')
print(response)