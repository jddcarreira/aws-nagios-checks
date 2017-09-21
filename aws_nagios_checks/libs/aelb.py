import datetime
import sys

class AELB(object):
    def __init__(self, cloudwatch_con, window=240, period=60):
        self.cloudwatch_con = cloudwatch_con
        self.window = window
        self.period = period

    def get_app_elb_metric(self, loadbalancer, metric):
        now_datetime = datetime.datetime.utcnow()
        metrics = self.cloudwatch_con.get_metric_statistics(
            Namespace='AWS/ApplicationELB',
            MetricName=metric,
            Dimensions=[
                {
                    'Name': 'LoadBalancer',
                    'Value': loadbalancer,
                }
            ],
            StartTime=now_datetime - datetime.timedelta(seconds=self.window),
            EndTime=now_datetime,
            Statistics=[
                'Average'
            ],
            Period=self.period,
        )
        if metrics['Datapoints']:
            metrics_dp = sorted(metrics['Datapoints'], key=lambda dp: dp['Timestamp'], reverse=True)
            return metrics_dp[0]
        sys.exit(4)
