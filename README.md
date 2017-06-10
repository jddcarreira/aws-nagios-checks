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

Metrics Prefix:
    - AELB_                                         ApplicationELB Metrics
    - RDSCluster_[Reader|Writer]                    RDS Cluster Metrics

Metric Example:
    [Metric Prefix]_[CW Metric Name]
    RDSCluster_ReaderCPUUtilization
```

### Available Metrics
#### Application ELB
- AELB_ActiveConnectionCount
- AELB_HTTPCode_Target_2XX_Count
- AELB_HTTPCode_Target_3XX_Count
- AELB_HTTPCode_Target_5XX_Count
- AELB_HTTPCode_ELB_2XX_Count
- AELB_HTTPCode_ELB_3XX_Count
- AELB_HTTPCode_ELB_5XX_Count
- AELB_TargetResponseTime
- AELB_RequestCount
- AELB_ClientTLSNegotiationError

#### RDS
- RDSCluster_[Writer|Reader]CommitLatency
- RDSCluster_[Writer|Reader]DatabaseConnections
- RDSCluster_[Writer|Reader]DDLThroughput
- RDSCluster_[Writer|Reader]NetworkReceiveThroughput
- RDSCluster_[Writer|Reader]BlockedTransactions
- RDSCluster_[Writer|Reader]SelectThroughput
- RDSCluster_[Writer|Reader]InsertLatency
- RDSCluster_[Writer|Reader]UpdateThroughput
- RDSCluster_[Writer|Reader]NetworkTransmitThroughput
- RDSCluster_[Writer|Reader]DeleteThroughput
- RDSCluster_[Writer|Reader]DMLLatency
- RDSCluster_[Writer|Reader]CommitThroughput
- RDSCluster_[Writer|Reader]DeleteLatency
- RDSCluster_[Writer|Reader]DMLThroughput
- RDSCluster_[Writer|Reader]LoginFailures
- RDSCluster_[Writer|Reader]SelectLatency
- RDSCluster_[Writer|Reader]ActiveTransactions
- RDSCluster_[Writer|Reader]BufferCacheHitRatio
- RDSCluster_[Writer|Reader]AuroraBinlogReplicaLag
- RDSCluster_[Writer|Reader]BinLogDiskUsage
- RDSCluster_[Writer|Reader]ResultSetCacheHitRatio

### Example
#### Run a check
`python aws-nagios-check.py --aws-profile=default1 --aws-region=eu-west-1 --metric=RDSClusterReadCPU --resource=myclust --warn=90 --crit=95`
#### Check return code
`echo $?`