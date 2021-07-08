#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.menu import build_menu
from utils.message import message

def init(update, context):
    bot = context.bot
    msg=str(update.message.text[7:]).strip()
    if msg != "":
        main_text = "Ecco i risultati della tua ricerca su NodeRed Flows"
        gurl = "https://flows.nodered.org/search?term={0}".format(msg.replace(' ','+'))
        button_list = [InlineKeyboardButton("Go to =>", url=gurl)]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        bot.send_message(update.message.chat_id,text=main_text,reply_markup=reply_markup,parse_mode='HTML')
    else:
        message(update,context, text="Devi inserire un termine di ricerca!\nEsempio: <code>/search android</code>")