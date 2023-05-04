import telebot
import  config
from telebot import types
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="movies",
    user="postgres",
    password="",
)

cur = conn.cursor()

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])

def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("horror")
    item2 = types.KeyboardButton("fantasy")
    item3 = types.KeyboardButton("rom-com")
    item4 = types.KeyboardButton("detective")
    item5 = types.KeyboardButton("picked")
    item6 = types.KeyboardButton("naah,bye")
    item7 = types.KeyboardButton("rating")

    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.reply_to(message, "hi, welcome to Dina's bot. please choose the genre", reply_markup=markup)


horror_text = """
1) The Conjuring 1/2/3 

2) Annabelle: Creation

3) The Nun

4) As Above, So Below

5) Final Destination 1/2/3
"""

fantasy_text = """
1) Avatar 

2) Marvel

3) X-Men

4) Harry Potter

5) Spy Kids
"""

rom_com_text = """
1) Mean Girls

2) Easy A

3) John Tucker Must Die

4) Pitch Perfect

5) Just My Luck

6) Bride Wars
"""

detective_text = """
1) Seven 

2) Zodiac

3) The Lovely Bones

4) Murder on the Orient Express

5) Knives Out
"""


@bot.message_handler(func=lambda message: True)
def work(message):
    if message.chat.type == 'private':
        if message.text == 'horror':
            bot.send_message(message.chat.id, horror_text)
        elif message.text == 'fantasy':
            bot.send_message(message.chat.id, fantasy_text)
        elif message.text == 'rom-com':
            bot.send_message(message.chat.id, rom_com_text)
        elif message.text == 'detective':
            bot.send_message(message.chat.id, detective_text)
        elif message.text == 'naah,bye':
            bot.send_message(message.chat.id, 'okey, maybe next time')
        elif message.text == 'picked':
            bot.send_message(message.chat.id, 'enjoy watching')
        elif message.text == 'thank you':
            bot.send_message(message.chat.id, 'u r welcome')
        elif message.text == 'rating':
            bot.send_message(message.chat.id, "Which movie's rating do you want? ")
            bot.register_next_step_handler(message, get_rating)


def get_rating(message):
    movie_name = message.text
    select = "SELECT rate FROM rating WHERE title = %s"
    cur.execute(select, (movie_name,))
    rating = cur.fetchone()

    if rating is not None:
        bot.send_message(message.chat.id, f"The rating for {movie_name} is {rating[0]}.")
    else:
        bot.send_message(message.chat.id, f"Sorry, could not find a rating for {movie_name}.")


bot.polling(none_stop = True)