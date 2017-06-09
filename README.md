## AWS Nagios Checks

Nagios checks based on AWS Cloudwatch metrics

### Installation
`pip install -r requirements.txt`

### Usage
```
AWS Nagios Check
Nagios checks based on AWS Cloudwatch metrics

Usage:
  aws-nagios-check.py [--aws-profile=<profile>] [--aws-region=<region>] --metric=<metric> --resource=<resource> --warn=<warn> --crit=<critical>

  --aws-profile=<profile>                           AWS Profile
  --metric=<metric>                                 Metric to be feteched
  --resource=<resource>                             Resource get the data
  --warn=<warn>                                     Warning threeshold
  --crit=<critical>                                 Critical threeshold

Options:
  -h --help                                         Show this screen.

Metrics:
    RDSClusterReadCPU/RDSClusterWriteCPU            Check RDS Cluster R/W CPU Usage
    RDSClusterReadQueries/RDSClusterWriteQueries    Check RDS Cluster Queries
```

### Example
#### Run a check
`python aws-nagios-check.py --aws-profile=default1 --aws-region=eu-west-1 --metric=RDSClusterReadCPU --resource=myclust --warn=90 --crit=95`
#### Check return code
`echo $?`