#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
    long int size;
    int i;
    char *data = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(bytes_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(bytes_obj, &data, &size);

    printf("  size: %li\n", size);
    printf("  data: %s\n", data);
    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", data[i]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    long int size = PyList_Size(list_obj);
    int i;
    PyListObject *list = (PyListObject *)list_obj;
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
