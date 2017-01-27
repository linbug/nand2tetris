load stof.hdl,
output-file stof.out,
compare-to stof.cmp,
output-list a%B1.16.1 out%B1.15.1;

set a %B1110000000000001,
eval,
output;

set a %B0000000000000001,
eval,
output;
