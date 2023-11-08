#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;
    PyListObject *list = (PyListObject *)p;
    const char *type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        type = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, type);
        if (!strcmp(type, "bytes"))
            print_python_bytes(list->ob_item[i]);
    }
}

