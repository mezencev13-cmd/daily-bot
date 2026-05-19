import asyncio
import random
from datetime import datetime, timedelta
import pytz
from telegram import Bot

TOKEN = "8614280760:AAEZJgrje1rTYxCjwL3Ql1w2Ax0Jsx7cFxg"
CHAT_ID = 104815136

async def send_daily_message():
    bot = Bot(token=TOKEN)
    while True:
        now = datetime.now(pytz.timezone("Europe/Moscow"))
        
        random_hour = random.randint(9, 23)
        random_minute = random.randint(0, 59)
        
        target = now.replace(hour=random_hour, minute=random_minute, second=0, microsecond=0)
        if target <= now:
            target = target + timedelta(days=1)
        
        wait_seconds = (target - now).total_seconds()
        await asyncio.sleep(wait_seconds)
        
        await bot.send_message(
            chat_id=CHAT_ID,
            text="⏳ Прошёл ещё один день. Как ты его провёл?"
        )

if __name__ == "__main__":
    asyncio.run(send_daily_message())
