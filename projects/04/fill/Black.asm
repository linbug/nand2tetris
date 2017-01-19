// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
@pos
M=0
@screenval
M=0
M=M-1
(LOOP)
@SCREEN
//now want: M[SCREEN+M[pos]] = M[screenval]
@SCREEN // A = SCREEN
D=A     // D = SCREEN
@pos    // A = pos
D=D+M // D = SCREEN+M[pos]
@screenpos // A = screenpos
M=D // M[screenpos] = SCREEN+M[pos]
@screenval // A = screenval
D=M // D = M[screenval]
@screenpos // A = screenpos
A=M // A = M[screenpos]
M=D // M[M[screenpos]] = D,
    // i.e., M[SCREEN+M[pos]] = M[screenval]
@pos // M[pos] += 1
M=M+1
@LOOP // goto LOOP
0;JMP
