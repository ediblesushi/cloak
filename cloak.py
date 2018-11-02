import sys, base64, click

array64 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=")

@click.group()
def main():
    pass

@main.command()
@click.argument('input', nargs=1)
@click.argument('cipher', nargs=1)
@click.argument('output', nargs=1, required=False, default=None)
def hide(input, cipher, output):
    with open(input, 'rb') as f:
        payloadb64 = base64.b64encode(f.read())

    with open('ciphers/{}'.format(cipher)) as c:
        cipherArray = c.readlines()

    if output:
        with open(output, 'w+') as f:
            for char in payloadb64.decode("utf-8"):
                if char != '\n':
                    f.write(cipherArray[array64.index(char)])
    else:
        for char in payloadb64.decode("utf-8"):
            if char != '\n':
                print(cipherArray[array64.index(char)], end='')


@main.command()
@click.argument('input', nargs=1)
@click.argument('cipher', nargs=1)
@click.argument('output', nargs=1, required=False, default=None)
def show(input, cipher, output):
    with open(input) as f:
        list = f.readlines()

    with open(cipher) as c:
        cipherArray = c.readlines()

    clear64 = ""

    for word in list:
        clear64 += array64[cipherArray.index(word)]

    if output:
        with open(output, 'w+') as f:
            f.write(base64.b64decode(clear64).decode('utf-8'))
    else:
        print(base64.b64decode(clear64).decode('utf-8'))

if __name__ == "__main__":
    main()
