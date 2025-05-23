#!/usr/bin/perl
use strict;
use warnings;
use Time::Piece;

# Arrays of machines and VLSI flow actions
my @machines = ("A", "B", "C");
my @actions = (
    "Floorplanning started", 
    "Floorplanning completed", 
    "Placement started", 
    "Placement completed", 
    "Clock Tree Synthesis started", 
    "Clock Tree Synthesis completed", 
    "Routing started", 
    "Routing completed", 
    "Timing analysis started", 
    "Timing analysis completed - 0 violations",
    "Timing analysis completed - 2 violations",
    "DRC check started",
    "DRC check completed - 5 errors",
    "DRC check completed - Clean"
);

# Select random machine and action
my $machine = $machines[int(rand(scalar(@machines)))];
my $action = $actions[int(rand(scalar(@actions)))];

# Generate timestamp
my $timestamp = localtime()->strftime('%Y-%m-%d %H:%M:%S');

# Format and print the log entry
print "$timestamp - Machine $machine: $action\n"; 