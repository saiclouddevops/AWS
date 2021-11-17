Three nested files are added master.yaml , security-groups.yaml , vpc.yaml . Please place these three files in s3 and call from cloudformation 
and pass the bucket name in the cloudformation stack parameters.

By calling master.yaml 
https://bucketname.s3.amazonaws.com/master.yaml ,resources specified in vpc.yaml and security-groups.yaml will be created.

This master.yaml will create VPC components with two public subnets and two private subnets and Mysql RDS.

Once all components are created , Create resources from the url https://bucketname.s3.amazonaws.com/Loadbalancer.yml .Application load balancer,target groups and ec2 instances 
wil be created using the above cloudformation.



