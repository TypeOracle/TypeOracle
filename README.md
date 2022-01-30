# Experimental Setup

## Target Programs

Adobe Reader v21.011.20039

Foxit Reader v11.1.0.52543

## Computing Resources

Windows10 virtual machine

One core CPU with 4G memory

host-machine:8cores(Intel i7-6700@4.00GHz) and 32G memory

Virtualbox 6.1


# Experimental Data

## coverage 
### compare_using_different_arguments (Figure 6)
#### adobe reader (Figure 6(a))

we use the random type of all (documented+undocumented) APIs,type information of Adobe Document and type information of TypeOracle to fuzz Adobe and record coverage information using DynamoRIO

##### document: randomly fuzzing documented APIs

we use the random type of document APIs to fuzz Adobe and record coverage information using DynamoRIO

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

all_document.txt/: record the number of instructions of every dir in adobe_sample_input

##### all_random: randomly fuzzing all (documented+undocumented) APIs

we use the random type of all (documented+undocumented) APIs to fuzz Adobe and record coverage information using DynamoRIO

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

random.txt/: record the number of instructions of every dir in adobe_sample_input

##### typeoracle: fuzzing all APIs using TypeOracle

we use the type information of all (documented+undocumented) APIs to fuzz Adobe and record coverage information using DynamoRIO

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

typeoracle.txt/: record the number of instructions of every dir in adobe_sample_input

#### foxit reader (Figure 6(b))

we use the type information of Adobe Document, random type of all (documented+undocumented) APIs and Foxit's type information of TypeOracle to fuzz Foxit and record coverage information using DynamoRIO

##### document: randomly fuzzing documented APIs

we use the random type of document APIs to fuzz Foxit and record coverage information using DynamoRIO

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

sample_output/: parse result of coverage information

document.txt/: record the number of instructions of every dir in sample_output

##### all_random: randomly fuzzing all (documented+undocumented) APIs

we use the random type of all (documented+undocumented) APIs to fuzz Foxit and record coverage information using DynamoRIO

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

sample_output/: parse result of coverage information

random.txt/: record the number of instructions of every dir in sample_output

##### typeoracle: fuzzing all APIs using TypeOracle

we use the type information of all (documented+undocumented) APIs to fuzz Foxit and record coverage information using DynamoRIO

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

sample_output/: parse result of coverage information

typeoracle.txt/: record the number of instructions of every dir in sample_output

### compare_with_favocado (Figure 7)
#### adobe reader (Figure 7(a))

we use Favocado and Favocado with type information of TypeOracle to fuzz Adobe and  record coverage information using DynamoRIO

##### favocado: fuzzing all APIs using Favocado

we use Favocado to fuzz Adobe 

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

favocado.txt/: record the number of instructions of every dir in adobe_sample_input

##### favocado+typeoracle: fuzzing all APIs using combination of TypeOracle and Favocado

we use Favocado and type information of TypeOracle to fuzz Adobe 

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

favocado_oracle.txt/: record the number of instructions of every dir in adobe_sample_input

#### foxit reader (Figure 7(b))

we use Favocado and Favocado with type information of TypeOracle to fuzz Foxit and  record coverage information using DynamoRIO

##### favocado: fuzzing all APIs using Favocado

we use Favocado to fuzz Foxit

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

sample_output/: parse result of coverage information

favocado.txt/: record the number of instructions of every dir in adobe_sample_input

##### favocado+typeoracle: fuzzing all APIs using combination of TypeOracle and Favocado

we use Favocado and type information of TypeOracle to fuzz Foxit

test_case/: test PDFs

db/: coverage information recoreded by DynamoRIO

sample_output/: parse result of coverage information

favocado_oracle.txt/: record the number of instructions of every dir in adobe_sample_input

## vulnerabilities (Table 3)
#### adobe reader

#### foxit reader

## vulnerabilities_48

All test PDFs can be downloaded from 

### adobe reader

#### document: randomly fuzzing documented APIs

we use the random type of document APIs to fuzz Adobe

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs

#### all_random: randomly fuzzing all (documented+undocumented) APIs

we use Favocado and type information of TypeOracle to fuzz Adobe 

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs

#### typeoracle: fuzzing all APIs using TypeOracle

we use the type information of all (documented+undocumented) APIs to fuzz Adobe

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs

#### favocado: fuzzing all APIs using Favocado

we use Favocado to fuzz Adobe 

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs

#### favocado+typeoracle: fuzzing all APIs using combination of TypeOracle and Favocado

we use Favocado and type information of TypeOracle to fuzz Adobe 

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs

### foxit reader

#### document: randomly fuzzing documented APIs

we use the random type of document APIs to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs

#### all_random: randomly fuzzing all (documented+undocumented) APIs

we use Favocado and type information of TypeOracle to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs

#### typeoracle: fuzzing all APIs using TypeOracle

we use the type information of all (documented+undocumented) APIs to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs

#### favocado: fuzzing all APIs using Favocado

we use Favocado to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs

#### favocado+typeoracle: fuzzing all APIs using combination of TypeOracle and Favocado

we use Favocado and type information of TypeOracle to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows

crash/: crash PDFs


# Utility

Can be downloaded from 

## crashinfo

parse the crashinfo logged by event viewer of windows and get unique crash

## parse_cov

parse coverage file genarated by DynamoRIO

## recored_cov

record coverage information using DynamoRIO

## bbkn2insn

count number of instructions

# How to reproduce (using coverage/compare_using_different_arguments/adobe reader/typeoracle as an example)



1. copy test PDFs from coverage/compare_using_different_arguments/adobe reader/typeoracle//test_case to utility/record_cov/adobe/test

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

