import asyncio
from binance.client import Client
from telegram import Bot
import json
from datetime import datetime
import logging
import nest_asyncio

nest_asyncio.apply()

# 设置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 币安API配置
api_key = ""
secret = ""
client = Client(api_key, secret)

# Telegram配置
BOT_TOKEN = ""
CHAT_ID = 

class PriceMonitor:
    def __init__(self):
        self.previous_prices = {}
        self.bot = Bot(BOT_TOKEN)
        
    async def send_alert(self, alert_message):
        try:
            await self.bot.send_message(chat_id=CHAT_ID, text=alert_message)
            logger.info(f"Alert sent successfully: {alert_message}")
        except Exception as e:
            logger.error(f"Error sending alert: {e}")

    async def check_price_changes(self):
        while True:
            try:
                # 获取所有交易对的价格
                current_prices = client.get_symbol_ticker()
                alert_messages = []

                # 检查价格变化
                for ticker in current_prices:
                    symbol = ticker['symbol']
                    current_price = float(ticker['price'])
                    
                    if symbol in self.previous_prices:
                        prev_price = self.previous_prices[symbol]
                        # 确保previous_price不为0且current_price是有效值
                        if prev_price > 0 and current_price > 0:
                            price_change = (current_price - prev_price) / prev_price * 100
                            
                            # 如果价格变化超过1%
                            if abs(price_change) > 1:
                                direction = "+" if price_change > 0 else "-"
                                message = f"{symbol}: 价格波动: {direction}{abs(price_change):.2f}%"
                                alert_messages.append(message)
                    else:
                        # 新增交易对提醒
                        message = f"新增交易对: {symbol}, 当前价格: {current_price}"
                        alert_messages.append(message)
                    
                    # 更新上一次的价格
                    self.previous_prices[symbol] = current_price

                # 如果有需要提醒的价格变化，一次性发送
                if alert_messages:
                    await self.send_alert("\n".join(alert_messages))

            except Exception as e:
                logger.error(f"Error in price monitoring: {e}")

            # 等待2秒
            await asyncio.sleep(2)

async def main():
    monitor = PriceMonitor()
    await monitor.check_price_changes()

if __name__ == "__main__":
    asyncio.run(main())