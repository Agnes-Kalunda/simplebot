from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from textblob import TextBlob
bot = ChatBot('My Chatbot')

#new chatbot trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.english.greetings',
            ' chatterbot.corpus.english.conversations')



#function to calculate sentiments of a message
def calc_sentiment(message):
    #using TextBlob for sentiment calculation
    sentiment = TextBlob(message).sentiment.polarity

    if sentiment > 0 :
        return 'positive'

    elif sentiment < 0:
        return 'negative'

    else: 
        return 'neutral'

# training the bot via deep learning
# memeory_trainer =  ChatterBotMemoryTrainer(bot)
# memory_trainer.train()


#gerating response from user input

response = bot.get_response('Hi, how can i help you')
print(response)