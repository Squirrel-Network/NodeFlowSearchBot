#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__ = "Copyright 2021, SquirrelNetwork"
__credits__ = ["https://github.com/Squirrel-Network"]
__license__ = "GPL 3.0"
__version__ = "1.0.0"
__repository__ = "https://github.com/Squirrel-Network/NodeFlowSearchBot"
__status__ = "Stable"

### IMPORT ###
import logging
from config import Config
from commands import search, start, source
from telegram.ext import Updater, CommandHandler as CMH

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    updater = Updater(Config.TOKEN, use_context=True)

    dp = updater.dispatcher
    function = dp.add_handler
    function(CMH('start', start.init))
    function(CMH('search', search.init))
    function(CMH('source', source.init))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
