from _pydev_bundle._pydev_saved_modules import threading

# Hack for https://www.brainwy.com/tracker/PyDev/363 (i.e.: calling is_alive() can throw AssertionError under some
# circumstances).
# It is required to debug threads started by start_new_thread in Python 3.4
_temp = threading.Thread()

if hasattr(_temp, "_handle") and hasattr(_temp, "_started"):  # Python 3.13 and later has this

    def is_thread_alive(t):
        return not t._handle.is_done()


elif hasattr(_temp, "_is_stopped"):  # Python 3.12 and earlier has this

    def is_thread_alive(t):
        return not t._is_stopped

elif hasattr(_temp, "_Thread__stopped"):  # Python 2.x has this

    def is_thread_alive(t):
        return not t._Thread__stopped

else:
    # Jython wraps a native java thread and thus only obeys the public API.
    def is_thread_alive(t):
        return t.is_alive()


del _temp
