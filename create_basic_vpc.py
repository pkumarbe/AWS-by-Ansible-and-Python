
import boto3
ec2 = boto3.resource('ec2')

#create VPC
create_vpc = ec2.create_vpc(CidrBlock='192.168.0.0/16')
#Add a tag, EX- Name
create_vpc.create_tags(Tags=[{ "Key":"Name", "Value":"PvtNetwrok"}])
# Wait until the task finished
create_vpc.wait_until_available()
# Print the vpc ID
print create_vpc.id
