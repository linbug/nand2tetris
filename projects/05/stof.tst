load stof.hdl,
output-file stof.out,
compare-to stof.cmp,
output-list in%B1.16.1 out%B1.15.1;

set in %B1110000000000001,
eval,
output;

set in %B0000000000000001,
eval,
output;
