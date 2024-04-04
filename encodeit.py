#!/usr/bin/env python3
# Path: encodeit.py
"""
This script encodes and decodes the URL encoded text.
__author__ = "Paul McDowell"
__copyright__ = "Copyright 2024"
__license__ = "MIT"
__version__ = "1.0"
__date__ = "2024-03-10"
__maintainer__ = "Paul McDowell"
"""

import urllib.parse
import sys
import base64
import argparse

class EncodeIt:
    parser = argparse.ArgumentParser(description="Encode and decode the URL encoded text.")

    def __init__(self):
        """
        Constructor
        """
        self.setupParser()
        args = self.parser.parse_args()
        
        if(args.mode == "encode"):
            if(args.format == "url"):
                print(self.EncodeUrl(input("Enter clear text: ")))
            elif(args.format == "base64"):
                print(self.EncodeBase64(input("Enter clear text: ")))
        else:
            if(args.format == "url"):
                print(self.DecodeUrl(input("Enter encoded text: ")))
            elif(args.format == "base64"):
                print(self.DecodeBase64(input("Enter encoded text: ")))
        sys.exit(0)

    def EncodeBase64(self, words: str) -> str:
        """
        Encodes the clear text to Base64 encoded text.

        @words -- The clear text for encoding
        @return -- (str)
        """
        return base64.b64encode(words.encode('utf-8')).decode('utf-8')

    def EncodeUrl(self, words: str) -> str:
        """ 
        Encodes the clear text to URL encoded text.

        @words -- The clear text for encoding
        @return -- (str)
        """
        length = len(words)

        converted = ""
        for i in range(0, length):
            tmp = urllib.parse.quote(words[i], safe='')
            if(tmp[0] == '%'):
                converted += tmp
            else:
                converted += f"%{hex(ord(tmp))[2:]}"
        
        return converted

    def DecodeBase64(self, encoded_text: str) -> str:
        """
        Decodes the Base64 encoded text to clear text.
        
        @encoded_text -- The Base64 encoded text
        @return -- (str)
        """
        return base64.b64decode(encoded_text).decode('utf-8')

    def DecodeUrl(self, encoded_text: str) -> str:
        """
        Decodes the URL encoded text to clear text.
        
        @encoded_text -- The URL encoded text, with or without %
        @return -- (str)
        """
        decoded = ""
        i = 0
        length = len(encoded_text)
        while (i < length):
            if(encoded_text[i] == '%') and (i + 3 <= length):
                decoded += chr(int(encoded_text[i+1:i+3], 16))
                i += 3
                continue
            elif (encoded_text[i] == '%') and i + 2 < length:
                decoded += chr(int(encoded_text[i:], 16))
                i += 3
                continue
            else:
                decoded += encoded_text[i]
                i += 1
                continue
        return decoded
    
    def setupParser(self):
        """
        Sets up the parser for the command line arguments.
        """
        self.parser.add_argument("-f", "--format", dest="format", help="a supported encoding format. Default: url", default="url", choices=['url','base64'], type=str)
        self.parser.add_argument("-m", "--mode", dest="mode", help="encode or decode. Default: encode", default="encode", type=str)

main = EncodeIt();