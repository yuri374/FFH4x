import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7502128435:AAGRm3i-gRKpgYCj9dk9tuymPgLNeAn7Ork"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Envie /getkey para receber uma key de acesso ao painel.")

async def getkey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("keys.json", "r") as f:
        keys = json.load(f)

    for key, info in keys.items():
        if not info["used"]:
            info["used"] = True
            with open("keys.json", "w") as f_out:
                json.dump(keys, f_out, indent=4)
            await update.message.reply_text(f"Sua key: {key}\nUse no painel: https://painel.seujogo.com")
            return

    await update.message.reply_text("❌ Todas as keys foram usadas.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getkey", getkey))
    app.run_polling()

if __name__ == "__main__":
    main()
