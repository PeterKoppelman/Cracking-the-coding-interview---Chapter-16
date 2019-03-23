# XML encoding. Map XML tags to pre-deifined integers. Problem 16.12
# Peter Koppelman January 21, 2018

dict_xml = {'family': 1, 'person': 2, 'firstname': 3, 'lastname': 4, 'state': 5}


def xml_encoding(xml):
    print(dict_xml)
    print(xml.split(' '))
    print()
    new_string = ''
    for x in xml.split(' '):
        print('x = ', x)
        # beginning of tag
        if (x[0:1]) == '<' and x[1:2] != '/':
            new_string += ' ' + str(dict_xml.get(x[1:])) + ' '
        # end of tag
        elif '</' in x:
            new_string += '0 '
        else:
            # check to see if part of the string is a key
            found = False
            for key, value in dict_xml.items():
                if key in x:
                    found = True
                    new_string += ' ' + str(value) + ' ' + x[len(key) + 1:].strip('>').strip('"')
                    if '>' in x:
                        new_string += ' 0 '
            if not found:
                new_string += x + ' '

    print(new_string)


if __name__ == '__main__':
    xml = '<family lastname="McDowell" state="Ca"> ' + \
                '<person firstname="Gayle"> Some message </person> ' + \
          '</family>'
    xml_encoding(xml)
