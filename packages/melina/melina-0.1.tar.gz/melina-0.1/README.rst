Melina can convert meta.xml to meta language (similar to protobuf) and back.

.. code-block::

    melina --meta-out DIR1 meta.xml  # to meta
    melina --xml-out DIR2 meta.meta  # back to xml

    melina --meta-stdout meta.xml > x.meta  # or to stdout

This is how melina language looks like:

.. code-block:: cpp

    /// pdmeta: "1.1", domain: "f", product: "b", release: "AX", version: "1.5", revision: "198"

    // line above is a header with meta module versions.
    // It needs to be the first symbol in file and start with '///'

    mo SCALAR
    {
        // you can define managed objects like structs in C++

        bool x;
        int y;
        string z;
    };

    mo COMPLEX
    {
        // enum/struct fields contain definition of enum/struct
        // enum/struct name should begin with small letter - after all it's a name of variable

        enum x
        {
            A = 1,
            B,
            C = 2
        };

        struct y
        {
            int z;
            struct v { int w; };
        };
    };

    mo CARDINALITY
    {
        // you can define cardinality of each managed object or struct field

        int x; // required by default
        optional int y; // optional integer, may be null
        repeated int z; // list of integers
        repeated(15) int z; // at most 15 'z' integers
    };

    mo DEFAULTS
    {
        // bool, int, string, enum can have default values

        bool x [default = true];
        int y [default = 12];
        string z [default = "foo bar"];
        enum v [default = 12] { A = 1, B = 12 };
    };

    mo RANGES
    {
        // int/string fields can specify allowed ranges
        // if int has a 3-param specifier, it's considered a "float"

        int(0..12) x;  // allowed integers from 0 to 12 inclusive
        int(-0.5, 0.5, 0.001) y;  // allowed floats from -0.5 to 0.5 inclusive with step 0.001
        string(0..10) z; // allowed string length from 0 to 10 chars inclusive
    };

    mo UNITS
    {
        // integers can have units (for documentational purposes)

        int y [units = "kbps"];
    };

    /**
     * Example managed object description.
     */
    mo COMMENTS
    {
        // you can use C++-style '//foo' or '/*foo*/' comments in meta files
        // doxygen-style comments '///foo' and '/**foo*/' are treated as mo/field description,
        // if present immediately above or rightwards of mo/field

        int x;  /// Example scalar field description
        int y;  /** Example scalar field description */

        /**
         * Example complex type description.
         */
        struct z
        {
        };

        /// Example complex type description.
        struct v
        {
        };
    };

    mo CHILDREN -> FIRST, SECOND, THIRD(10)
    {
        // managed object can have children defined
        // children can have max count specified in parens (at most 10 THIRD children)
    };

    mo(hc) FLAGS
    {
        // each managed object has: hidden('h'), create('c'), update('u'), delete('d') flags.
        // If not specified, hidden is assumed false, rest is assumed true.
        // Specification may be provided as 'hcud' letters in parens.
    };
