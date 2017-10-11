#!/usr/bin/python3
# -*- coding: utf-8 -*-


from xml.sax import make_parser  # metodo
from xml.sax.handler import ContentHandler  # clase


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.root_layout = {}  # esto es para decir que info guardar
        self.region = {}
        self.img = {}
        self.audio = {}
        self.textstream = {}
        self.list = list()

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.root_layout['width'] = attrs.get('width', "")
            self.root_layout['height'] = attrs.get('height', "")
            self.root_layout['bground_clr'] = attrs.get('background-color', "")
            self.list.append("Etiqueta : " + name + "\n")
            self.list.append("Atributos : " + str(self.root_layout))
        elif name == 'region':
            self.region['id'] = attrs.get('ud', "")
            self.region['top'] = attrs.get('height', "")
            self.region['bottom'] = attrs.get('bottom', "")
            self.region['left'] = attrs.get('left', "")
            self.region['right'] = attrs.get('right', "")
            self.list.append("Etiqueta : " + name)
            self.list.append("Atributos : " + str(self.region))
        elif name == 'img':
            self.img['src'] = attrs.get('src', "")
            self.img['region'] = attrs.get('region', "")
            self.img['begin'] = attrs.get('begin', "")
            self.img['dur'] = attrs.get('dur', "")
            self.list.append("Etiqueta : " + name)
            self.list.append("Atributos : " + str(self.img))
        elif name == 'audio':
            self.audio['src'] = attrs.get('src', "")
            self.audio['begin'] = attrs.get('begin', "")
            self.audio['dur'] = attrs.get('dur', "")
            self.list.append("Etiqueta : " + name)
            self.list.append("Atributos : " + str(self.audio))
        elif name == 'textstream':
            self.textstream['src'] = attrs.get('src', "")
            self.textstream['region'] = attrs.get('region', "")
            self.list.append("Etiqueta : " + name)
            self.list.append("Atributos : " + str(self.textstream))

    def get_tags(self):
        return self.list


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
