from math import sqrt

from consumers import TransposedConsumer


# statistics and stochastic process consumers


class _Statistics(object):
    """
    calculate basic statistics for a 1 dim empirical sample
    """

    def __init__(self, data):
        sps = sorted(data)
        p = [int(i * len(sps) * 0.01) for i in range(100)]
        self.count = len(sps)
        self.mean = sum(sps) / len(sps)
        self.variance = sum([rr ** 2 for rr in sps]) / (len(sps) - 1) - self.mean ** 2
        self.stdev = sqrt(self.variance)
        self.min = sps[0]
        self.max = sps[-1]
        self.median = sps[p[50]]
        self.box = [sps[0], sps[p[25]], sps[p[50]], sps[p[75]], sps[-1]]
        self.percentile = [sps[i] for i in p]
        self.sample = data

    def __str__(self):
        keys = ['count', 'mean', 'stdev', 'variance', 'min', 'median', 'max']
        values = ['%0.8f' % getattr(self, a, 0.0) for a in keys]
        mk = max(map(len, keys))
        mv = max(map(len, values))
        res = [a.ljust(mk) + ' : ' + v.rjust(mv) for a, v in zip(keys, values)]
        return '\n'.join(res)


class StatisticsConsumer(TransposedConsumer):
    """
    run basic statistics on storage consumer result per time slice
    """

    def __init__(self, func=None, statistics=None):
        if statistics is None:
            statistics = _Statistics
        self.statistics = statistics
        super(StatisticsConsumer, self).__init__(func)

    def finalize(self):
        """finalize for StatisticsConsumer"""
        super(StatisticsConsumer, self).finalize()
        # run statistics on timewave slice w at grid point g
        self.result = [(g, self.statistics(w)) for g, w in zip(self.grid, self.result)]


class StochasticProcessStatisticsConsumer(StatisticsConsumer):
    """
    run basic statistics on storage consumer result as a stochastic process
    """

    def finalize(self):
        """finalize for StochasticProcessStatisticsConsumer"""
        super(StochasticProcessStatisticsConsumer, self).finalize()

        class StochasticProcessStatistics(self.statistics):
            """local version to store statistics"""

            def __str__(self):
                s = [k.rjust(12) + str(getattr(self, k)) for k in dir(self) if not k.startswith('_')]
                return '\n'.join(s)

        sps = StochasticProcessStatistics([0, 0])
        keys = list()
        for k in dir(sps):
            if not k.startswith('_'):
                a = getattr(sps, k)
                if isinstance(a, (int, float, str)):
                    keys.append(k)
                else:
                    delattr(sps, k)
        for k in keys:
            setattr(sps, k, list())
        grid = list()
        for g, r in self.result:
            grid.append(g)
            for k in keys:
                a = getattr(sps, k)
                a.append(getattr(r, k))
        self.result = grid, sps


class TimeWaveConsumer(TransposedConsumer):

    def finalize(self):
        super(TimeWaveConsumer, self).finalize()

        max_v = max(max(w) for w in self.result)
        min_v = min(min(w) for w in self.result)
        min_l = min(len(w) for w in self.result)
        n = int(sqrt(min_l))  # number of y grid
        y_grid = [min_v + (max_v - min_v) * float(i) / float(n) for i in range(n)]
        y_grid.append(max_v + 1e-12)

        x, y, z = list(), list(), list()  # grid, value, count
        for point, wave in zip(self.grid, self.result):
            for l, u in zip(y_grid[:-1], y_grid[1:]):
                x.append(point)
                y.append(l + (u - l) * .5)
                z.append(float(len([w for w in wave if l <= w < u])) / float(min_l))
        self.result = x, y, z
