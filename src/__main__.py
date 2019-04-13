from expand import spread
from template_engine import webTemplate
import os


def main():
    newEx = spread()
    d = newEx.parseSettings()
    if d['path'] == '.':
        webTemp = webTemplate(os.getcwd())
        webTemp.remove_all()
if __name__ == "__main__":
    main()