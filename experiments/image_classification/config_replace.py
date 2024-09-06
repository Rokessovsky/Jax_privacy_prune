import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("--dataset_main", default="cifar10")
parser.add_argument("--stop_training_at_epsilon", default=0.31, type=float)
parser.add_argument("--pruning_rate", default=0.42, type=float)
parser.add_argument("--pruning_method", default="synflow")
args = parser.parse_args()
dic = vars(args)

file_name = file_name = f"configs/{args.dataset_main}_wrn_28_10_eps1_finetune.py"
lines = open(file_name, 'r').readlines()
for key in dic.keys():
    for it, line in enumerate(lines):
        keyeq=str(key)+"="
        if keyeq in line:
            print(line)

            if isinstance(dic[key], str):
                line_split=line.split("=")
                line = line.replace(line_split[1], f"'{dic[key]}'\n")
            else:
                num = re.findall("\d+\.\d+", line)
                line = line.replace(num[0], str(dic[key]))
            # line_split[1] = str(dic[key])
            lines[it] = line
            print(line)
        

out = open(file_name, 'w')
out.writelines(lines)
out.close()
