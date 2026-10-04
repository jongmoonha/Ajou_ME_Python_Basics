import argparse
import os
import pandas as pd
import yaml

parser = argparse.ArgumentParser()

# ① 사용할 모든 옵션을 정의하고, 기본값을 default=로 설정
parser.add_argument('--act',        type=str,   default='relu',        help='activation function')
parser.add_argument('--optim',      type=str,   default='adam',        help='optimizer')
parser.add_argument('--lr',         type=float, default=0.001,         help='learning rate')
parser.add_argument('--batch_size', type=int,   default=32,            help='batch size')
parser.add_argument('--exp_name',   type=str,   default='name',        help='exp name')
parser.add_argument('--config',     type=str,   default=None,          help='yaml file')

# ② 실행 명령 뒤에 적은 인자를 읽는다
args = parser.parse_args()

# --config 로 설정 파일을 주면 그 안의 값이 default 가 된다 → 인자를 다시 읽는다
if args.config is not None:
    with open(args.config, encoding='utf-8') as f:
        parser.set_defaults(**yaml.safe_load(f))
    args = parser.parse_args()

# ③ 값 확인
print("Training with the following parameters:")
print(f"Activation: {args.act}")
print(f"Optimizer: {args.optim}")
print(f"Learning Rate: {args.lr}")
print(f"Batch Size: {args.batch_size}")
print(f"Experiment Name: {args.exp_name}")

# ④ 결과 저장
os.makedirs('results', exist_ok=True)
filename_df = './results/{}.csv'.format(args.exp_name)
args_df = pd.DataFrame(vars(args), index=[0])
args_df.to_csv(filename_df)
