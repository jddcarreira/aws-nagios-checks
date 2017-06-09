import datetime

class RDS(object):
    def __init__(self, cloudwatch_con, window=240, period=60):
        self.cloudwatch_con = cloudwatch_con
        self.window = window
        self.period = period

    def __get_rds_cluster_metric(self, cluster, role, metric):
        now_datetime = datetime.datetime.utcnow()
        metrics = self.cloudwatch_con.get_metric_statistics(
            Namespace='AWS/RDS',
            MetricName=metric,
            Dimensions=[
                {
                    'Name': 'DBClusterIdentifier',
                    'Value': cluster,
                },
                {
                    'Name': 'Role',
                    'Value': role
                }
            ],
            StartTime=now_datetime - datetime.timedelta(seconds=self.window),
            EndTime=now_datetime,
            Statistics=[
                'Average'
            ],
            Period=self.period,
        )
        metrics_dp = sorted(metrics['Datapoints'], key=lambda dp: dp['Timestamp'], reverse=True)
        return metrics_dp[0]

    def get_rds_cluster_cpu(self, cluster, role):
        return self.__get_rds_cluster_metric(cluster, role, "CPUUtilization")

    def get_rds_cluster_queries(self, cluster, role):
        return self.__get_rds_cluster_metric(cluster, role, "Queries")
