import sys
import optparse

class MigrateInterface(object):
    """
    Main class doing the migration
    """
    def __init__(self):
        self.version = "1.0"
        self.parser = optparse.OptionParser()
        self.opts = None
        self.setup_parser()

    def setup_parser(self):
        """
        Setups options in parser
        and returns opts dict and args list
        """
        self.parser.usage = """ main [options] \n\nVersion: {version}""".format(version=self.version)



        self.parser.add_option("-p", "--paths",
                               default=None,
                               dest="paths",
                               help="Provide full path to input file with listed paths",
                               metavar="paths")

        self.parser.add_option("-c", "--csvfile",
                               dest="csvfile",
                               help="Provide full path to input csv file",
                               metavar="csvfile")

        opts, _ = self.parser.parse_args(sys.argv) # _ ignores the returned args
        self.opts = opts
