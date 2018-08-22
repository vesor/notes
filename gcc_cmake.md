## GCC default search path
I don't know why gcc search default path **prior** to specified path (-Ixxx, -Lxxx). 
So be careful if you installed some headers/libs in default path.

        `gcc -print-prog-name=cc1` -v
        ld --verbose | grep SEARCH

## view API in so file:

        #-C is also useful for demangling C++
        objdump -TC libz.so 
        
        
