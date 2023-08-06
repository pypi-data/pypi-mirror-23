# simulateSV
Simulate structural variations and SNPs for artificial DNA templates.

## Installation

## Usage

* If you are simulating a small DNA template (< 500), make sure that SV option
sizes are less than the total size of your genomes, otherwise you may run into
unknown issues.

* Mutation rates for SVs and SNPs are approximate. The probabilities are 
applied sequentially to determine if a mutation occurs at a certain location,
and does not correct for conditional probabilities. However, since the mutation
rates are very small, the difference is very slight.

* This code has been optimized for readability instead of speed so that you may 
alter the code to however suits your need.
