import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--col', type=int, required=True)
args = parser.parse_args()

wanted = args.col

pd.set_option('display.max_rows', None)
df = pd.read_excel('Mishawaka Vars.xlsm')
heat = df.iloc[:,[wanted-1]]
heat_temp = heat
heat_temp = heat_temp.dropna()
heat_temp.isnull()

print(heat_temp)