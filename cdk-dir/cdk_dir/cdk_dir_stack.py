from aws_cdk import (
    # Duration,
    Stack,
    aws_sqs as sqs,
    aws_ec2 as ec2,
)
from constructs import Construct


class CdkDirStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # Create a VPC
        vpc = ec2.Vpc(self, "MyVpc", max_azs=3)

        # Create an EC2 instance
        ec2.Instance(self, 
                     "MyInstance",
                     instance_type=ec2.InstanceType("t2.micro"),
                     machine_image=ec2.AmazonLinuxImage(),
                     vpc=vpc)

        # example resource
        queue = sqs.Queue(
            self, "CdkDirQueue",
            visibility_timeout=sqs.Duration.seconds(300),
        )
