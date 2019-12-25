import os


def main():
    try:
        with open('counter.txt', 'x') as file:
            file.write('1')
            file.close()
            os.chmod('counter.txt', 0o777)
            return 0
    except:
        with open('counter.txt', 'r+') as file:
            try:
                data = int(file.read())
            except:
                return 1
            file.seek(0)
            file.write(str(data+1))
            file.truncate()
            return 0


if __name__ == '__main__':
    main()
