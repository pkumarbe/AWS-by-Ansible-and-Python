import boto3
def create_add_rule_secgroup():
    ec2= boto3.resource('ec2')
    print "Creating Security Group..."
    sec_group = ec2.create_security_group(
        GroupName = "custom sec",
        Description = "Allow http/s and SSH"
        )

    # Create the list rules to be allowed by this SG.
    ip_ranges = [{
        'CidrIp': '0.0.0.0/0'
    }]

    permission_lists = [{
        'IpProtocol':'TCP',
        'FromPort':80,
        'ToPort':80,
        'IpRanges':ip_ranges
    },{
        'IpProtocol':'TCP',
        'FromPort':22,
        'ToPort':22,
        'IpRanges':ip_ranges
    }]

    #Add the lists to SG

    sec_group.authorize_ingress(IpPermissions=permission_lists)
    return  sec_group.id

print create_add_rule_secgroup()