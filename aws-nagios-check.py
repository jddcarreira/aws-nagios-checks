"""
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
"""

import sys
import boto3

from libs.nagios_validations import NagiosValidations
from libs.rds import RDS
from docopt import docopt

def cloudwatch_connection(profile, region):
    if profile:
        session = boto3.Session(profile_name=profile)
    con = session.client('cloudwatch', region_name=region)
    return con

def main(aws_profile, aws_region, metric, resource, wrn, crt):
    if metric == "RDSClusterReadCPU" or metric == "RDSClusterWriteCPU":
        role = "READER" if metric == "RDSClusterReadCPU" else "WRITER"
        cw_con = cloudwatch_connection(aws_profile, aws_region)
        cpu_status = RDS(cw_con).get_rds_cluster_cpu(resource, role)
        if cpu_status:
            check_code = NagiosValidations.high_is_bad(val=cpu_status['Average'], wrn=wrn, crt=crt)
        else:
            check_code(3)
        sys.exit(check_code)

    elif metric == "RDSClusterReadQueries" or metric == "RDSClusterWriteQueries":
        role = "READER" if metric == "RDSClusterReadQueries" else "WRITER"
        cw_con = cloudwatch_connection(aws_profile, aws_region)
        n_queries = RDS(cw_con).get_rds_cluster_queries(resource, role)
        if n_queries:
            check_code = NagiosValidations.high_is_bad(val=n_queries['Average'], wrn=wrn, crt=crt)
        else:
            check_code(3)
        sys.exit(check_code)

    else:
        sys.exit(100)

if __name__ == "__main__":
    args = docopt(__doc__)

    aws_profile = args['--aws-profile']
    aws_region = args['--aws-region']
    metric = args['--metric']
    resource = args['--resource']
    warn = float(args['--warn'])
    critical = float(args['--crit'])

    main(aws_profile, aws_region, metric, resource, warn, critical)
