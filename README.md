# python-mpi
```
module load anaconda3/personal
conda create --name python-mpi -y
source activate python-mpi
module load mpi intel-suite
pip install mpi4py
source deactivate
qsub parallel.pbs.sh
```
