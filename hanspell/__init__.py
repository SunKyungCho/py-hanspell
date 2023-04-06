__version__ = '1.1'

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path

        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from hanspell import spell_checker

        with open("save.txt", "w") as f:
            with open('open.txt', newline='') as file:
                reader = file.readlines()
                for row in reader:
                    checked_text = ''
                    row = row.replace('&', '')
                    if len(row) > 500:
                        count = len(row) / 500
                        for i in range(int(count)):
                            result = spell_checker.check(row[i*500:(i+1)*500])
                            row = result.as_dict()['checked']
                            checked_text = checked_text + row
                    else:
                        result = spell_checker.check(row)
                        checked_text = result.as_dict()['checked']

                    print(checked_text)
                    checked_text = checked_text + '\n'
                    f.write(checked_text)
