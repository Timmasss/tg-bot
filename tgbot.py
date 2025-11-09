import asyncio 
import logging 
from aiogram import F, Bot, Dispatcher,types 
from aiogram.filters import Command 
from aiogram.types import Message 
 
logging.basicConfig(level=logging.INFO) 
bot = Bot(token='7427831106:AAHxjPyOYbkwYzastoKNhsIXNY-4NrLohDE') 
dp = Dispatcher() 
 
@dp.message(Command("start")) 
async def cmd_name(message: Message): 
    await message.answer("Привет, я тестовый бот") 
 
@dp.message(Command("info")) 
async def cmd_name(message: Message): 
    await message.reply("У меня есть следующие команды") 
 
@dp.message(Command("name")) 
async def cmd_name(message:Message): 
    args=message.text.split(maxsplit=1) 
    if len(args)>1: 
        await message.answer(f"hello,<b>{args[1]}</b>",parse_mode="HTML") 
    else: 
         await message.answer("please write your name /name") 
 
@dp.message(Command("test")) 
async def cmd_name(message:Message): 
    await message.answer("Hello,<b>world</b>", parse_mode="HTML") 
    await message.answer("Hello, *world*\!",parse_mode="MarkdownV2")     
 
@dp.message(Command("button")) 
async def cmd_start(message: Message): 
    kb = [ 
        [types.KeyboardButton(text="Первая кнопка")], 
        [types.KeyboardButton(text="Вторая кнопка")] 
 
    ] 
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb) 
    await message.answer("Какую кнопку вы выбрали?", reply_markup=keyboard  )    
 
@dp.message(lambda message: message.text =="Первая кнопка") 
async def first_btn(message:Message): 
    await message.reply("Вы нажали первую кнопку")      
 
@dp.message(lambda message: message.text =="Вторая кнопка") 
async def first_btn(message:Message): 
    await message.reply("Вы нажали вторую кнопку") 
 
@dp.message(Command("special_buttons")) 
async def cmd_special_buttons(message: types.Message): 
    kb = [ 
        [types.KeyboardButton(text="Запросить контакт",request_contact=True)], 
        [types.KeyboardButton(text="Запросить Викторину",request_poll=types.KeyboardButtonPollType(type='quiz'))]         
    ] 
    keyboard=types.ReplyKeyboardMarkup(keyboard=kb) 
    await message.reply("Выберите Действие",reply_markup=keyboard) 
 
@dp.message(lambda message: message.text =="Запросить Викторину") 
async def send_quiz(message: types.Message): 
    question = "Сколько iQ у Ратмира?" 
    options = ['-1','10','20'] 
    correct_option_id = 0 
 
    await bot.send_poll( 
        chat_id=message.chat.id, 
        question=question, 
        options=options, 
        type='quiz', 
        correct_option_id=correct_option_id, 
        is_anonymous=False 
    )     
@dp.message(F.content_type=="animation") 
async def echo_gif(message: Message): 
    await message.reply_animation(message.animation.file_id) 
 
btn_keyboard=ReplyKeyboardMarkup( keyboard=[ 
        [KeyboardButton(text="horror")], 
        [KeyboardButton(text="action")], 
        [KeyboardButton(text="comedy")], 
        [KeyboardButton(text="fantasy")] 
    ], 
    resize_keyboard=True 
) 
horror=["https://www.kinopoisk.ru/film/5871/","https://www.kinopoisk.ru/film/1973/","https://www.kinopoisk.ru/film/1973/"] 
action=["https://www.kinopoisk.ru/film/432550/","https://www.kinopoisk.ru/film/885658/","https://www.kinopoisk.ru/film/1267348/"] 
comedy=["https://www.kinopoisk.ru/film/462360/","https://www.kinopoisk.ru/film/961715/","https://www.kinopoisk.ru/film/749540/"] 
fantasy=["https://www.kinopoisk.ru/film/8124/","https://www.kinopoisk.ru/series/77044/","https://www.kinopoisk.ru/film/1326397/"] 
 
@dp.message(Command("films")) 
async def cmd_name(message:Message): 
     await message.reply("choose genre",reply_markup=btn_keyboard) 
 
@dp.message(lambda message:message.text=="horror") 
async def show_horror(message: Message): 
    await message.reply("А вот и хороший ужастик"+random.choice(horror)) 
 
 
@dp.message(lambda message:message.text=="action") 
async def show_action(message: Message): 
    await message.reply("А вот ихороший экшен"+random.choice(action)) 
 
 
@dp.message(lambda message:message.text=="comedy") 
async def show_comedy(message: Message): 
    await message.reply("А вот и хороший комедия"+random.choice(comedy)) 
 
 
@dp.message(lambda message:message.text=="fantasy") 
async def show_fantasy(message: Message): 
    await message.reply("А вот и хороший фантазия"+random.choice(fantasy)) 
 
@dp.message(Command("weather")) 
async def start_command(message:Message): 
    await message.answer("Choose city to learn weather conditions")  
 
@dp.message(F.text) 
async def get_weather(message:types.Message): 
    city=message.text 
    try: 
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347" 
        weather_data=requests.get(url).json() 
 
        temperature=weather_data["main"]["temp"]  
        wind_speed = weather_data['wind']['speed'] 
        temperature_feels = weather_data["main"]["feels_like"] 
        cloud_cover = weather_data['weather'][0]['description'] 
        humidity=weather_data['main']['humidity']  
 
        await message.answer(f"air temprature:{temperature}\n" 
                            f"feels like:{temperature_feels}\n" 
                            f"wind:{wind_speed}m/s\n" 
                            f"clouds:{cloud_cover}\n" 
                            f"humidity:{humidity}%\n") 
        pass 
    except KeyError: 
        await message.answer("The city was not found") 
 
 
engine=pyttsx3.init() 
engine.setProperty("rate",150) 
engine.setProperty("volume",0.9) 
engine.say("You are welcome") 
engine.runAndWait() 
         
async def main(): 
    await dp.start_polling(bot) 
 
if __name__=="__main__": 
    asyncio.run(main())