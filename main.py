import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('data/out.csv')


def first():

    plt.figsize=(12, 8)
    sns.set_style("darkgrid")
    sns.displot(x='length', kde=True, data=data)
    plt.savefig('first.png')
    plt.show()

# first()


def second():
    plt.figsize=(12, 8)
    sns.set_style("darkgrid")
    sns.displot(x='width', kde=True, data=data)
    plt.savefig('second.png')
    plt.show()

# second()


def third():
    plt.figsize=(12, 8)
    sns.set_style("darkgrid")
    sns.displot(x='length', hue='width', kde=True, data=data)
    plt.savefig('third.png')
    plt.show()

# third()


def fourth():
    plt.figsize=(12, 8)
    sns.set_style("darkgrid")
    sns.displot(x='length', hue='width', kind="kde", fill=True, data=data)
    plt.savefig('fourth.png')
    plt.show()

# fourth()


def fifth():
    plt.figsize=(12, 8)
    sns.set_style("darkgrid")
    sns.displot(x='length', y='width', bins=10, data=data)
    plt.savefig('fifth.png')
    plt.show()


# fifth()


def sixth():
    plt.figsize=(12, 8)
    sns.set_style("darkgrid")
    sns.jointplot(x='length', y='width', data=data)
    plt.savefig('sixth.png')
    plt.show()

# sixth()







