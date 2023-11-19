# aws s3 setup

1. create s3 and allow public access

# update bucket policy and permission
- go to permission and add bucket policy

> copy and paste

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": "*"
                },
                "Action": "s3:*",
                "Resource": [
                    "arn:aws:s3:::bucket_name",
                    "arn:aws:s3:::bucket_name/*"
                ]
            }
        ]
    }

# CORS Policy
go down on same permission page and edit the cors policy

    [
        {
            "AllowedHeaders": [
                "*"
            ],
            "AllowedMethods": [
                "GET",
                "HEAD"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]

# IAM USER SETUP

1. now create a IAM user to access the bucket
2. search IAM > users > create user > enter name > Set permissions > Attach policies directly
3. search   "s3 full access" and check and submit
4. user list > security credential > create access key
5. use access key in project

