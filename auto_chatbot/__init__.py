from smartbot import SmartBot


def main(chatbot: SmartBot):
    while True:
        usr_input = input('You: ')

        if len(usr_input) > 0:

            if usr_input == '0':
                chatbot.bot.trainer.export_for_training('./my_export.json')
                exit(0)

            output = chatbot.get_response(usr_input)
            print('Bot:', output)


if __name__ == "__main__":
    chat_bot = SmartBot()
    main(chat_bot)
