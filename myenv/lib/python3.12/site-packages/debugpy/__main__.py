# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

import sys

if __name__ == "__main__":

    # There are three ways to run debugpy:
    #
    # 1. Installed as a module in the current environment (python -m debugpy ...)
    # 2. Run as a script from source code (python <repo_root>/src/debugpy ...)
    # 3. Installed as a module in a random directory
    #
    # -----
    #
    # In the first case, no extra work is needed. Importing debugpy will work as expected.
    # Also, running 'debugpy' instead of 'python -m debugpy' will work because of the entry point
    # defined in setup.py.
    #
    # -----
    #
    # In the second case, sys.path[0] is the one added automatically by Python for the directory 
    # containing this file. 'import debugpy' will not work since we need the parent directory 
    # of debugpy/ to be in sys.path, rather than debugpy/ itself. So we need to modify sys.path[0].
    # Running 'debugpy' will not work because the entry point is not defined in this case.
    #
    # -----
    #
    # In the third case, running 'python -m debugpy' will not work because the module is not installed
    # in any environment. Running 'python <install_dir>/debugpy' will work, just like the second case. 
    # But running the entry point will not work because python doesn't know where to find the debugpy module.
    #
    # In this case, no changes to sys.path are required. You just have to do the following before calling
    # the entry point:
    #   1. Add <install_dir> to PYTHONPATH.
    #       On Windows, this is set PYTHONPATH=%PYTHONPATH%;<install_dir>
    #   2. Add <install_dir>/bin to PATH. (OPTIONAL)
    #       On Windows, this is set PATH=%PATH%;<install_dir>\bin
    #   3. Run the entry point from a command prompt
    #       On Windows, this is <install_dir>\bin\debugpy.exe, or just 'debugpy' if you did the previous step.
    #
    # -----
    #
    # If we modify sys.path, 'import debugpy' will work, but it will break other imports
    # because they will be resolved relative to debugpy/ - e.g. `import debugger` will try
    # to import debugpy/debugger.py.
    #
    # To fix both problems, we need to do the following steps:
    # 1. Modify sys.path[0] to point at the parent directory of debugpy/ instead of debugpy/ itself.
    # 2. Import debugpy.
    # 3. Remove sys.path[0] so that it doesn't affect future imports. 
    # 
    # For example, suppose the user did:
    #
    #   python /foo/bar/debugpy ...
    #
    # At the beginning of this script, sys.path[0] will contain "/foo/bar/debugpy".
    # We want to replace it with "/foo/bar', then 'import debugpy', then remove the replaced entry.
    # The imported debugpy module will remain in sys.modules, and thus all future imports of it 
    # or its submodules will resolve accordingly.
    if "debugpy" not in sys.modules:

        # Do not use dirname() to walk up - this can be a relative path, e.g. ".".
        sys.path[0] = sys.path[0] + "/../"
        import debugpy  # noqa
        del sys.path[0]

    from debugpy.server import cli

    cli.main()
