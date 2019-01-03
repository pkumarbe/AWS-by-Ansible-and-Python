import boto3
ec2_keys = boto3.client('ec2')
list_key =  ec2_keys.describe_key_pairs()
print "List of keys before create" + str(list_key["KeyPairs"])
create_key = ec2_keys.create_key_pair(KeyName='My_Key')
list_key =  ec2_keys.describe_key_pairs()
print "List of keys after create" + str(list_key["KeyPairs"])
