import argparse
import os
from deepsense import neptune

def get_configuration():
    if os.environ.get('PMILOS_DEBUG', '0') == '1':
        # local run, with offline neptune
        parser = argparse.ArgumentParser(description='Debug run.')
        parser.add_argument('--ex', type=str)
        # parser.add_argument("--spec", default='spec')
        parser.add_argument("--exp_dir_path", default='/tmp')
        commandline_args = parser.parse_args()
        if commandline_args.ex != None:
            vars = {}
            exec(open(commandline_args.ex).read(), vars)
            spec_func = vars['spec']
            # take first experiment (params configuration)
            experiment = spec_func()[0]
            params = experiment.parameters
        else:
            params = None
        # create offline context
        ctx = neptune.Context(offline_parameters=params)
        exp_dir_path = commandline_args.exp_dir_path
        return ctx, exp_dir_path
    else:
        # running under neptune
        ctx = neptune.Context()
        # I can't find storage path in Neptune2 context
        # exp_dir_path = ctx.storage_url
        exp_dir_path = os.getcwd()
        return ctx, exp_dir_path


