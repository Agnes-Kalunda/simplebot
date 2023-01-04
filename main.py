from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('My Chatbot')

#new chatbot trainer for the chatbot
 trainer = ChatterBotCorpusTrainer(bot)