import telebot
import random

# Встав сюди токен свого бота від @BotFather
TOKEN = '8583425066:AAESr8dUSdgZdCPN0LWLsiWHK2fge1iRZZ4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Вітаю! Щоб отримати код доступу до адмін-панелі, введіть команду /getcode")

@bot.message_handler(commands=['getcode'])
def give_code(message):
    # Генеруємо випадковий 6-значний код
    auth_code = str(random.randint(100000, 999999))
    
    # Відправляємо код користувачу
    bot.send_message(
        message.chat.id, 
        f"🔐 Ваш код доступу: `{auth_code}`\n\nВведіть його на сторінці авторизації.",
        parse_mode="Markdown"
    )
    # Виводимо в консоль для контролю
    print(f"Користувач {message.from_user.first_name} отримав код: {auth_code}")

print("Бот запущений і доступний для всіх...")
bot.infinity_polling()
