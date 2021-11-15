# Experimental Setup

## Target Programs

Adobe Reader v19.021.20048
Foxit Reader v10.1.0.37527

## Computing Resources

Windows10 virtual machine

One core CPU with 4G memory

host-machine:8cores(Intel i7-6700@4.00GHz) and 32G memory

Virtualbox 6.1


# Experimental Data

## coverage 
### compare_using_different_arguments (Figure 5)
#### adobe reader (Figure 5(a))

we use the random type of all (documented+undocumented) APIs,type information of Adobe Document and type information of TypeOracle to fuzz Adobe and record coverage information using DynamoRio

#### foxit reader (Figure 5(b))

we use the random type of all (documented+undocumented) APIs,type information of Adobe Document, Adobe's type information of TypeOracle and Foxit's type information of TypeOracle to fuzz Foxit and record coverage information using DynamoRio

### compare_with_favocado (Figure 6)
#### adobe reader (Figure 6(a))

we use Favocado and Favocado with type information of TypeOracle to fuzz Adobe and  record coverage information using DynamoRio

#### foxit reader (Figure 6(b))

we use Favocado and Favocado with type information of TypeOracle to fuzz Foxit and  record coverage information using DynamoRio

## vulnerabilities (Table 3)
#### adobe reader

#### foxit reader

## coverage_24
### documented_random: randomly fuzzing documented APIs

we use the random type of document APIs to fuzz Adobe and record coverage information using DynamoRio

test/: test PDFs

db/: coverage information recoreded by DynamoRio

adobe_sample_input/: parse result of coverage information

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

res.txt: the final res number of instructions 



### all_random: randomly fuzzing all (documented+undocumented) APIs

we use the random type of all (documented+undocumented) APIs to fuzz Adobe and record coverage information using DynamoRio

test/: test PDFs

db/: coverage information recoreded by DynamoRio

adobe_sample_input/: parse result of coverage information

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

res.txt: the final res number of instructions 

### all_typeoracle: fuzzing all APIs using TypeOracle

we use the type information of all (documented+undocumented) APIs to fuzz Adobe and record coverage information using DynamoRio

test/: test PDFs

db/: coverage information recoreded by DynamoRio

adobe_sample_input/: parse result of coverage information

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

res.txt: the final res number of instructions 

## vulnerabilities_24
### documented_random: randomly fuzzing documented APIs

we use the random type of document APIs to fuzz Adobe

test/: test PDFs

crashinfo/: crashinfo logged by event viewer of windows

save/crash/: crash PDFs



### all_random: randomly fuzzing all (documented+undocumented) APIs

we use the random type of all (documented+undocumented) APIs to fuzz Adobe 

test/: test PDFs

crashinfo/: crashinfo logged by event viewer of windows

save/crash/: crash PDFs

### all_typeoracle: fuzzing all APIs using TypeOracle

we use the type information of all (documented+undocumented) APIs to fuzz Adobe 

test/: test PDFs

crashinfo/: crashinfo logged by event viewer of windows

save/crash/: crash PDFs

### all_favocado: fuzzing all APIs using Favocado

we use Favocado to fuzz Adobe 

test/: test PDFs

crashinfo/: crashinfo logged by event viewer of windows

save/crash/: crash PDFs

### all_typeoracle_favocado: fuzzing all APIs using combination of TypeOracle and Favocado

we use Favocado and type information of TypeOracle to fuzz Adobe 

test/: test PDFs

crashinfo/: crashinfo logged by event viewer of windows

save/crash/: crash PDFs


# Utility
## crashinfo

parse the crashinfo logged by event viewer of windows and get unique crash

## parse_cov

parse coverage file genarated by DynamoRio

## recored_cov

record coverage information using DynamoRio

## bbkn2insn

count number of instructions

# How to reproduce (using coverage_24/all_typeoracle as an example)



1. copy test PDFs from coverage_24/all_typeoracle/test to utility/record_cov/adobe/test

2. cd utility/record_cov/adobe

3. run the tool and record coverage info

```
python run.py
```

4. copy coverage file from utility/record_cov/adobe/db to utility/parse_covfile/sample_data
5. cd utility/record_cov
6.  run the tool and parse coverage information

```
python frame.py
```

6. copy coverage file from utility/parse_covfile/sample_output to utility/bbkn2insn/adobe_sample_input
7. cd utility/bbkn2insn

8. run the tool and count number of instruction

```
python batch.py
python combine.py
python res.py
```

