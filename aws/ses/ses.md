# install
    pip install boto3

# Setting up AWS SES for Sending Emails


1. **Access SES from AWS Console:**

Once logged in, go to the AWS Management Console and search for "SES" in the services search bar.

2. **Verify Your Email Address or Domain:**

In SES, under "Email Addresses" or "Domains," verify the email addresses or domains you plan to send emails from. This involves receiving and acting on verification emails sent by AWS SES.

3. **Get SMTP Credentials:**

To send emails programmatically through SES, you'll need SMTP credentials. These can be generated in the SES console. Go to "SMTP Settings" under "Email Sending" and create an IAM user with SMTP credentials.

4. **Configure Your Application:**

Integrate the SMTP credentials (SMTP server, username, password) into your application or email-sending library. Libraries like smtplib in Python can be used to send emails using the SES SMTP server.

### Setting up AWS SES for Receiving Emails

1. **Create SES Rule Sets and Configuration:**

In SES, under "Email Receiving," you can create rule sets to define how SES handles incoming emails. Configure rules to specify the actions (e.g., save to an S3 bucket, invoke a Lambda function) to be taken upon receiving emails.

2. **DNS Configuration (Optional):** 
If you want to receive emails for a specific domain, you'll need to set up DNS records to direct incoming emails to SES. This involves updating MX records in your domain's DNS settings to point to SES.

3. **Handle Incoming Emails in Your Application (if applicable):**

If you want to process incoming emails in your application, configure the necessary endpoints or services to handle SES notifications or store the received emails.

### Note:
1. SES Usage and Limits: AWS SES has usage limits and a sandbox mode for new accounts. In the sandbox, you can only send emails to verified email addresses. Request a limit increase to move out of the sandbox and increase your sending limits.

2. Billing and Cost: AWS SES has a pay-as-you-go pricing model. Be aware of the costs associated with sending and receiving emails based on SES pricing.

3. This overview provides a general guide; the exact steps might vary slightly based on AWS updates and changes. Always refer to the official AWS SES documentation for the most accurate and detailed instructions.

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
