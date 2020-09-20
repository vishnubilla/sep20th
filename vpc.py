import boto3

client = boto3.client('ec2',
	region_name = 'us-east-2',
	aws_access_key_id = 'AKIAIF5GMINM7WTOQVWA',
	aws_secret_access_key = '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')
	
#Creating Vpc
myvpc = client.create_vpc(
	CidrBlock='10.0.0.0/16',
	InstanceTenancy='default',
	TagSpecifications=[{'ResourceType': 'vpc','Tags': [{'Key': 'Name','Value': 'Vishnu_vpc'}]}])
print(myvpc['Vpc']['VpcId'])

#Creating Subnet1
mysubnet1 = client.create_subnet(
	CidrBlock='10.0.1.0/24',
	VpcId=myvpc['Vpc']['VpcId'],
	TagSpecifications=[{'ResourceType': 'subnet','Tags': [{'Key': 'Name','Value': 'Subnet1'}]}])
print(mysubnet1['Subnet']['SubnetId'])

#Creating Subnet2
mysubnet2 = client.create_subnet(
	CidrBlock='10.0.2.0/24',
	VpcId=myvpc['Vpc']['VpcId'],
	TagSpecifications=[{'ResourceType': 'subnet','Tags': [{'Key': 'Name','Value': 'Subnet2'}]}])
print(mysubnet2['Subnet']['SubnetId'])

#Create Internet_Gateway
myIWG = client.create_internet_gateway(
	TagSpecifications=[{'ResourceType': 'internet-gateway','Tags': [{'Key': 'Name','Value': 'IWG'}]}])
print(myIWG['InternetGateway']['InternetGatewayId'])

#Attach_IGW
Attach_IGW = client.attach_internet_gateway(
	InternetGatewayId=myIWG['InternetGateway']['InternetGatewayId'],
    VpcId=myvpc['Vpc']['VpcId'])
	
#Create Route_Table
myroute = client.create_route_table(
	VpcId=myvpc['Vpc']['VpcId'],
	TagSpecifications=[{'ResourceType': 'route-table','Tags': [{'Key': 'Name','Value': 'Myroute'}]}])
print(myroute['RouteTable']['RouteTableId'])

#Associate RouteTable
Assroute = client.associate_route_table(
	RouteTableId=myroute['RouteTable']['RouteTableId'],
	SubnetId=mysubnet1['Subnet']['SubnetId'])

#Associate RouteTable
Routentry = client.create_route(
	DestinationCidrBlock='0.0.0.0/0',
	GatewayId=myIWG['InternetGateway']['InternetGatewayId'],
	RouteTableId=myroute['RouteTable']['RouteTableId'])
