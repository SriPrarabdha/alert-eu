#!/bin/bash
#SBATCH --account EUHPC_E03_068
#SBATCH -p boost_usr_prod
#SBATCH --time 24:00:00     # format: HH:MM:SS
#SBATCH -N 1               # 3 node
#SBATCH --cpus-per-task=24  # 10 is default
#SBATCH --ntasks-per-node=1 # 4 tasks out of 32
#SBATCH --gpus-per-node=4
#SBATCH --gres=gpu:4          # 4 gpus per node out of 4
#SBATCH --wait-all-nodes=1
#SBATCH --mem=300000          # memory per node out of 494000MB (481GB)
#SBATCH --job-name="alert-eu"   
#SBATCH --output=/leonardo_work/EUHPC_E03_068/alert-eu/slurm_out/testing-%j-%t.out

export NCCL_IB_DISABLE=1 
export NCCL_P2P_DISABLE=1
export NCCL_BLOCKING_WAIT=1
export NCCL_ASYNC_ERROR_HANDLING=1
export CUDA_LAUNCH_BLOCKING=1

export NCCL_IB_TIMEOUT=100       
export NCCL_IB_RETRY_CNT=20      
export UCX_RC_TIMEOUT=10         

# Hub specific
export HF_HUB_DISABLE_TELEMETRY=1
export DO_NOT_TRACK=1
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1
source ~/miniconda3/bin/activate

TORCH_USE_CUDA_DSA=1
GPUS_PER_NODE=4
NNODES=$SLURM_NNODES
NUM_PROCESSES=$(expr $NNODES \* $GPUS_PER_NODE)

# so processes know who to talk to
MASTER_ADDR=$(scontrol show hostnames $SLURM_JOB_NODELIST | head -n 1)
MASTER_PORT=6000
module load cuda


cache_dir="/leonardo_work/EUHPC_E03_068/alert-eu/cache"
export HF_HOME=/leonardo_work/EUHPC_E03_068/.cache
export HF_DATASETS_CACHE=/leonardo_work/EUHPC_E03_068/.cache
export HF_MODELS_CACHE=/leonardo_work/EUHPC_E03_068/.cache
echo 'testing'

python /leonardo_work/EUHPC_E03_068/alert-eu/gen.py