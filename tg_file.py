import json
from os import terminal_size
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from attr import Factory
from config import token
import main as mn

bot = Bot(token=token)
dp = Dispatcher(bot)

with open("type_of_sports.json","r") as f:
    tp_sp = json.load(f)

lst_tp_sp = ""
for key, value in tp_sp.items():
    lst_tp_sp += f"{key}" + f"{value} \n"
    
lst_tp_sp = lst_tp_sp[0:-1]

# список футбольных турниров
with open("list_of_name_turn.json","r") as fl:
    list_of_name_turn = json.load(fl)

# main buttons
btn_news, btn_res  = KeyboardButton("Новости"),KeyboardButton("Результаты игр")

main_rows = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(btn_news).row(btn_res)

# sort of sport buttons
btn1, btn2, btn3 = KeyboardButton("1"),KeyboardButton("2"), \
    KeyboardButton("3")

crt_rows = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    btn1, btn2, 
).row(
    btn3
)

# championship lists
# football
btn_ftb_chmp1, btn_ftb_chmp2, btn_ftb_chmp3 = KeyboardButton("Англия"),\
    KeyboardButton("Испания"), KeyboardButton("Германия")

crt_rows_ftbl = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    btn_ftb_chmp1, btn_ftb_chmp2
).add(
    btn_ftb_chmp3
)

# hokkey
btn_hkk_chmp1, btn_hkk_chmp2, btn_hkk_chmp3 = KeyboardButton("НХЛ"),\
    KeyboardButton("КХЛ"), KeyboardButton("ВХЛ")

crt_rows_hkk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    btn_hkk_chmp1, btn_hkk_chmp2
).add(
    btn_hkk_chmp3
)

# basketball
btn_bskt_chmp1 = KeyboardButton("Лига ВТБ")
crt_rows_bskt = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_bskt_chmp1)

# move_button
bth_main = KeyboardButton("На главную")
crt_mv_btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(bth_main)


@dp.message_handler(commands="start")
async def start(message: types.Message):  
    await message.answer("Вас приветствует бот новостей и результатов спортивных игр."+\
        " Выберите, чтобы вы хотели посмотреть:\n\n                 Новости <----> "+\
            "Результаты игр", reply_markup=main_rows)


@dp.message_handler(content_types=["text"])
async def gener(message: types.Message):
    if message.text == "Новости":
        mn.get_news()
        with open("news.json","r") as fl:
            news = json.load(fl)

        for key, value in news.items():
            list_news = f"\nВремя публикации: {value['time']}\n" + f"{value['link']}" 
    
            await message.answer(list_news, reply_markup=crt_mv_btn)
    
    elif message.text == "Результаты игр":
        await message.answer("Выберите вид спорта:\n" + \
            lst_tp_sp, reply_markup=crt_rows)

    elif message.text == "На главную":
        await message.answer("Выберите, чтобы вы хотели посмотреть:\n\n          Новости <----> "+\
            "Результаты игр", reply_markup=main_rows)


    elif message.text == "1":
        await message.answer("Выберите чемпионат:\n" + \
            "1. Англия\n2. Испания\n3. Германия", reply_markup=crt_rows_ftbl)

    elif message.text == "2":
        await message.answer("Выберите чемпионат:\n" + \
            "1. НХЛ\n2. КХЛ\n3. ВХЛ", reply_markup=crt_rows_hkk)

    elif message.text == "3":
        await message.answer("Выберите чемпионат:\n" + \
            "1. Лига ВТБ", reply_markup=crt_rows_bskt)

    elif message.text == "Англия":
        mn.get_football_games()

        # список английских игр
        with open("ftb_res/angl_ftb_games.json","r") as fl:
            angl_ftb_games = json.load(fl)

        angl_lst_ftb_games = ""

        for key, value in angl_ftb_games.items():
            angl_lst_ftb_games += f"{value['home_team']}" + " " + f"{value['score']}"+ " " + f"{value['guest_team']}\n"

        angl_lst_ftb_games = angl_lst_ftb_games[0:-1]

        await message.answer(f"{list_of_name_turn[0]}. \nСписок игр:" + "\n\n" + f"{angl_lst_ftb_games}",\
                reply_markup=crt_mv_btn)
    
    elif message.text == "Испания":
        mn.get_football_games()

        # список испанских игр
        with open("ftb_res/isp_ftb_games.json","r") as fl:
            isp_ftb_games = json.load(fl)

        isp_lst_ftb_games = ""

        for key, value in isp_ftb_games.items():
            isp_lst_ftb_games += f"{value['home_team']}" + " " + f"{value['score']}"+ " " + f"{value['guest_team']}\n"

        isp_lst_ftb_games = isp_lst_ftb_games[0:-1]
    
        await message.answer(f"{list_of_name_turn[1]}. \nСписок игр:" + "\n\n" + f"{isp_lst_ftb_games}",\
                reply_markup=crt_mv_btn)
    
    elif message.text == "Германия":
        mn.get_football_games()

        # список немецких игр
        with open("ftb_res/germ_ftb_games.json","r") as fl:
            germ_ftb_games = json.load(fl)

        germ_lst_ftb_games = ""

        for key, value in germ_ftb_games.items():
            germ_lst_ftb_games += f"{value['home_team']}" + " " + f"{value['score']}"+ " " + f"{value['guest_team']}\n"

        germ_lst_ftb_games = germ_lst_ftb_games[0:-1]
    
        await message.answer(f"{list_of_name_turn[2]}. \nСписок игр:" + "\n\n" + f"{germ_lst_ftb_games}",\
                reply_markup=crt_mv_btn)

    elif message.text == "НХЛ":
        mn.get_hokkey_games()

        # список игр НХЛ
        with open("hkk_res/nhl_hkk_games.json","r") as fl:
            nhl_hkk_games = json.load(fl)

        nhl_hkk_list_games = ""

        for key, value in nhl_hkk_games.items():
            nhl_hkk_list_games += f"{value['home_team']}" + " " + f"{value['score']}"+ " " + f"{value['guest_team']}\n"

        nhl_hkk_list_games = nhl_hkk_list_games[0:-1]
    
        await message.answer(f"{list_of_name_turn[3]}. \nСписок игр:" + "\n\n" + f"{nhl_hkk_list_games}",\
                reply_markup=crt_mv_btn)

    elif message.text == "КХЛ":
        mn.get_hokkey_games()

        # список игр КХЛ
        with open("hkk_res/khl_hkk_games.json","r") as fl:
            khl_hkk_games = json.load(fl)

        khl_hkk_list_games = ""

        for key, value in khl_hkk_games.items():
            khl_hkk_list_games += f"{value['home_team']}" + " " + f"{value['score']}"+ " " + f"{value['guest_team']}\n"

        khl_hkk_list_games = khl_hkk_list_games[0:-1]
    
        await message.answer(f"{list_of_name_turn[4]}. \nСписок игр:" + "\n\n" + f"{khl_hkk_list_games}",\
                reply_markup=crt_mv_btn)
    
    elif message.text == "ВХЛ":
        mn.get_hokkey_games()

        # список игр VHL
        with open("hkk_res/vhl_hkk_games.json","r") as fl:
            vhl_hkk_games = json.load(fl)

        vhl_hkk_list_games = ""

        for key, value in vhl_hkk_games.items():
            vhl_hkk_list_games += f"{value['home_team']}" + " " + f"{value['score']}"+ " " + f"{value['guest_team']}\n"

        vhl_hkk_list_games = vhl_hkk_list_games[0:-1]

        await message.answer(f"{list_of_name_turn[5]}. \nСписок игр:" + "\n\n" + f"{vhl_hkk_list_games}",\
                reply_markup=crt_mv_btn)
    
    elif message.text == "Лига ВТБ":
        mn.get_basketball_games()

        # баскетбол
        # Лига ВТБ
        with open("bskt_res/vtb_bkst_games.json","r") as fl:
            vtb_bkst_games = json.load(fl)

        vtb_bkst_list_games = ""

        for key, value in vtb_bkst_games.items():
            vtb_bkst_list_games += f"{value['home_team']}" + " " + f"{value['score']}"+ " " + f"{value['guest_team']}\n"

        vtb_bkst_list_games = vtb_bkst_list_games[0:-1]
    
        await message.answer(f"{list_of_name_turn[6]}. \nСписок игр:" + "\n\n" + f"{vtb_bkst_list_games}",\
                reply_markup=crt_mv_btn)

    else:
        await message.answer("Я Вас не понимаю. Пожалуйста, нажмите на одну из"+ \
            "имеющихся кнопок c интересующим Вас контентом:\n\n          Новости <----> Результаты игр",
            reply_markup=main_rows)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=False)
 