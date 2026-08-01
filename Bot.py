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


# ----------------------------------------------------------------
# "Chatni avtomatlashtirish" orqali sizning shaxsiy chatlaringizga
# kelgan xabarlar ham shu handler orqali keladi (oddiy botga yozilgan
# xabarlardan farqli o'laroq). Telegram bunday xabarlarni alohida
# "business_message" turi sifatida yuboradi.
# ----------------------------------------------------------------
@bot.business_message_handler(func=lambda message: True, content_types=["text"])
def handle_business_message(message):
    reply = build_reply(message.text)
    # business_connection_id ko'rsatilishi SHART — aks holda javob
    # botning o'z nomidan emas, sizning profilingiz nomidan yuborilmaydi
    bot.send_message(
        chat_id=message.chat.id,
        text=reply,
        business_connection_id=message.business_connection_id,
        reply_to_message_id=message.message_id,
    )


if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.infinity_polling()
