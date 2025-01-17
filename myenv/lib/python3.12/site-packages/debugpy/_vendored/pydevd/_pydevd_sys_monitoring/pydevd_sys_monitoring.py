from _pydevd_bundle.pydevd_constants import USE_CYTHON_FLAG, ENV_TRUE_LOWER_VALUES, ENV_FALSE_LOWER_VALUES, IS_PY312_OR_GREATER

if IS_PY312_OR_GREATER:
    if USE_CYTHON_FLAG in ENV_TRUE_LOWER_VALUES:
        from ._pydevd_sys_monitoring_cython import *

    elif USE_CYTHON_FLAG in ENV_FALSE_LOWER_VALUES:
        from ._pydevd_sys_monitoring import *

    else:
        try:
            from ._pydevd_sys_monitoring_cython import *
        except:
            from ._pydevd_sys_monitoring import *
else:
    from ._pydevd_sys_monitoring import *
