import boto3
ec2 = boto3.resource('ec2')
for i in ec2.instances.all():
    if i.state['Name'] == 'running':
        print str(i.id) + " is in running state, terminating it...."
        i.terminate()

# ec2client = ec2.meta.client
# vpcslist = ec2client.describe_vpcs()
# vpcid =  vpcslist['Vpcs'][0]['VpcId']
# ec2.delete_vpc(vpcid)