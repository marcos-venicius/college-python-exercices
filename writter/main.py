#!/usr/bin/env python3

from prompt import Prompter
from functions import dec_to_bin, bin_to_dec


def main():
    prompt = Prompter(True, True)

    equation = prompt.prompt("equation: ")

    commands = {
        'dec_to_bin': {
            'args': {
                'count': 1
            },
            'exec': dec_to_bin
        },
        'bin_to_dec': {
            'args': {
                'count': 1
            },
            'exec': bin_to_dec
        }
    }

    try:
        while (response := next(equation)) != 'quit()':
            command = response.split('(')[0].strip()

            if command in commands and response.count('(') == 1 and response.count(')') == 1:
                open_bracket_index = response.index('(')
                close_bracket_index = response.index(')')
                args = [arg for arg in response[open_bracket_index + 1:close_bracket_index].split(',') if arg.strip() != '']

                args_count = int(commands[command]['args']['count'])

                if len(args) != args_count:
                    print(f'[!!] this command expects {args_count} arguments but received {len(args)}')
                    continue

                stop = False
                for key, arg in enumerate(args):
                    if (arg.startswith("'") and arg.endswith("'")) or (arg.startswith('"') and arg.endswith('"')):
                        args[key] = str(arg[1:-1])
                    elif not arg.strip().isnumeric():
                        print('[!!] invalid parameter type')
                        stop = True
                        break
                    else:
                        args[key] = float(arg)

                if stop:
                    continue

                result = commands[command]['exec'](*args)

                print(result)
    except KeyboardInterrupt:
        print()
        exit()


if __name__ == '__main__':
    main()
