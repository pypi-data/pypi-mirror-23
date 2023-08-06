# Copyright 2013 Mario Graff Guerrero

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import numpy as np
import json
import os


def tonparray(a):
    return np.array(a.full_array())


def BER(y, yh):
    u = np.unique(y)
    b = 0
    for cl in u:
        m = y == cl
        b += (~(y[m] == yh[m])).sum() / float(m.sum())
    return (b / float(u.shape[0])) * 100.


def RSE(x, y):
    return ((x - y)**2).sum() / ((x - x.mean())**2).sum()

params_fname = os.path.join(os.path.dirname(__file__), 'conf', 'parameter_values.json')
with open(params_fname, 'r') as fpt:
    PARAMS = json.loads(fpt.read())


class RandomParameterSearch(object):
    def __init__(self, params=PARAMS,
                 npoints=1468,
                 training_size=5000,
                 seed=0):
        self._training_size = training_size
        self.popsize_constraint(params)
        self._params = sorted(params.items())
        self._params.reverse()
        self._len = None
        self._npoints = npoints
        self._seed = seed
        self.fix_early_popsize()

    def popsize_constraint(self, params):
        try:
            params['popsize'] = [x for x in params['popsize'] if x <= self._training_size]
        except KeyError:
            pass

    def fix_early_popsize(self):
        try:
            popsize = [x for x in self._params if x[0] == 'popsize'][0]
            if len(popsize[1]) == 0:
                popsize[1].append(self._training_size)
        except IndexError:
            pass
        try:
            early = [x for x in self._params if x[0] == 'early_stopping_rounds'][0]
            early_min = min(early[1])
            if early_min > self._training_size:
                early[1].append(self._training_size)
        except IndexError:
            pass

    def __len__(self):
        if self._len is None:
            _ = np.product([len(x[1]) for x in self._params])
            self._len = _
        return self._len

    def __getitem__(self, key):
        res = {}
        lens = [len(x[1]) for x in self._params]
        for l, k_v in zip(lens, self._params):
            k, v = k_v
            key, residual = divmod(key, l)
            res[k] = v[residual]
        return res

    def constraints(self, k):
        try:
            if k['population_class'] == 'Generational' and\
               k['early_stopping_rounds'] < k['popsize']:
                return False
            if k['early_stopping_rounds'] > self._training_size:
                return False
        except KeyError:
            return True
        return True

    def __iter__(self):
        np.random.seed(self._seed)
        m = {}
        _len = len(self)
        npoints = self._npoints if _len > self._npoints else _len
        while npoints:
            k = np.random.randint(_len)
            if len(m) == _len:
                return
            while k in m:
                k = np.random.randint(_len)
            m[k] = 1
            p = self[k]
            if self.constraints(p):
                npoints -= 1
                yield p

    @staticmethod
    def process_params(a):
        from EvoDAG import EvoDAG
        fs_class = {}
        function_set = []
        for x in EvoDAG()._function_set:
            fs_class[x.__name__] = x
        args = {}
        for k, v in a.items():
            if k in fs_class:
                if not isinstance(v, bool):
                    fs_class[k].nargs = v
                if v:
                    function_set.append(fs_class[k])
            else:
                args[k] = v
            fs_evo = EvoDAG()._function_set
            fs_evo = filter(lambda x: x in function_set, fs_evo)
            args['function_set'] = [x for x in fs_evo]
        return args
