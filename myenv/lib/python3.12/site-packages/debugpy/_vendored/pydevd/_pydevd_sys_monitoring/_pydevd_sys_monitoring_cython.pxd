from cpython.mem cimport PyMem_Malloc, PyMem_Free

cdef extern from *:
    ctypedef void PyObject
    ctypedef struct PyCodeObject:
        int co_argcount;		# arguments, except *args */
        int co_kwonlyargcount;	# keyword only arguments */
        int co_nlocals;		    # local variables */
        int co_stacksize;		# entries needed for evaluation stack */
        int co_flags;		    # CO_..., see below */
        int co_firstlineno;     # first source line number */
        PyObject *co_code;		# instruction opcodes */
        PyObject *co_consts;	# list (constants used) */
        PyObject *co_names;		# list of strings (names used) */
        PyObject *co_varnames;	# tuple of strings (local variable names) */
        PyObject *co_freevars;	# tuple of strings (free variable names) */
        PyObject *co_cellvars;  # tuple of strings (cell variable names) */
        unsigned char *co_cell2arg; # Maps cell vars which are arguments. */
        PyObject *co_filename;	# unicode (where it was loaded from) */
        PyObject *co_name;		# unicode (name, for reference) */
        PyObject *co_lnotab;	# string (encoding addr<->lineno mapping) See
                                # Objects/lnotab_notes.txt for details. */
        void *co_zombieframe;   # for optimization only (see frameobject.c) */
        PyObject *co_weakreflist;   # to support weakrefs to code objects */
        void *co_extra;

cdef extern from "frameobject.h":
    ctypedef struct PyFrameObject:
        PyFrameObject *f_back
        PyCodeObject *f_code       # code segment
        PyObject *f_builtins       # builtin symbol table (PyDictObject)
        PyObject *f_globals        # global symbol table (PyDictObject) */
        PyObject *f_locals         # local symbol table (any mapping) */
        PyObject **f_valuestack   #
        PyObject **f_stacktop
        PyObject *f_trace         # Trace function */
        PyObject *f_exc_type
        PyObject *f_exc_value
        PyObject *f_exc_traceback
        PyObject *f_gen;

        int f_lasti;                #/* Last instruction if called */
        int f_lineno;               #/* Current line number */
        int f_iblock;               #/* index in f_blockstack */
        char f_executing;           #/* whether the frame is still executing */
        PyObject *f_localsplus[1];
