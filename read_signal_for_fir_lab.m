% read binary file
f = fopen('x.dat','r') ;
x = fread( f, 'double') ;
fclose(f) ;
