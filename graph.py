"""
Creates a test depth size (kb) vs latency (ns) graph from the data in the txt files

The format of the text is the following:

$test_size_1,$latency_1 $test_size_2,$latency_2 ... $test_size_n,$latency_n

"""
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

def readable_size(size_in_kilobytes: int) -> str:
    # formats the size in kilobytes to a readable string
    if size_in_kilobytes < 1024:
        return f"{size_in_kilobytes}K"
    elif size_in_kilobytes < 1024**2:
        return f"{size_in_kilobytes / 1024:.0f}M"
        
with open("idle.txt", "r") as f:
    data = f.read().split(" ")
    data = [x.split(",") for x in data]
    data = [[int(x[0]), float(x[1])] for x in data ]
    print(data)

# graph
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_yscale('log')
ax.set_xlabel("Size")
ax.set_ylabel("Latency (ns)")
ax.set_title("Latency idle")
ax.set_ylim(0, 300)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))
ax.plot([readable_size(x[0]) for x in data], [x[1] for x in data])
plt.show()