# Aqui eu defino logging básico para toda a aplicação. Uso o logging da stdlib
# porque é simples e suficiente para demonstrar observabilidade.

import logging

from logging.handlers import RotatingFileHandler

LOG_FILE = '/tmp/brain_agriculture.log'

def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # File handler com rotação
    fh = RotatingFileHandler(LOG_FILE, maxBytes=10 * 1024 * 1024, backupCount=3)
    fh.setLevel(logging.INFO)

    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    ch.setFormatter(fmt)
    fh.setFormatter(fmt)

    logger.addHandler(ch)
    logger.addHandler(fh)

    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
