#include <Python.h>

int main(int argc, char* argv[])
{
    wchar_t* prog_name = (wchar_t*)"jm_object";

    Py_SetProgramName(prog_name);
    Py_Initialize();


    return 0;
}
