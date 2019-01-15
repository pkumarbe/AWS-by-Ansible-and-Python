import  boto3
ec2 = boto3.resource('ec2')
def mktag(val):
    return [{'Key': 'Name', 'Value': val}]
def create_aws_instance(image,mincount, maxcount, Keyname,Instancetype,SG, instancename):
    rc = ec2.create_instances(
            ImageId = image,
            MinCount = mincount,
            MaxCount = maxcount,
            KeyName = Keyname,
            InstanceType = Instancetype,
            # security group shoud define by a list
            SecurityGroupIds = [SG],
            # VpcId = vpc,
            # BlockDeviceMappings = blockdevmap,
            # SubnetId = subnet,
            # PrivateIpAddress = instance['ipaddr']
            )
    # We can tag the instance with the same ID as follow..
    # iid = rc[0].id
    # # give the instance a tag name
    # ec2.create_tags(
    #     Resources=[iid],
    #     Tags=mktag(iid)
    # )

    # Else we can take tag as a parameter and tag as below...
    iid = rc[0].id
    ec2.create_tags(
        Resources=[iid],
        Tags=mktag(instancename)
    )


def list_all_instance():
    for i in ec2.instances.all():
        print str(i.id) + " " + i.state['Name']
create_aws_instance('ami-009d6802948d06e52',1,1,'learncloud','t2.micro','sg-055cfb0401dfded3c','testinstance')
list_all_instance()