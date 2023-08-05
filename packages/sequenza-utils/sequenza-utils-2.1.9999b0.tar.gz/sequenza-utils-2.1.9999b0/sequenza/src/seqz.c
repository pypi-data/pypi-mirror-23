#include "common.h"
#include "merge.h"

#if PY_MAJOR_VERSION >= 3
  #define py2str(str) str;
#else
  #define py2str(str) PyString_AsString(str);
#endif

static char module_doc[] = "This is a simple, module wrapping a "
    "C pileup parser";
static char seqz_doc[] = "This function reads merged pileups and "
    "gc info to return a data to build a seqz line";

static PyObject *main_merge(PyObject *module, PyObject *args,
    PyObject *kwargs) {

    static char *kwlist[] = {
        "data",
        "depth_sum",
        "qlimit",
        "hom_t",
        "het_t",
        "het_f",
    };
    char data[4];


    int depth_sum;
    int qlimit;

    float hom_t, het_t, het_f;

    qlimit    = 53; /* Default value. */
    hom_t    = 0.85; /* Default value. */
    het_t    = 0.35; /* Default value. */
    het_f    = -0.1; /* Default value. */

    #if PY_MAJOR_VERSION >= 3
        if (! PyArg_ParseTupleAndKeywords(args, kwargs, "zii|fff", kwlist,
            &data, &depth_sum, &qlimit, &hom_t, &het_t, &het_f)) {
            goto except;
        }
    #else
        if (! PyArg_ParseTupleAndKeywords(args, kwargs, "Oii|fff", kwlist,
            &data, &depth_sum, &qlimit, &hom_t, &het_t, &het_f)) {
            goto except;
        }
    #endif

    merge_seqz(data, depth_sum, qlimit, hom_t, het_t, het_f);


    assert(! PyErr_Occurred());
    goto finally;
except:
    return 0;
finally:
    return 0;
}

static PyMethodDef module_methods[] = {
  {
      "do_seqz",
      (PyCFunction)main_merge,
      METH_VARARGS | METH_KEYWORDS,
      seqz_doc },
  {
      NULL, NULL, 0, NULL }
};


MOD_INIT(c_seqz)
{
    PyObject *m;

    MOD_DEF(m, "c_seqz", module_doc,
            module_methods)

    if (m == NULL)
        return MOD_ERROR_VAL;

    return MOD_SUCCESS_VAL(m);

}
