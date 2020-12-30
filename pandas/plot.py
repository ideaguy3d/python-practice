import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas
import os

rcParams.update({'figure.autolayout': True, 'axes.titlepad': 20})

df = pandas.read_pickle(os.path.join('..', 'data', 'data_frame.pickle'))
small_df = df.iloc[49980:50019, :].copy()
path = '../data/'

acquisition_years = df.groupby('acquisitionYear').size()
acq_plot = acquisition_years.plot()

title_font = {
    'family': 'source sans pro',
    'color': 'darkblue',
    'weight': 'normal',
    'size': 20
}

labels_font = {
    'family': 'consolas',
    'color': 'darkred',
    'weight': 'normal',
    'size': 16
}

fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
acquisition_years.plot(ax=subplot, rot=45, logy=True, grid=True)
subplot.set_xlabel("Acquisition Year", fontdict=labels_font, labelpad=10)
subplot.set_ylabel("Artworks Acquired", fontdict=labels_font)
subplot.locator_params(nbins=40, axis='x')
subplot.set_title('Tate Gallery Acquisitions', fontdict=title_font)
fig.show()

fig.savefig('plot.png')
fig.savefig('plot.svg', format='svg')

debug = 1

# end of file
