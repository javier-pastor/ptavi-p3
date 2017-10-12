#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    """
        Esta clase es un manejador Smil
    """

    def __init__(self):
        self.list = []

    def startElement(self, name, attrs):
        """
            Crea una lista con las etiquetas y atributos de un archivo smil
        """

        tags_list = ['root-layout', 'region', 'img', 'audio', 'textstream']

        if name in tags_list:
            attrs_dicc = {}
            for attr in attrs.keys():
                attrs_dicc[str(attr)] = str(attrs.get(attr, ''))
            self.list.append([name, attrs_dicc])

    def get_tags(self):
        """
            Devuelve la lista de etiquetas y atributos del archivos smil
        """
        return self.list

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.get_tags())
