# Connect via ssh

    chmod 400 xxx.pem
    ssh -i xxx.pem ubuntu@xxx.xxx.xxx.xx

# Attach vol
(First time Only): format vol: 

    sudo mkfs -t ext4 /dev/xvdf

Mount vol

    sudo mount /dev/xvdf /mnt/vol


# Ref link
instance pricing: https://aws.amazon.com/ec2/pricing/on-demand/

storage pricing: https://aws.amazon.com/ebs/pricing/

# Automatically start stop instance

aws CloudWatch -> Events -> Rules

aws Lambda

# Getting instance info by AWS CLI

aws ec2 describe-instances

