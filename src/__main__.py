from expand import spread
from argument_parser import argumentParser
from template_engine import webTemplate
import os

# the entry point
def main():
        args = argumentParser().parseIt()
        settings = spread().parseSettings()
        z = webTemplate(settings)
        if args.action == 'start':
                z.create_elements()
        elif args.action == 'delete':
                z.remove_all()
if __name__ == "__main__":
    main()