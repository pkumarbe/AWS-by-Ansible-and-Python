import boto3
def create_vpc_withsubnet():
    ec2 = boto3.resource('ec2')
    print "Creating VPC..."
    create_vpc = ec2.create_vpc(CidrBlock="192.168.0.0/16")
    create_vpc.create_tags(Tags=[{ "Key":"Name", "Value":"PvtNetwrok"}])
    create_vpc.wait_until_available()
    print  "VPC Created with ID..." + create_vpc.id
    print "Creating subnet and attach to the above VPC..."
    create_subnet= ec2.create_subnet(CidrBlock="192.168.1.0/24",VpcId=create_vpc.id)

    print "Creating Internet Gateway and attach to above VPC..."
    create_internet_gw = ec2.create_internet_gateway()
    create_internet_gw.attach_to_vpc(VpcId=create_vpc.id)

    print "Creating Router and add the gateway..."
    create_route_table= create_vpc.create_route_table()
    create_route = create_route_table.create_route(
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=create_internet_gw.id
    )
    

    return  create_vpc.id,create_subnet.id, create_internet_gw.id, create_route_table.id

print create_vpc_withsubnet()