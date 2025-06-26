#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("problem_num", help="Problem number on Baekjoon", type=int)
args = parser.parse_args()

url = f"https://www.acmicpc.net/problem/{args.problem_num}"

session = requests.Session()
session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36"
    ),
    "Referer": "https://www.acmicpc.net/",
})
session.get("https://www.acmicpc.net/")

r = session.get(url)
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")
pres = soup.select("pre.sampledata")
if not pres:
    print("No sample data found")
    exit(1)

samples = []
for i in range(0, len(pres), 2):
    inp = pres[i].get_text().rstrip()
    outp = pres[i+1].get_text().rstrip() if i+1 < len(pres) else ""
    samples.append((inp, outp))

num_samples = len(samples)

input_file  = f"{args.problem_num}.in"
output_file = f"{args.problem_num}.out"

with open(input_file, "w", encoding="utf-8") as f_in, \
     open(output_file, "w", encoding="utf-8") as f_out:

    for idx, (inp, outp) in enumerate(samples):
        f_in.write(inp)
        f_out.write(outp)

        if idx < len(samples) - 1:
            f_in.write("\n\n")
            f_out.write("\n\n")

print(f"Successfully written {args.problem_num}.in and {args.problem_num}.out!")
