#!/usr/bin/python3.6
from expand import spread
from argument_parser import argumentParser
from template_engine import webTemplate , pythonTemplate
import os

# the entry point
def main():
        args = argumentParser().parseIt()
        spread().createSettings()
        settings = spread().parseSettings()
        z = pythonTemplate(settings)
        if args.action == 'start':
                z.createElements()
        elif args.action == 'delete':
                z.removeAll()
if __name__ == "__main__":
    main()