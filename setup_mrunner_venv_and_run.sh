#!/bin/sh
# run with
# bash mrunner_config.sh prometheus_username your_initials
export USERNAME=$1
export INITIALS=$2

git clone https://github.com/konradczechowski/mrunner_example

python3 -m venv mrunner_npt2
source mrunner_npt2/bin/activate
# install neptune
pip install -I neptune-cli==2.8.23
# Run experiment (with neptune) locally
neptune run some_src/experiment.py

# Install mrunner
pip install git+git://github.com/deepsense-ai/mrunner.git@bd1849cf

# Prepare config file, you can use default config in ~/.configs/mrunner/ instead.
sed -r "s/^(\s*)(slurm_url: <username>@pro.cyfronet.pl$)/\1slurm_url: $USERNAME@pro.cyfronet.pl/" mrunner_config_template.yaml > tmp_mrunner_config.yaml
sed -r "s/^(\s*)(user_id: <initials>$)/\1user_id: $INITIALS/" tmp_mrunner_config.yaml > mrunner_config.yaml
rm tmp_mrunner_config.yaml


# Run job on prometheus.
# You need to set slurm_url in mrunner_config.yaml (change username to yours).
mrunner --config mrunner_config.yaml --context plgrid_cpu run exp_specs/example_specs/2018_09_25__exp_name.py



