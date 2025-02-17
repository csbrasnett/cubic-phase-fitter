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
        params.add('rot_a', value=np.random.uniform(low=-np.pi, high=np.pi), min=-np.pi, max=np.pi)
        params.add('rot_b', value=np.random.uniform(low=-np.pi, high=np.pi), min=-np.pi, max=np.pi)
        params.add('rot_c', value=np.random.uniform(low=-np.pi, high=np.pi), min=-np.pi, max=np.pi)
        params.add('scale', value=dimensions[0])

        minner = Minimizer(fitfunc, params, fcn_args=(terminal_positions,))
        iter_result = minner.minimize()

        counter += 1
        if counter == 5:
            break

        # if the residual is too low we get a memory error later for some reason
        if (iter_result.residual.sum() > 1000) or (iter_result.residual.sum() < 20):
            continue
        else:
            result = iter_result
            fit_success = True

    if fit_success:
        p_out = {}
        p_out['trans_a'] = iter_result.params['trans_a']
        p_out['trans_b'] = iter_result.params['trans_b']
        p_out['trans_c'] = iter_result.params['trans_c']
        p_out['rot_a'] = iter_result.params['rot_a']
        p_out['rot_b'] = iter_result.params['rot_b']
        p_out['rot_c'] = iter_result.params['rot_c']
        p_out['scale'] = iter_result.params['scale']
        C_i_array = fitfunc(p_out, terminal_positions, alt_return=True)
        return result, C_i_array
    else:
        return None, None