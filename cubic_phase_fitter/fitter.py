from .fitfunc.fitfunc import fitfunc
from lmfit import Minimizer, Parameters
import numpy as np


def fitter(terminal_positions, dimensions, ncells):

    upper_threshold = {1: 1000,
                       2: 15000,
                       4: 1e6}

    fit_success = False
    counter = 0
    result = None
    while not fit_success:

        randmin = -0.5
        randmax = 0.5
        params = Parameters()
        params.add('trans_a', value=-terminal_positions[:, 0].mean())
        params.add('trans_b', value=-terminal_positions[:, 1].mean())
        params.add('trans_c', value=-terminal_positions[:, 2].mean())
        params.add('rot_a', value=np.random.uniform(low=randmin, high=randmax),
                   # min=-np.pi, max=np.pi,
                   min=randmin, max=randmax)
        params.add('rot_b', value=np.random.uniform(low=randmin, high=randmax),
                   # min=-np.pi, max=np.pi,
                   min=randmin, max=randmax)
        params.add('rot_c', value=np.random.uniform(low=randmin, high=randmax),
                   # min=-np.pi, max=np.pi,
                   min=randmin, max=randmax)
        params.add('scale', value=dimensions[0]/2)

        minner = Minimizer(fitfunc, params, fcn_args=(terminal_positions,))
        iter_result = minner.minimize()

        counter += 1
        if counter == 20:
            break
        print(counter, iter_result.residual.sum())
        # print(iter_result.params.valuesdict())
        # if the residual is too low we get a memory error later for some reason
        if (iter_result.residual.sum() > upper_threshold[ncells]) or (iter_result.residual.sum() < 20):
            continue
        else:
            result = iter_result
            fit_success = True

    return result
