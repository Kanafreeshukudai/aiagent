import os
import telebot
from datetime import datetime

# Bot tokenini Railway'dagi "Variables" bo'limidan o'qiydi (kodga yozilmaydi!)
TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# ----------------------------------------------------------------
# SHU YERDA O'ZINGIZ XOHLAGAN JAVOBLARNI TAHRIRLASHINGIZ MUMKIN
# ----------------------------------------------------------------

DEFAULT_REPLY = (
    "Salom! 👋 Hozircha band bo'lganim uchun shaxsan javob bera olmayapman, "
    "lekin xabaringizni ko'rdim va imkon bo'lishi bilan albatta javob beraman."
)

# Kalit so'z -> maxsus javob (kichik harflarda yozilsin)
KEYWORD_REPLIES = {
    "salom": "Salom! Qalaysiz? 😊 Tez orada shaxsan javob beraman.",
    "assalomu alaykum": "Va alaykum assalom! Xabaringiz uchun rahmat, tez orada javob beraman.",
    "narx": "Narxlar bo'yicha savolingiz uchun rahmat, batafsil ma'lumotni tez orada yuboraman.",
    "qachon": "Vaqt bo'yicha savolingizni ko'rdim, iloji boricha tezroq javob berishga harakat qilaman.",
}

# Ish vaqtidan tashqarida boshqacha javob berish (ixtiyoriy)
WORKING_HOURS_START = 9
WORKING_HOURS_END = 18


def build_reply(text: str) -> str:
    lowered = text.lower()
    for keyword, reply in KEYWORD_REPLIES.items():
        if keyword in lowered:
            return reply

    hour = datetime.now().hour
    if hour < WORKING_HOURS_START or hour >= WORKING_HOURS_END:
        return DEFAULT_REPLY + "\n\n(Hozir ish vaqtidan tashqari, ertalab javob beraman.)"

    return DEFAULT_REPLY


@bot.message_handler(func=lambda message: True, content_types=["text"])
def handle_message(message):
    reply = build_reply(message.text)
    bot.reply_to(message, reply)


if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.infinity_polling()
