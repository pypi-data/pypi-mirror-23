"""
Author: Trieu Pham (trieu@codelynx.io)

A private property of #codelynx company
"""

from codelynx.api import Api
from asciinema.commands.command import Command


class Lookup(Command):
    """
    This class manages insert new document to lookup collection
    Expected command: xirion lookup
    Response: switch to insert mode
    @args: None
    @return:
        0 if everything 's good, 1 otherwise
    @raises:
        unknown
    """
    def __init__(self):
        # self.cmd = cmd
        # self.correction = correction
        self.api = Api()
        Command.__init__(self)  # color

    def execute(self):
        try:
            cmd = None
            while True:
                cmd = input('Command: ')
                # keep escape character
                cmd_decoded = bytes(cmd, 'utf-8').decode('unicode_escape')
                if cmd == 'exit':
                    self.print_info('Bye! exit insert lookup mode ~')
                    break
                correction = input('Correction: ')
                correction_decoded = bytes(correction, 'utf-8').decode('unicode_escape')
                # while True:
                #     correction = input('Correction: ')
                #     if correction == '\n\n'
                # Save these data to server
                # then make some noise ~ print response
                # kwargs = dict(orig=cmd, correct=correction)
                self.api.handle_data('lookup', quiet=False,
                                   orig=cmd_decoded, correct=correction_decoded)
        except Exception as ex:
            print(ex)  # For debug
            return 1  # exit code 1 ~ error
        return 0  # if code runs to this line, it means everything is ok => exit code 0
