import boto3
ec2 = boto3.resource('ec2')
#make sure the keyname exist
#conn = boto.ec2.connect_to_region("us-west-2") will also work
createInstance = ec2.create_instances(
       ImageId='ami-009d6802948d06e52',
       MinCount=2,
       MaxCount=2,
       InstanceType='t2.micro',
       KeyName='learncloud'
        )

