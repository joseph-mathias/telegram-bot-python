## telegram-bot-python
Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages, commands and inline requests. You control your bots using HTTPS requests to Telegram's Bot API.

##1. What can I do with bots?
[A chat with a bot also showing search results from the @gif inline-bot]

To name just a few things, you could use bots to:

    Get customized notifications and news. A bot can act as a smart newspaper, sending you relevant content as soon as it's published.

    Integrate with other services. A bot can enrich Telegram chats with content from external services.
    Gmail Bot, GIF bot, IMDB bot, Wiki bot, Music bot, Youtube bot, GitHubBot

    Accept payments from Telegram users. A bot can offer paid services or work as a virtual storefront. Read more »
    Demo Shop Bot, Demo Store

    Create custom tools. A bot may provide you with alerts, weather forecasts, translations, formatting or other services.
    Markdown bot, Sticker bot, Vote bot, Like bot

    Build single- and multiplayer games. A bot can offer rich HTML5 experiences, from simple arcades and puzzles to 3D-shooters and real-time strategy games.
    GameBot, Gamee

    Build social services. A bot could connect people looking for conversation partners based on common interests or proximity.

    Do virtually anything else. Except for dishes — bots are terrible at doing the dishes.

##2. How do bots work?

At the core, Telegram Bots are special accounts that do not require an additional phone number to set up. Users can interact with bots in two ways:

    Send messages and commands to bots by opening a chat with them or by adding them to groups.
    Send requests directly from the input field by typing the bot's @username and a query. This allows sending content from inline bots directly into any chat, group or channel.

Messages, commands and requests sent by users are passed to the software running on your servers. Our intermediary server handles all encryption and communication with the Telegram API for you. You communicate with this server via a simple HTTPS-interface that offers a simplified version of the Telegram API. We call that interface our Bot API.
