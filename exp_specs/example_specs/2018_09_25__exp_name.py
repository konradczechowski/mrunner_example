from mrunner.experiment import Experiment
import sys, os
sys.path.append(os.path.join(os.getcwd(), 'some_utils'))
from spec_utils import get_git_head_info
# It might be a good practice to not change specification files if run
# successfully, to keep convenient history of experiments. When you want to run
# the same experiment with different hyper-parameters, just copy it.
# Starting name with (approximate) date of run is also helpful.

def create_experiment_for_spec(parameters):
    script = 'some_src/experiment.py'
    name = 'experiment name'
    project_name = "my-project"
    python_path = '.:some_utils:some/other/utils/path'
    paths_to_dump = ''  # e.g. 'plgrid tensor2tensor', do we need it?
    tags = 'test_user other_tag'.split(' ')
    parameters['git_head'] = get_git_head_info()
    return Experiment(project=project_name, name=name, script=script,
                      parameters=parameters, python_path=python_path,
                      paths_to_dump=paths_to_dump, time='3-0', tags=tags)


# params are also good place for e.g. output path, or git hash
params_configurations = [dict(delta=0.5),
                         dict(delta=1.)]


def spec():
    experiments = [create_experiment_for_spec(params) for params in params_configurations]
    return experiments
