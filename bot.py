import os
import telebot
from datetime import datetime

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

business_owners = {}

@bot.business_connection_handler()
def handle_business_connection(connection):
    business_owners[connection.business_connection_id] = connection.user.id

# ----------------------------------------------------------------
# QISQA STANDART JAVOB
# ----------------------------------------------------------------
DEFAULT_REPLY = "Salom! 👋 Hozir band ekanman, tez orada javob beraman."

# ----------------------------------------------------------------
# KALIT SO'Z / IBORALAR -> QISQA JAVOB (kichik harflarda)
# ----------------------------------------------------------------
KEYWORD_REPLIES = {
    # Salomlashish
    "salom": "Assalomu Alaykum 😊 
    Tez orada javob beraman.",
    "assalomu alaykum": "Va alaykum assalom! Tez orada javob beraman.",
    "hey": "Salom! Tez orada javob beraman.",
    "hi": "Salom! Tez orada javob beraman.",
    "salomlar": "Salom! Tez orada javob beraman.",

    # Bot kimligi haqida
    "sen kimsan": "Men telegram egasining shaxsiy agentiman 🤖 U hozir band, men esa navbatchiman.",
    "kimsan": "Men uning shaxsiy yordamchisiman 🤖 Xabaringizni yetkazib qo'yaman.",
    "bot mi": "Ha, men botman, lekin his-tuyg'ularim bor deb hisoblang 😄 Tez orada egam o'zi javob beradi.",
    "robotmisan": "Ha, robotman, lekin yaxshi robotlardanman 🤖✨",

    # Qayerda ekanligi haqida
    "qayerda": "U hozir boshqa vazifalar bilan band, ammo xabaringiz yetib bordi ✅ Tez orada o'zi javob beradi.",
    "qayerdasiz": "Hozircha ko'rinmay turibdi, lekin qaytishi bilanoq javob beradi 🙂",
    "nimaqilyapsiz": "Menga qolsa, sizga javob yozib turibman 😄 Egam esa band, tez orada o'zi yozadi.",

    # Kundalik / kulgili
    "qalaysiz": "Zo'rman, rahmat! Siz-chi? 😄",
    "yaxshimisiz": "Ha, ajoyibman! Siz qalaysiz?",
    "nima gap": "Hammasi joyida! Sizda-chi? 😊",
    "zerikdim": "Ehh, zerikish yomon narsa 😅 Egam kelsa, albatta suhbatlashib beradi!",
    "charchadim": "Dam oling unda! 🍵 Men shu yerdaman, u kelguncha kutib turaman.",
    "kulgili gap ayt": "Dasturchi nega ko'chaga chiqmaydi? Chunki u 'bug' larni tuzatishdan charchamaydi 😂",
    "hazil": "Nega robot hech qachon ochlikni his qilmaydi? Chunki u faqat 'bayt' yeydi 😄",
    "rahmat": "Arzimaydi! 🙏",
    "tashakkur": "Arzimaydi! 🙏",
    "xayr": "Xayr! Yaxshi kun tilayman 👋",
    "ko'rishguncha": "Ko'rishguncha! 👋",
    "sog'inibman": "Awww, u ham sizni albatta sog'ingandir 🥰 Tez orada javob beradi!",
    "yoqtiraman": "Bu juda yoqimli! 😊 Egamga albatta yetkazib qo'yaman.",
}

WORKING_HOURS_START = 9
WORKING_HOURS_END = 18

def build_reply(text: str) -> str:
    lowered = text.lower()
    for keyword, reply in KEYWORD_REPLIES.items():
        if keyword in lowered:
            return reply
    hour = datetime.now().hour
    if hour < WORKING_HOURS_START or hour >= WORKING_HOURS_END:
        return DEFAULT_REPLY + "\n(Ish vaqtidan tashqari, ertalab javob beraman.)"
    return DEFAULT_REPLY

@bot.message_handler(func=lambda message: True, content_types=["text"])
def handle_message(message):
    reply = build_reply(message.text)
    bot.reply_to(message, reply)

@bot.business_message_handler(func=lambda message: True, content_types=["text"])
def handle_business_message(message):
    owner_id = business_owners.get(message.business_connection_id)
    if owner_id is None:
        try:
            connection = bot.get_business_connection(message.business_connection_id)
            owner_id = connection.user.id
            business_owners[message.business_connection_id] = owner_id
        except Exception:
            pass
    if owner_id is not None and message.from_user.id == owner_id:
        return
    reply = build_reply(message.text)
    bot.send_message(
        chat_id=message.chat.id,
        text=reply,
        business_connection_id=message.business_connection_id,
        reply_to_message_id=message.message_id,
    )

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.infinity_polling()
