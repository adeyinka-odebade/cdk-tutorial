from aws_cdk import (
    core as cdk,
    cloudformation_include as cfn_inc,
    aws_s3 as s3,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    aws_ec2 as ec2,
    aws_iam as iam
)

# Import Existing Cloudformation Stack
template = cfn_inc.CfnInclude(
    self, "Template",
    template_file="cdk_fun/cformation_s3.json",
    preserve_logical_ids=True
)

# Use within CDK and convert to a L2 construct
existing_bucket_l1 = template.get_resource("MyBucket-S3B4E9YC")
existing_bucket_l2 = s3.Bucket.from_bucket_name(
    self, "Bucket", existing_bucket_l1.ref
)

# Show it being used with a lambda!
        handler = lambda_.Function(self, "WidgetHandler",
                                   runtime=lambda_.Runtime.NODEJS_10_X,
                                   code=lambda_.Code.from_asset(
                                       "./cdk_fun/lambda"
                                   ),
                                   handler="widgets.main",
                                   environment=dict(
                                       BUCKET=existing_bucket_l2.bucket_name
                                   )
                                   )

        existing_bucket_l2.grant_read_write(handler)

        api = apigateway.RestApi(self, "widgets-api",
                                 rest_api_name="Widget Service",
                                 description="This service serves widgets.")

        get_widgets_integration = apigateway.LambdaIntegration(handler,
                                                               request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_widgets_integration)   # GET /