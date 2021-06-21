from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import spacy

#spacy.load("en")


bot = ChatBot('bot')
trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
#bot.get_response("Hello, how are you today?")

while True:
  message = input('You:')
  if message.strip() != 'Bye':
    reply = bot.get_response(message)
    print('ChatBot :', reply)
  if message.strip() == 'Bye':
    print('Chatbot : Bye')
    break


#for files in os.listdir('drive/My Drive/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
  #data = open('drive/My Drive/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
  #trainer.train(data)
  #print(data)
