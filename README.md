# Binance-Price-Change-Alert
Binance Price Change Alert
---

# Price Alert Monitor

该项目通过调用 Binance API 实时监控所有交易对的价格波动，并使用 Telegram Bot 发送提醒。当价格波动超过 1% 或新增交易对时，程序会自动发送提醒消息到指定的 Telegram 聊天窗口。

## 功能特点

- **实时监控**：每隔 2 秒钟获取 Binance 所有交易对的最新价格数据。
- **价格波动提醒**：当某个交易对价格变化超过 1% 时，自动发送提醒。
- **新增交易对通知**：对新出现的交易对进行通知。
- **异步处理**：使用 Python 的 asyncio 实现异步任务，提高效率。
- **日志记录**：详细记录运行过程中的信息及错误，方便调试与维护。

## 安装依赖

你可以使用 pip 安装所需的依赖包：

```bash
pip install python-binance python-telegram-bot nest_asyncio
```

## 配置说明

在 `price_alert.py` 文件中，你需要进行如下配置：

1. **Binance API 密钥**  
   - 在代码中填写你的 Binance `api_key` 和 `secret`。
2. **Telegram Bot 配置**  
   - 将 `BOT_TOKEN` 设置为你的 Telegram 机器人 token。  
   - 将 `CHAT_ID` 设置为你要发送提醒消息的聊天 ID。
   - 通过asyncio.sleep配置时间间隔
   - 通过if abs(price_change) > 1:配置波动警报

确保你已经创建了 Telegram 机器人，并且在 Telegram 中获得了相应的聊天 ID。

## 运行方式

在配置好 API 密钥和 Telegram Bot 信息后，可以直接运行该脚本：

```bash
python price_alert.py
```

程序将会不断监控价格变化，并在满足条件时向 Telegram 发送提醒消息。

## 日志记录

程序使用 Python 的 logging 模块记录运行日志。日志格式包括时间、模块名称、日志级别及详细信息。你可以根据需要调整日志级别和输出格式。

## 注意事项

- 请妥善保管好你的 Binance API 密钥和 Telegram Bot Token，避免泄露。
- 程序每 2 秒获取一次数据，请注意 API 调用频率是否符合 Binance 的限制。
- 如需修改价格提醒阈值或监控频率，可调整 `check_price_changes` 方法中的逻辑和 `asyncio.sleep` 的时间参数。

## 贡献与反馈

欢迎提交 Issue 或 Pull Request 来改进此项目。如果你在使用过程中遇到问题，请随时联系。

## 许可

该项目使用 [MIT 许可证](LICENSE)
