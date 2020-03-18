import telebot # Import pyTelegramBotAPI
import datetime
import time

tele_bot = telebot.TeleBot('token') # Token bot

dictio_diary = {} # Membuat dictionary diary


@tele_bot.message_handler(commands=['start'])
def start_message(message):
    '''Menyambut user'''
    tele_bot.reply_to(message, "Assalamu'alaikum! Type '/help' to see what to do!")

@tele_bot.message_handler(commands=['help'])
def help_message(message):
    '''Memberi tahu user yang harus diketik sesuai pilihan user'''
    tele_bot.reply_to(message, "Type between happy, sad, scared, or angry "+
                      "based on how you feel today and I'll respond you!"+
                      "\n\nOr if you want to read your diary, type 'Read diary'!")


@tele_bot.message_handler(func=lambda message: message.text is not None and
                          ('no diary' in message.text or 'No diary' in message.text))
def no_diary(message):
    '''Apabila user tidak mau membuat diary'''
    tele_bot.reply_to(message, "Okay then, hope you have a good day!")

@tele_bot.message_handler(func=lambda message: message.text is not None and
                          ('yes diary' in message.text or 'Yes diary' in message.text))
def yes_diary(message):
    '''Instruksi untuk membuat diary'''
    tele_bot.reply_to(message, "Begin your diary with 'Diary' and write down your diary "+
                      "in one bubble chat, please! :)"+
                      "\n\nexample: Diary, today I'm really happy! Because I got free ice creams!")


@tele_bot.message_handler(func=lambda message: message.text is not None and
                          ('read diary' in message.text or 'Read diary' in message.text))
def read_diary(message):
    '''Instruksi untuk memilih membaca diary yang telah dibuat'''
    chat_id = message.chat.id # Mengambil chat ID
    if chat_id not in dictio_diary.keys(): # Apabila user belum pernah membuat diary
        tele_bot.reply_to(message, "You haven't write any diary :(")
    else:
        lst = [] # List berisi tanggal diary yang pernah dibuat
        for i in dictio_diary[chat_id].keys():
            lst.append(i)
        tele_bot.reply_to(message, "Please choose between the date you wrote your diary:\n{}\n\n".format(", ".join(lst))+
                          "Choose one, then type the date just the way it"+
                          " is shown above.\nexample: 12/12/2018")

@tele_bot.message_handler(func=lambda message: message.text is not None and
                          '/20' in message.text)
def diary_date(message):
    '''Memunculkan diary sesuai tanggal yang diminta user'''
    chat_id = message.chat.id # Mengambil chat ID
    lst = list(message.text)
    if len(lst) != 10: # Apabila input user tidak sesuai
        tele_bot.reply_to(message, "Please choose between the date then type the date just the way it"+
                              " was shown above.\nexample: 12/12/2018")
    else:
        tele_bot.reply_to(message, "Your diary that day:\n\n{}".format(dictio_diary[chat_id][message.text]))


@tele_bot.message_handler(func=lambda message: message.text is not None and
                          ('diary' in message.text or 'Diary' in message.text))
def write_diary(message):
    '''Menulis diary'''
    chat_id =  message.chat.id # Mengambil chat ID
    today_date = datetime.date.today().strftime("%d/%m/%Y") # Tanggal diary dibuat
    if chat_id not in dictio_diary.keys():
        dictio_diary[chat_id] = {today_date : message.text}
        tele_bot.reply_to(message, "Saved!\nType 'Read diary' if you want to read your diary!"+
                      "\n\nPsst ... there will be only one diary saved in a day.")
    else:
        dictio_diary[chat_id][today_date] = message.text
        tele_bot.reply_to(message, "Saved!\nType 'Read diary' if you want to read your diary!"+
                      "\n\nPsst ... there will be only one diary saved in a day.")


@tele_bot.message_handler(func=lambda message: message.text is not None and
                          ('happy' in message.text or 'Happy'in message.text))
def reply_happy(message):
    '''Balasan bila input user adalah "happy"'''
    chat_id = message.chat.id # Mengambil chat ID
    photo = 'https://i.pinimg.com/564x/3a/36/a9/3a36a971fda04c8a60618c0223c5441d.jpg'
    tele_bot.reply_to(message, "Good to know you're happy, don't forget to "+
                      "be grateful!")
    tele_bot.send_photo(chat_id, photo)
    tele_bot.reply_to(message, "Do you want to write a diary about today? Type 'Yes diary' or 'No diary'.")

@tele_bot.message_handler(func=lambda message: message.text is not None and
                          ('sad' in message.text or 'Sad'in message.text))
def reply_sad(message):
    '''Balasan bila input user adalah "sad"'''
    chat_id = message.chat.id # Mengambil chat ID
    photo = 'https://i.pinimg.com/564x/70/e1/5d/70e15d30e0b6e4d0c64d7a97d9949c51.jpg'
    tele_bot.reply_to(message, "Don't be sad, remember Allah :)")
    tele_bot.send_photo(chat_id, photo)
    tele_bot.reply_to(message, "Do you want to write a diary about today? Type 'Yes diary' or 'No diary'.")

@tele_bot.message_handler(func=lambda message: message.text is not None and
                          ('angry' in message.text or 'Angry' in message.text))
def reply_angry(message):
    '''Balasan bila input user adalah "angry"'''
    chat_id = message.chat.id # Mengambil chat ID
    photo = 'https://i.pinimg.com/564x/7d/b1/f2/7db1f261887b8e521eec2dd43115350f.jpg'
    tele_bot.reply_to(message, "Take refuge to Allah :)")
    tele_bot.send_photo(chat_id, photo)
    tele_bot.reply_to(message, "Do you want to write a diary about today? Type 'Yes diary' or 'No diary'.")

@tele_bot.message_handler(func=lambda message: message.text is not None and
                          ('scared' in message.text or 'Scared' in message.text))
def reply_scared(message):
    '''Balasan bila input user adalah "scared"'''
    chat_id = message.chat.id # Mengambil chat ID
    photo = 'https://i.pinimg.com/564x/09/cb/c8/09cbc80e9e82b0974b10f90e761e13ed.jpg'
    tele_bot.reply_to(message, "What, why? You don't need to be scared!")
    tele_bot.send_photo(chat_id, photo)
    tele_bot.reply_to(message, "Do you want to write a diary about today? Type 'Yes diary' or 'No diary'.")


@tele_bot.message_handler(func=lambda message: message.text is not None)
def reply_else(message):
    '''Apabila input user selain di atas'''
    tele_bot.reply_to(message, "Please type the way you are instructed to.")


while True:
    # Mencegah berhentinya program apabila terjadi error pada Telegram
    try:
        tele_bot.polling()
    except:
        time.sleep(20)
