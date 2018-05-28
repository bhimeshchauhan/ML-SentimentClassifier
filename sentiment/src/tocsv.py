import csv
import pandas as pd

newf=""
with open('sentiment-neg.txt','r') as f:
    for line in f:
        newf+=line.strip()+"+-1\n"
    f.close()
with open('sentiment-neg.txt','w') as f:
    f.write(newf)
    f.close()


txt_file = r"sentiment-neg.txt"
csv_file = r"sentiment-neg.csv"
in_txt = csv.reader(open(txt_file, "r"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'w', newline=''))
out_csv.writerows(in_txt)


newf=""
with open('sentiment-pos.txt','r') as f:
    for line in f:
        newf+=line.strip()+"+1\n"
    f.close()
with open('sentiment-pos.txt','w') as f:
    f.write(newf)
    f.close()


txt_file = r"sentiment-pos.txt"
csv_file = r"sentiment-pos.csv"
in_txt = csv.reader(open(txt_file, "r"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'w', newline=''))
out_csv.writerows(in_txt)



df1 = pd.read_csv('sentiment-pos.csv', header=None, error_bad_lines=False)
df2 = pd.read_csv('sentiment-neg.csv', header=None, error_bad_lines=False)
