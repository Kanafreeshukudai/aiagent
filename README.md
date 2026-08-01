# Shaxsiy Telegram avtomatlashtirish boti

Bu bot sizga yozilgan xabarlarga oldindan tayyorlangan javoblar bilan avtomatik
javob beradi. To'liq bepul ishga tushirish uchun quyidagi qadamlarni bajaring.

## 1-qadam: Bot yaratish (BotFather orqali)

1. Telegram'da **@BotFather** ni toping va oching
2. `/newbot` buyrug'ini yuboring
3. Botga nom bering (masalan: "Mening Yordamchim")
4. Foydalanuvchi nomini bering — oxiri `bot` bilan tugashi kerak (masalan: `mening_yordamchim_bot`)
5. BotFather sizga bir qatorlik **TOKEN** beradi, masalan:
   `123456789:AAExampleTokenHereXXXXXXXXXXXXXXXXXXX`
6. Bu tokenni saqlab qo'ying — hech kimga bermang!

## 2-qadam: Kodni GitHub'ga yuklash

1. github.com'da yangi repository (ombor) yarating, masalan `telegram-bot`
2. Ushbu papkadagi barcha fayllarni (`bot.py`, `requirements.txt`, `Procfile`,
   `.gitignore`) o'sha repositoryga yuklang (GitHub saytida "Upload files"
   tugmasi orqali ham qilsa bo'ladi — terminal shart emas)

## 3-qadam: Railway'da joylashtirish

1. https://railway.app saytiga kirib, GitHub hisobingiz orqali ro'yxatdan o'ting
2. "New Project" → "Deploy from GitHub repo" ni tanlang
3. Yuqorida yaratgan repository'ni tanlang
4. Railway loyihasi ochilgach, **Variables** bo'limiga o'ting va yangi
   o'zgaruvchi qo'shing:
   - Nomi: `BOT_TOKEN`
   - Qiymati: BotFather bergan tokeningiz
5. Saqlang — Railway avtomatik ravishda botni qayta ishga tushiradi

Shu bilan tugadi! Bot endi 24/7 ishlab turadi. Botga Telegram'da xabar yozib
sinab ko'ring.

## Javoblarni o'zgartirish

`bot.py` faylidagi `DEFAULT_REPLY` va `KEYWORD_REPLIES` qismlarini tahrirlab,
xohlagan javoblaringizni yozishingiz mumkin. O'zgartirgandan so'ng, GitHub'da
faylni yangilang — Railway avtomatik ravishda yangi versiyani joylashtiradi.

## Muhim eslatma

Bu oddiy bot **AI emas** — u faqat oldindan yozilgan matnlar bilan javob
beradi. Agar kelajakda haqiqiy AI (masalan Claude yoki ChatGPT) bilan
"tushunib" javob beradigan qilishni xohlasangiz, bu alohida qadam bo'ladi.
