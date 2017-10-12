#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import os
import sys
import json


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
