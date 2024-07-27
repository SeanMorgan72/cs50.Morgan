import emoji
import sys

def main():
    user_input = input()
    emojized_output = emojize_text(user_input)
    print(f"{emojized_output}")
    sys.exit()


def emojize_text(text):
     return emoji.emojize(text, language= 'alias')


if __name__ == "__main__":
    main()