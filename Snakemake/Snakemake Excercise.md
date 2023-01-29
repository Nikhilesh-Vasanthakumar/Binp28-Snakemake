#Snakemake Version-7.20.0
#Nikhilesh Vasanthakumar
#
# Q1. Try running the above code. Do so by running snakemake in the
#   example_workflow directory. What error do you get? Once you fix the
#   first error, what does the second one mean?
#   Q1.A)
$ snakemake
#
#   Running in the terminal gives the following error:you need to specify the maximum number of CPU cores to be used at the same time. If you want to use N     #   cores, #say #--cores N or -cN. For all cores on your system (be sure that this is appropriate) use --cores all. For no parallelization use --cores 1 or #       -c1. <_io.#TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
#   To fix this error we can use the -c flag to specify the number of cpu cores to use at the same time.
#
$ snakemake -c1 #where 1 stands for 1 core.
#
#   The second error we get is 
#   Missing input files for rule first:
#    output: s1.1
#    affected files:
#        s1.0
#   This is caused by the missing s1.0 file in the working directory.
#
# Q2.Add the missing file by touching it. What happens if you run snakemake
#-n? Try re-running the workflow. What happens?
#
$ snakemake -n c1 
#
# The above code runs a dryrun which helps understand workflow and calculate the computational time
#The program in the end creates 2 files as output, s1.1 and s1.2
#
#Q3.Try running the workflow again. What happens? What happens if you
#remove or touch s1.1, and try re-running it?
# If we rerun the workflow it checks for outputfiles in the directory since they are present the it does not run the code and gives an output as:
# Nothing to be done (all requested files are present and up to date).removing s1.1 does not cause the code to run again as: rule all input is given as s1.2.
#
#
#Q4.Program
#
#Q5.Multiple files ending with .1 and .2 will be generated corresponding to the names of the .0 files.
#Expand when used in rule other than all will help reduce the number of steps required to complete the task thus saving time.

#Q6.
#-j is used as an alternative for cores for parellization of the jobs when run on a cluster/cloud.
#-p is used to print out the shell commands that will be executed.
#Q7.
#import-imports python libraries.Here pandas and Regular Expressions.
#read.csv is used to read the csv file,dtype is used to define the data type of the columns
#df.set_index is used to index the rows, the argument drop is set to false to not delete columns to be used as an index
#Multiext short for multiple-extension is used to define files which vary only by extensions.
#temp is used to produce temporary files that are deleted after execution.
#df.loc is used to acess .fastq rows
#Params under rules are used to define arbitary parameters for the shell commands.
#rules.aaa.output is an easier way of accesiing the output of a particular rule.

#Q8.
#Samtools Version 1.16
#bcftools version 1.16
#bowtie2 version 2.4.2

#9.
#The two files are exactly the same in content only the following titles vary.
#4,5c4,5
###bcftoolsCommand=mpileup -Ou -f Genes/yeastGenome.fa results/00_mapped_reads/sample.bam
###reference=file://Genes/yeastGenome.fa

###bcftoolsCommand=mpileup -Ob -f yeastGenome.fa readsAligned_sortedPositions.bam
###reference=file://yeastGenome.fa
#45,46c45,46
###bcftools_callCommand=call -m -v; Date=Sat Jan 28 18:27:48 2023
##CHROM        POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  results/00_mapped_reads/sample.bam
###bcftools_callCommand=call -m -v variants.bcf; Date=Wed Jan 25 13:54:59 2023
##CHROM        POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  readsAligned_sortedPositions.bam

#10
#The code ran succesfully when using a copy of the reads file.
$ snakemake -p --conda-frontend conda --use-conda -j2
#
#
#11
#fastp-version used 0.23.2
#fastqc version 0.11.9
#A new rule quality control was added to execute to the fastqc and fastp commands.
#The results are stored results/02_QC
#YAML file used
#
#channels:
#- conda-forge
#- bioconda
#dependencies:
#- fastqc=0.11.9
#- fastp=0.23.2
#
#13
#A new rule tsv_file was created to print out the required information.
#Library imported Io
