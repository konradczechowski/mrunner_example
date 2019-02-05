#!/bin/sh
# run with
# bash mrunner_config.sh prometheus_username your_initials
set -e
export USERNAME=$1
export INITIALS=$2

python3 -m venv mrunner_npt2
source mrunner_npt2/bin/activate
# install neptune
pip install -I neptune-cli==2.8.23

# Install mrunner
pip install git+git://github.com/deepsense-ai/mrunner.git@bd1849cf

# Prepare config file with mrunner context. You can also create contexts in global default config in ~/.configs/mrunner/ .
sed -r "s/^(\s*)(slurm_url: <username>@pro.cyfronet.pl$)/\1slurm_url: $USERNAME@pro.cyfronet.pl/" mrunner_config_template.yaml > tmp_mrunner_config.yaml
sed -r "s/^(\s*)(user_id: <initials>$)/\1user_id: $INITIALS/" tmp_mrunner_config.yaml > mrunner_config.yaml
rm tmp_mrunner_config.yaml
# For real experiments change cmd_type in mrunner_config.yaml from srun to sbatch. srun is usefull for remote debug runs.

# Run job on prometheus.
# You need to set slurm_url in mrunner_config.yaml (change username to yours).
cd run
mrunner --config mrunner_config.yaml --context plgrid_cpu run exp_specs/example_specs/2018_09_25__exp_name.py
