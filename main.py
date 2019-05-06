import sys
import csv
import optparse


class MigrateInterface():
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

    def load_data(self, fpath):
        """
        Loads data from file
        """
        with open(fpath, 'rb') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            header = next(data)

            for row in data:
                if not row == header:
                    if len([field for field in row if field not in [None, '']]) > 1:
                        try:
                            pass
                            # TODO: create objects
                        except Exception as e:
                            print 'ERROR - Could not set do stuff with row {0}: {1}'.format(row, e)

    def main(self):
        """
        check and run stages
        :return:
        """
        import pdb; pdb.set_trace()
        # TODO: parse files
        # TODO: loop over csv and create FunctionItems and EnumItems
        # TODO: loop over files and do migration
        # TODO: Generate delta file
        # TODO: run ccrscope



if __name__ == '__main__':
    migration = MigrateInterface()
    migration.main()
