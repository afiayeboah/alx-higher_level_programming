#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Function that prints some basic
 * info about a Python list
 * @p: Python list object
 */
void print_python_list_info(PyObject *p)
{
	int Py_ssize_t size, allocated, elem;
    PyObject *item;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (elem = 0; elem < size; elem++)
    {
        item = PyList_GetItem(p, elem);
        printf("Element %ld: %s\n", elem, Py_TYPE(item)->tp_name);
    }
}
