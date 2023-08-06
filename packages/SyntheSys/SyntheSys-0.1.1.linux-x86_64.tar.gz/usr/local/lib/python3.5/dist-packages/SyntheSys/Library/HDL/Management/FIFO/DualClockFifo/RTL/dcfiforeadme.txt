//******************************************************************************
//                                                                             *
// Copyright (C) 2010 Regents of the University of California.                 *
//                                                                             *
// The information contained herein is the exclusive property of the VCL       *
// group but may be used and/or modified for non-comercial purposes if the     *
// author is acknowledged.  For all other uses, permission must be attained    *
// by the VLSI Computation Lab.                                                *
//                                                                             *
// This work has been developed by members of the VLSI Computation Lab         *
// (VCL) in the Department of Electrical and Computer Engineering at           *
// the University of California at Davis.  Contact: bbaas@ece.ucdavis.edu      *
//******************************************************************************

Dual Clock FIFO Readme

by: Aaron Stillmaker (astillmaker@ucdavis.edu)
VLSI Computation Lab, UC Davis
11/9/2010

Files:

FIFO.v
SRAM.v
tb.vt
tb.vf
Makefile


Description:

This dual clock FIFO is designed as a way for two circuits operating in
different clock frequencies to communicate with each other.  There is a read
side and write side where data is stored into the internal memory of the
FIFO using the write side clock and then read from the internal memory using
the read side clock.  This module is meant to be flexible, allowing to
easily change the data width and address width as well as the size of the
internal memory. 

This project was motivated by the need for a simple dual clock FIFO similar
to the dual clock FIFO designed by Ryan Apperson which is used inside of
the VCL group's AsAP2 chip.  To make this design Ryan's thesis was used as
a guide.  For completeness sake there is extra circuitry and signals
specifically meant to be used by the AsAP2 chip.  It was desirable to have a
single module that was straightforward and easy to change.

A testbench was created to test this circuit which will randomly choose a 
clock frequency for each clock after each clock pulse.  Each side will
randomly stop reading or writing accordingly for a random amount of clock
pulses.  The output is monitored and it will give an error if a non 
sequential output is given, which would mean an incorrect value was read.


Instructions:

Put all files in the same directory and to compile and run use the commands:
make compile
make run

As-is this will compile with NCVerilog and run indefinatly.  When this was made
the files were correctly compileing on NCVerilog and Verilogxl as well as
synthesizing correctly on Design Compiler.

To change how long the test runs, uncomment line 253 and set the if statement
equality of symcount to how many cycles you want run.

To change the width of the data, simply change the DATA_WIDTH_M1 value on all 
three .v files.

To change the width of the address, change ADDR_WIDTH_M1.  If you are making it
larger, you will need to modify the gray code conversion to add more bits.

SRAM.v was a seperate module to easily allow other meories to be substituted in.
One can also use this module and change the size as needed.

For more information, contact Aaron Stillmaker: astillmaker@ucdavis.edu.

