import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_dir.cdk_dir_stack import CdkDirStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_dir/cdk_dir_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkDirStack(app, "cdk-dir")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
