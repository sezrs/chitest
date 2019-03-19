import argparse
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Chi-squared test')
parser.add_argument('--testnum', type=int, default=100000,
                    help='total number of tests')
parser.add_argument('--critvalueU', type=int, default=134.642,
                    help='total number of tests')
parser.add_argument('--critvalueE', type=int, default=57.342,
                    help='total number of tests')
args = parser.parse_args()


def sampleU(f=100, r=range(0, args.testnum)):
    observed = []
    observed_indx = {i: 0 for i in range(1, f+1)}

    for i in r:
        observed.append(random.randint(1, f))

    for i in observed:
        observed_indx[i]+=1

    return observed_indx

def sampleE(r=range(0, args.testnum)):
    observed = []
    x = 0
    observed_indx = {i: 0 for i in range(0, 37)}

    for i in r:
        x = 0
        for i in range(0, 4):
            x+=random.randint(0, 9)
        observed.append(x)    

    for i in observed:
        observed_indx[i]+=1

    return observed_indx
    

def graph(o):

    plt.bar(x=range(1, len(o)+1), height=list(o.values()), width=0.5)
    plt.plot(range(1, len(o)+1), list(o.values()), color="#ff0000ff")
    plt.show()
    return o;

def test(o, static_freq=True):

    if(static_freq):
        freq = args.testnum*(1/len(o))
        e = {i: freq for i in range(1, len(o)+1)}
    x = 0
    for i, y in enumerate(o.values()):
        x+=((y-e[i+1])**2)/e[i+1]
    
    return(x)

def pie_chart(s, critvalue):
    rejected = 0
    accepted = 0
    indx = {i: "" for i in range(1, 1001)}
    pbar = tqdm(range(0, 1000))
    for i in pbar:
        if(test(s())>critvalue):
            rejected+=1
            indx[i+1]="rejected"
        else:
            accepted+=1
            indx[i+1]="accepted"

    pie = [accepted, rejected]
    labels = "accepted", "rejected"
    exploded = [0.1, 0]
    plt.pie(pie, explode=exploded, labels=labels, autopct="%1.1f%%", shadow=True)
    plt.axis("equal")
    plt.show()
    return(indx)

x = sampleU()
print(x)
print(test(x))
graph(x)
print(pie_chart(sampleU, args.critvalueU))
