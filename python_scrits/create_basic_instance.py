import boto3
ec2 = boto3.resource('ec2')
#make sure the keyname exist
createInstance = ec2.create_instances(
       ImageId='ami-009d6802948d06e52',
       MinCount=1,
       MaxCount=1,
       InstanceType='t2.micro',
       KeyName='my_keypair'
        )

