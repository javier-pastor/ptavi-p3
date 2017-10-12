#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve
import os
import sys
import json
import fileinput


class KaraokeLocal(SmallSMILHandler):
    """
        Esta clase se utiliza para orientar a objetos el programa karaoke.py
    """

    def constructor(self, smil_file):
        """
            Inicializa parser
        """
        parser = make_parser()
        parser.setContentHandler(self)
        try:
            parser.parse(open(smil_file))
            self.list = self.get_tags()
        except IOError:
            print ('File not found')
            raise SystemExit

    def print_list(self):
        """
            Imprimo etiquetas y archivos
        """
        for elem in self.list:
            print("\n" + elem[0] + "\t", end = "") #that end is for printing same line
            for attr in elem[1]:
                print (attr + '="' + (elem[1][attr])+ '"' + "\t", end = "")
        print("\n")

    def save_json(self):
        with open('karaoke.json', 'w') as file:
            json.dump(self.list, file)

    def do_local(self):
        """
            Descarga archivos remotos y los hace locales
        """
        for elem in self.list:
            for attr in elem[1]:
                if attr == 'src' and elem[1][attr][:7] == 'http://':
                    source = elem[1][attr]
                    urlretrieve(source, elem[1][attr][(elem[1][attr].rfind('/'))+1:])
                    elem[1][attr] = elem[1][attr][(elem[1][attr].rfind('/'))+1:]
                    with fileinput.FileInput("karaoke.smil", inplace=True, backup='.bak') as file:
                        for line in file:
                            print(line.replace(source, elem[1][attr]), end='')


if __name__ == '__main__':
    try:
        smil_file = str(sys.argv[1])
    except IndexError:
        print ('Usage: python3 karaoke.py file.smil')
        raise SystemExit
    Karaoke = KaraokeLocal()
    Karaoke.constructor(smil_file)
    Karaoke.print_list()
    Karaoke.save_json()
    Karaoke.do_local()
