from .fitfunc.fitfunc import fitfunc
from lmfit import Minimizer, Parameters
import numpy as np


def fitter(terminal_positions, dimensions):

    fit_success = False
    counter = 0
    while fit_success == False:

        params = Parameters()
        params.add('trans_a', value=-terminal_positions[:, 0].mean())
        params.add('trans_b', value=-terminal_positions[:, 1].mean())
        params.add('trans_c', value=-terminal_positions[:, 2].mean())
        params.add('rot_a', value=np.random.uniform(low=-np.pi, high=np.pi, size=(100,)), min=-np.pi, max=np.pi)
        params.add('rot_b', value=np.random.uniform(low=-np.pi, high=np.pi, size=(100,)), min=-np.pi, max=np.pi)
        params.add('rot_c', value=np.random.uniform(low=-np.pi, high=np.pi, size=(100,)), min=-np.pi, max=np.pi)
        params.add('scale', value=dimensions[0])

        minner = Minimizer(fitfunc, params, fcn_args=(terminal_positions,))
        iter_result = minner.minimize()

        counter += 1
        # print(counter)
        if counter == 5:
            break

        # if the residual is too low we get a memory error later for some reason
        if (iter_result.residual.sum() > 1000) or (iter_result.residual.sum() < 20):
            # print('fit failed!')
            continue
        else:
            # print('success')
            result = iter_result
            fit_success = True
    # if counter == 5:
    #     continue

    if fit_success:
        return result
    else:
        return None