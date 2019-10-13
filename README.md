# Clouseau
**A QC suite for large VCF files**

## Workflow

![mid_workflow](./plots/mid_workflow.png)

## Early Planning 
![User requirement](./plots/requirement.jpg)

![Main Workflow](./plots/workflow.png)


## Proposed implementation plan

The code is separated into two modules: Storage and Processing. This allows for easy swap out of Processing module with low level language for faster processing if needed. 

![Proposed implementation](./plots/implementation_plan.jpg)

``` 
clouseau.py -derp
```

## Output
Output is a file names “sample”
```
CHROM	SV1	SV2	SVn	start	end
ChrN  0 1 1 100
ChrN+1 1  1 1 78  
```

Log file for gaps
```
Sample_name	gap_start gap_end
Sample 1 	800	1000
```

