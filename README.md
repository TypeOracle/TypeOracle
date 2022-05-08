# Experimental Setup

## Target Programs

Adobe Reader v21.011.20039

Foxit Reader v11.2.1.53537

## Computing Resources

Windows 8.1 virtual machine

One core CPU with 4G memory

Host-machine: 8cores(Intel i7-6700@4.00GHz) and 32G memory

VMWare Workstation Pro 16

 
# Experimental Data

## coverage 

All files that generated in coverage recording process can be downloaded from 


### compare_using_different_arguments (Figure 8(a), Figure 9(a))
#### adobe reader (Figure 8(a))

We use the random type of documented binding calls, all (documented+undocumented) binding calls,type information of Adobe Manual and type information of TypeOracle to fuzz Adobe and record coverage information using DynamoRIO.

##### document: randomly fuzzing documented binding calls

We use the random type of document binding calls to fuzz Adobe and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parsed result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### random: randomly fuzzing all (documented+undocumented) binding calls

We use the random type of all (documented+undocumented) binding calls to fuzz Adobe and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### adobe_manual: fuzzing all binding calls using Adobe Manual

We use the Adobe Manual's type information of all (documented+undocumented) binding calls to fuzz Adobe and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### typeoracle: fuzzing all binding calls using TypeOracle

We use the TypeOracle's type information of all (documented+undocumented) binding calls to fuzz Adobe and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

#### foxit reader (Figure 9(a))

We use the type information of Adobe Document, random type of all (documented+undocumented) binding calls, Adobe's type information of TypeOracle and Foxit's type information of TypeOracle to fuzz Foxit and record coverage information using DynamoRIO

##### adobe_manual: fuzzing all binding calls using Adobe Manual

We use the Adobe Manual's type information of all (documented+undocumented) binding calls to fuzz Foxit and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/log-FoxitPDFReader_exe.txt: record the number of instructions of every dir in adobe_sample_input

##### random: randomly fuzzing all (documented+undocumented) binding calls

We use the random type of all(document+undocument) binding calls to fuzz Foxit and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/log-FoxitPDFReader_exe.txt: record the number of instructions of every dir in adobe_sample_input

##### typeoracle_adobe: fuzzing all binding calls using TypeOracle of Adobe

We use the Adobe's type information of all (documented+undocumented) binding calls to fuzz Foxit and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/log-FoxitPDFReader_exe.txt: record the number of instructions of every dir in sample_output

##### typeoracle_foxit: fuzzing all binding calls using TypeOracle of Foxit

We use the Foxit's type information of all (documented+undocumented) binding calls to fuzz Foxit and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/log-FoxitPDFReader_exe.txt/: record the number of instructions of every dir in sample_output

### compare_using_coverage_guidance (Figure 8(b), Figure 9(b))
#### adobe reader (Figure 8(b))

We use all (documented+undocumented) binding calls, all (documented+undocumented) binding calls with coverage guidance, type information of TypeOracle and type information of TypeOracle with coverage guidance to fuzz Adobe and record coverage information using DynamoRIO.

##### random: randomly fuzzing all (documented+undocumented) binding calls

We use the random type of all (documented+undocumented) binding calls to fuzz Adobe and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### coverage_random: randomly fuzzing all (documented+undocumented) binding calls with coverage guidance

We use the random type of all (documented+undocumented) binding calls to fuzz Adobe and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### typeoracle: fuzzing all binding calls using TypeOracle

We use the TypeOracle's type information of all (documented+undocumented) binding calls to fuzz Adobe and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### coverage_typeoracle: fuzzing all binding calls using TypeOracle with coverage guidance

We use the TypeOracle's type information of all (documented+undocumented) binding calls to fuzz Adobe and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

#### foxit reader (Figure 9(b))

We use all (documented+undocumented) binding calls, all (documented+undocumented) binding calls with coverage guidance, type information of TypeOracle and type information of TypeOracle with coverage guidance to fuzz Foxit and record coverage information using DynamoRIO.

##### random: randomly fuzzing all (documented+undocumented) binding calls

We use the random type of all (documented+undocumented) binding calls to fuzz Foxit and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### coverage_random: randomly fuzzing all (documented+undocumented) binding calls with coverage guidance

We use the random type of all (documented+undocumented) binding calls to fuzz Foxit and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### typeoracle_foxit: fuzzing all binding calls using TypeOracle

We use the TypeOracle's type information of all (documented+undocumented) binding calls to fuzz Foxit and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### coverage_typeoracle: fuzzing all binding calls using TypeOracle with coverage guidance

We use the TypeOracle's type information of all (documented+undocumented) binding calls to fuzz Foxit and record coverage information using DynamoRIO

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

### compare_with_favocado (Figure 8(c), Figure 9(c))
#### adobe reader (Figure 8(c))

we use Favocado and Favocado with type information of TypeOracle to fuzz Adobe and  record coverage information using DynamoRIO

##### favocado: fuzzing all binding calls using Favocado

we use Favocado to fuzz Adobe 

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### favocado_typeoracle: fuzzing all binding calls using combination of TypeOracle and Favocado

we use Favocado and type information of TypeOracle to fuzz Adobe 

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

#### foxit reader (Figure 9(c))

we use Favocado and Favocado with type information of TypeOracle to fuzz Foxit and  record coverage information using DynamoRIO

##### favocado: fuzzing all binding calls using Favocado

we use Favocado to fuzz Foxit

adobe_sample_input/: parse result of coverage information

adobe_sample_output/log-FoxitPDFReader_exe.txt: record the number of instructions of every dir in adobe_sample_input

##### favocado_typeoracle: fuzzing all binding calls using combination of TypeOracle and Favocado

we use Favocado and type information of TypeOracle to fuzz Foxit

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/log-FoxitPDFReader_exe.txt: record the number of instructions of every dir in adobe_sample_input

### compare_with_cooper (Figure 8(d), Figure 9(d))
#### adobe reader (Figure 8(d))

we use Cooper and Cooper with type information of TypeOracle to fuzz Adobe and  record coverage information using DynamoRIO

##### cooper: fuzzing all binding calls using Cooper

we use Cooper to fuzz Adobe 

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

##### cooper_typeoracle: fuzzing all binding calls using combination of TypeOracle and Cooper

we use Cooper and type information of TypeOracle to fuzz Adobe 

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/: instruction numbers of modules

adobe_sample_result.txt/: record the number of instructions of every dir in adobe_sample_input

#### foxit reader (Figure 9(d))

we use Cooper and Cooper with type information of TypeOracle to fuzz Foxit and  record coverage information using DynamoRIO

##### cooper: fuzzing all binding calls using Cooper

we use Cooper to fuzz Foxit

adobe_sample_input/: parse result of coverage information

adobe_sample_output/log-FoxitPDFReader_exe.txt: record the number of instructions of every dir in adobe_sample_input

##### cooper_typeoracle: fuzzing all binding calls using combination of TypeOracle and Cooper

we use Cooper and type information of TypeOracle to fuzz Foxit

db/: coverage information recoreded by DynamoRIO

adobe_sample_input/: parse result of coverage information

adobe_sample_output/log-FoxitPDFReader_exe.txt: record the number of instructions of every dir in adobe_sample_input

## vulnerabilities (Table 2)
#### adobe reader

#### foxit reader

## vulnerabilities_48

All test PDFs (including crash PDFs) can be downloaded from https://drive.google.com/file/d/1t5lKc69_leeg2iCfmkO-PsW4mt2c8L_j/view?usp=sharing

### adobe reader

#### document: randomly fuzzing documented binding calls

we use the random type of document binding calls to fuzz Adobe

crashinfo/: crashinfo logged by event viewer of windows


#### random: randomly fuzzing all (documented+undocumented) binding calls

we use the random type of all (documented+undocumented) binding calls to fuzz Adobe

crashinfo/: crashinfo logged by event viewer of windows


##### adobe_manual: fuzzing all binding calls using Adobe Manual

We use the Adobe Manual's type information of all (documented+undocumented) binding calls to fuzz Adobe

crashinfo/: crashinfo logged by event viewer of windows


#### typeoracle: fuzzing all binding calls using TypeOracle

we use the type information of all (documented+undocumented) binding calls to fuzz Adobe

crashinfo/: crashinfo logged by event viewer of windows


#### favocado: fuzzing all binding calls using Favocado

we use Favocado to fuzz Adobe 

crashinfo/: crashinfo logged by event viewer of windows


#### favocado+typeoracle: fuzzing all binding calls using combination of TypeOracle and Favocado

we use Favocado and type information of TypeOracle to fuzz Adobe 

crashinfo/: crashinfo logged by event viewer of windows

##### cooper: fuzzing all binding calls using Cooper

we use Cooper to fuzz Adobe

crashinfo/: crashinfo logged by event viewer of windows

##### cooper_typeoracle: fuzzing all binding calls using combination of TypeOracle and Cooper

we use Cooper and type information of TypeOracle to fuzz Adobe

crashinfo/: crashinfo logged by event viewer of windows

### foxit reader

##### adobe_manual: fuzzing all binding calls using Adobe Manual

We use the Adobe Manual's type information of all (documented+undocumented) binding calls to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows


#### radnom: randomly fuzzing all (documented+undocumented) binding calls

we use the random type of all (documented+undocumented) binding calls to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows


##### typeoracle_adobe: fuzzing all binding calls using TypeOracle of Adobe

We use the Adobe's type information of all (documented+undocumented) binding calls to fuzz Foxit

#### typeoracle_foxit: fuzzing all binding calls using TypeOracle of Foxit

We use the Foxit's type information of all (documented+undocumented) binding calls to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows


#### favocado: fuzzing all binding calls using Favocado

we use Favocado to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows


#### favocado+typeoracle: fuzzing all binding calls using combination of TypeOracle and Favocado

we use Favocado and type information of TypeOracle to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows

##### cooper: fuzzing all binding calls using Cooper

we use Cooper to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows

##### cooper_typeoracle: fuzzing all binding calls using combination of TypeOracle and Cooper

we use Cooper and type information of TypeOracle to fuzz Foxit

crashinfo/: crashinfo logged by event viewer of windows


# Utility

Can be downloaded from https://drive.google.com/file/d/1KeQNjcNm6109GV-4cam0TIdpldLyQMpR/view?usp=sharing

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
