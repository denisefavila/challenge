import argparse
import sys

from const import DEFAULT_INPUT_TEXT, DEFAULT_LIMIT, DEFAULT_JUSTIFY
from formater.idwall_formatter import IdwallFormatter


def main():

    text = 'This is a program to manipulate strings. You can give me a string with --text/-t ' \
           'an I\'ll return the same text with only n characters per line. The default value for n is 40, ' \
           'but you can define you\'re own value passing a --size/-s argument. Besides that, if you want ' \
           'a justified string, you just need to specify --justifify/-j'

    parser = argparse.ArgumentParser(description=text)
    parser.add_argument("--text", "-t", help="text to be manipulated")
    parser.add_argument("--size", "-s", help="characters per line")
    parser.add_argument("-j", "--justify", help="justify=true", action="store_true")

    argss = vars(parser.parse_args())

    input_text = argss["text"] or DEFAULT_INPUT_TEXT
    limit = int(argss["size"] or DEFAULT_LIMIT)
    justify = argss["justify"] or DEFAULT_JUSTIFY

    formatted_string = IdwallFormatter(input_text,
                                       limit,
                                       justify=True).format()

    print(formatted_string)


if __name__ == "__main__":
    main()
