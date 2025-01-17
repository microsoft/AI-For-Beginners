#include <stdio.h>
#include <string.h>

#include "pyversion_compat.h"
#include "mutex.h"
#include "ipcmaxlen.h"
#include "zmq_compat.h"
#include <zmq.h>

typedef struct _zhint {
  void *sock;
  mutex_t *mutex;
  size_t id;
} zhint;

void free_python_msg(void *data, void *vhint) {
  zmq_msg_t msg;
  zhint *hint = (zhint *)vhint;
  int rc;
  if (hint != NULL) {
    zmq_msg_init_size(&msg, sizeof(size_t));
    memcpy(zmq_msg_data(&msg), &hint->id, sizeof(size_t));
    rc = mutex_lock(hint->mutex);
    if (rc != 0) {
      fprintf(stderr, "pyzmq-gc mutex lock failed rc=%d\n", rc);
    }
    rc = zmq_msg_send(&msg, hint->sock, 0);
    if (rc < 0) {
      /*
       * gc socket could have been closed, e.g. during process teardown.
       * If so, ignore the failure because there's nothing to do.
       */
      if (zmq_errno() != ENOTSOCK) {
        fprintf(stderr, "pyzmq-gc send failed: %s\n",
                zmq_strerror(zmq_errno()));
      }
    }
    rc = mutex_unlock(hint->mutex);
    if (rc != 0) {
      fprintf(stderr, "pyzmq-gc mutex unlock failed rc=%d\n", rc);
    }
    zmq_msg_close(&msg);
    free(hint);
  }
}

int zmq_wrap_msg_init_data(zmq_msg_t *msg, void *data, size_t size,
                           void *hint) {
  return zmq_msg_init_data(msg, data, size, free_python_msg, hint);
}
