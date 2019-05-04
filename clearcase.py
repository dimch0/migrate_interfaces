import os
import re
import subprocess

#              FUNCTIONS              #

def execute_cmd(cmd, view_name=False):
    """
    Executes a command in the given view.
    :param cmd: command which should be executed
    :param view_name: name of the view
    :return: a dict with the output and exit code
    {'output'   : "Some output string",
    'exit_code' : 0}
    """
    result = {}

    if view_name:
        full_cmd = 'ccset_view -e "{0}" {1}'.format(cmd, view_name)
    else:
        full_cmd = cmd

    try:
        proc = subprocess.Popen(full_cmd,
                                shell=True,
                                stdout=subprocess.PIPE)

        output = proc.communicate()[0]
        proc.poll()
        result['output'] = output
        result['exit_code'] = proc.returncode
    except Exception as exc:
        result['output'] = exc
        if result['exit_code'] != 141:  # SIGPIPE
            print "Return %s; Output:\n" % (result['exit_code']), result['output']

    if result['exit_code'] not in [0, 141]:
        print "Command execution failed with exit code: %s \n" % result['exit_code']

    return result