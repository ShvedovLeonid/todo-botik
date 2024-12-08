import telebot 
from models import TaskModel

class Controller:
    def __init__(self, bot):
        self.bot:telebot.TeleBot = bot

    def add_task_handler(self, message):
        TaskModel.add_tesk(message.chat.id, message.text)
        message.reply_to(message, "Задача добавлена!")

    def register_handlers(self):
        @self.bot.message_handler(commands = ['start'])
        def send_welcome(message):
            self.bot.reply_to(message, "Это Todo-bot")
    
        @self.bot.message_handler(commands = ['add'])
        def add_task(message):
            msg = self.bot.reply_to(message, "Введите текст задачи:")
            self.bot.register_next_step_handler(msg, self.add_task_handler)
            
        