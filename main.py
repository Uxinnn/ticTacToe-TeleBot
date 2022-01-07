from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from tictactoe import init_game, print_game_state, take_turn, check_win


BOT_TOKEN = "1717925286:AAFWjuPMC7YmhAqAcSX-V-xNQPhW66KfRPA"


def start(update, context):
    context.user_data["game_state"] = init_game()
    context.user_data["player"] = "X"
    context.bot.send_message(
        text=f"Let's play tic tac toe!\n\n{print_game_state(context.user_data['game_state'])}\n\nPlayer X's turn.",
        chat_id=update.message.chat_id
    )
    return 0


def player_x(update, context):
    chat_id = update.message.chat.id
    text = update.message.text
    pos = tuple(map(int, text.strip().split()))
    game_state = context.user_data["game_state"]
    player = context.user_data["player"]
    next_player = take_turn(game_state, player, pos)
    winner = check_win(game_state)
    if winner is not None:
        context.bot.send_message(
            text=f"player {player} WIN!\n\n{print_game_state(context.user_data['game_state'])}",
            chat_id=chat_id
        )
        return ConversationHandler.END

    context.user_data["player"] = next_player
    context.bot.send_message(
        text=f"Player {next_player}'s turn.\n\n{print_game_state(context.user_data['game_state'])}",
        chat_id=chat_id
    )

    return 0


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            0: [
                MessageHandler(Filters.text & ~Filters.command, player_x)
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
