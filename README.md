## lambda-NAT-test
Lambda functions used to test Lambda setup, test VPC setup to get NAT IP address as well as to test connectivity to an address and port. 

I still find, even in 2019, that some organizations still use [IP Whitelisting](https://en.wikipedia.org/wiki/Whitelisting) for allowing access to their services. One of the challenges, when using dynamic environments in AWS is not having static IP addresses. This is becoming easier now, but in the early days of AWS, pre VPC and NAT, you would have to use an AWS Range of IP's for whitelisting. Today AWS provides a [JSON file](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) to simplify it. 

AWS Lambda now supports assigning your Lambda function to a VPC, with corresponding VPC subnets and Security Groups, [more info](https://docs.aws.amazon.com/lambda/latest/dg/vpc.html). If you VPC is setup, with private subnets, no external access, they will typically be setup with a NAT for any external routes. 

Typically I setup a 3 tiered approach.

1. External Network -- (for Load Balancers, ALB, NLB and ELB) This will use the VPC gateway for routing
2. Application Network -- for application services, ECS, etc. This will not have direct external access and will use a NAT for any external application calls.
3. Data Network -- for all databases, RDS, etc. This typically does not have NAT and should not need to make external calls.

</br>

### Lambda Functions
I created the following Lambda functions to test the VPC and NAT setup as well as testing connectivity to any external services that might use IP Whitelisting.


[lambda-NAT-test.py](lambda-NAT-test.py) -- Function calls [ifconfig.me](https://ifconfig.me) and returns the NAT IP used in the call. 

[lambda-port-test.py](lambda-port-test.py) -- Function tests the connectivity to an external service and port. In this function it makes a call to test.rebex.net:22 an external public SSH, SFTP server for testing connections. [More info](https://www.sftp.net/public-online-sftp-servers)

[lambda-NAT-Port-test.py](lambda-NAT-Port-test.py) -- This function runs both tests above in a single lambda function. 




 