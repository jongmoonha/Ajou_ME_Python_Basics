import argparse
import os
import pandas as pd
import yaml

parser = argparse.ArgumentParser()

# ① Define every option and set its default with default=
parser.add_argument('--act',        type=str,   default='relu',        help='activation function')
parser.add_argument('--optim',      type=str,   default='adam',        help='optimizer')
parser.add_argument('--lr',         type=float, default=0.001,         help='learning rate')
parser.add_argument('--batch_size', type=int,   default=32,            help='batch size')
parser.add_argument('--exp_name',   type=str,   default='name',        help='exp name')
parser.add_argument('--config',     type=str,   default=None,          help='yaml file')

# ② Read the arguments written after the run command
args = parser.parse_args()

# If a config file is given with --config, its values become the defaults → read the arguments again
if args.config is not None:
    with open(args.config, encoding='utf-8') as f:
        parser.set_defaults(**yaml.safe_load(f))
    args = parser.parse_args()

# ③ Check the values
print("Training with the following parameters:")
print(f"Activation: {args.act}")
print(f"Optimizer: {args.optim}")
print(f"Learning Rate: {args.lr}")
print(f"Batch Size: {args.batch_size}")
print(f"Experiment Name: {args.exp_name}")

# ④ Save the result
os.makedirs('results', exist_ok=True)
filename_df = './results/{}.csv'.format(args.exp_name)
args_df = pd.DataFrame(vars(args), index=[0])
args_df.to_csv(filename_df)
