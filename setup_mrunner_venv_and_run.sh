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
# Login into neptune to generate tokens.
neptune account login

# Install mrunner
pip install git+git://github.com/deepsense-ai/mrunner.git@bd1849cf

# Prepare config file with mrunner context. You can also create contexts in global default config in ~/.configs/mrunner/ .
sed "s/<username>/$USERNAME/g" mrunner_config_template.yaml > tmp_mrunner_config.yaml
sed -i.bak "s/<initials>/$INITIALS/g" tmp_mrunner_config.yaml
mv tmp_mrunner_config.yaml mrunner_config.yaml
# For real experiments change cmd_type in mrunner_config.yaml from srun to sbatch. srun is usefull for remote debug runs.

# Run job on prometheus.
# You need to set slurm_url in mrunner_config.yaml (change username to yours).
cd run
mrunner --config mrunner_config.yaml --context plgrid_cpu run exp_specs/example_specs/2018_09_25__exp_name.py

# See your experiment in https://neptune.ml/
