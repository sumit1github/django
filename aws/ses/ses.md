# install
    pip install boto3

# Setting up AWS SES for Sending Emails
# email verification vs domain verification

1. **email:**

    The mail can be fired from only the email address which is verified.

2. **domain**

    if the domain is verified, like assiduusinc.com, we can able to send the mail from any email address of assiduusinc.com.


# SES creation 

### IAM
1. first select a region

2. create an user
    * only programatic access
    * assign permission
        * sesfullacess

    * **generate access**
        * select "other"
        * download the credentical .csv file

# Domain verifcation 
1. create identity
2. email address
3. using DKIM (domain key identity management)
    * an email is going to send to email id for verification purpose
4. we need to create the CNAME
    * from ses we can get the txt record
5. Now go the DNS management dashboard of the domain provider (go-daddy)
    * update the txt record
    * it will take some time to update


# problem: mail is going in junk
1. for not using proper subject
2. for the non standard mail content
3. Due the spf record
    * tool to check: 

# ses client
    import boto3
    
    ses = boto3.client(
        'ses', 
        aws_access_key_id=aws_access_key, 
        aws_secret_access_key=aws_secret_key,
        region_name='us-east-1'
    )
    SENDER_EMAIL = 'sumit@gmail.com'

# send mail function

    def send_mail(subject, body, RECIPIENT=["sumit1panda@gmail.com",]):

        email_date_object = utils.GetDateTime()
        email_today_date = str(email_date_object.get_datetime())
        try:
            # Provide the contents of the email.
            response = ses.send_email(
                Destination={
                    'ToAddresses': RECIPIENT,
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': "UTF-8",
                            'Data': body,
                        },
                        'Text': {
                            'Charset': "UTF-8",
                            'Data': body,
                        },
                    },
                    'Subject': {
                        'Charset': "UTF-8",
                        'Data': subject,
                    },
                },
                Source=SENDER_EMAIL,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
            utils.send_sqs_data(f"error in send_mail $ {email_today_date} $ error : {e}")
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

# send html data through the mail
Pass dynamic data
- create email.html
- <h1> hi i am {my_name} </h1>



        with open("templates/email_templates/email.html","r") as html_content:
            raw_html_content = html_content.read().format(my_name='sumit panda')
            subject = "<enter_subject>
            body_content = raw_html_content
            RECIPIENT = [
                "sumit@mail.com.com",
                "user@gmail.com"
                
            ]
            send_mail(subject, body_content, RECIPIENT)
