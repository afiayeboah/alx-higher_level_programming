#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p) {
    long int byte_size;
    int i;
    char *byte_data = NULL;

    printf("[.] Python Bytes Object Info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &byte_data, &byte_size);

    printf("  Size: %li\n", byte_size);
    printf("  Data: %s\n", byte_data);

    if (byte_size < 10)
        printf("  First %li bytes:", byte_size + 1);
    else
        printf("  First 10 bytes:");

    for (i = 0; i <= byte_size && i < 10; i++)
        printf(" %02hhx", byte_data[i]);

    printf("\n");
}
