#PBS -l walltime=00:30:00,select=2:ncpus=12:mem=46gb
module load anaconda3/personal
module load mpi intel-suite
cd $PBS_O_WORKDIR
mpiexec python parallel.py
