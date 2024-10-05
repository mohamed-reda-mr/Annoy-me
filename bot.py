from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# وظيفة لحظر المستخدم
def ban_user_by_username(update: Update, context: CallbackContext):
    username = update.message.text.strip()  # اسم المستخدم المزعج الذي تم إرساله
    chat_id = update.message.chat_id

    # التأكد من أن الرسالة تبدأ بـ @ لتمييز أنها اسم مستخدم
    if username.startswith('@'):
        try:
            # البحث عن المستخدم في الجروب وحظره
            members = context.bot.get_chat_administrators(chat_id)
            for member in members:
                if member.user.username == username[1:]:
                    context.bot.kick_chat_member(chat_id, member.user.id)
                    update.message.reply_text(f"تم حظر المستخدم @{username}")
                    return
            update.message.reply_text(f"لم يتم العثور على المستخدم {username} في المجموعة.")
        except Exception as e:
            update.message.reply_text(f"حدث خطأ أثناء محاولة حظر {username}: {str(e)}")
    else:
        update.message.reply_text("يرجى إرسال اسم المستخدم المزعج بصيغة @username")

# الوظيفة الرئيسية لتشغيل البوت
def main():
    # ضع الـ Token الخاص بالبوت هنا
    updater = Updater("7327557278:AAEiElUmDOR6f_fLitX4YUlj59D6DBv03_8", use_context=True)

    dp = updater.dispatcher

    # ربط وظيفة حظر المستخدم برسالة يرسلها الضحية
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, ban_user_by_username))

    # تشغيل البوت
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
