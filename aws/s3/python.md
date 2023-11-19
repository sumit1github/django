# install boto3
pip install boto3

# create s3 client
    bucket_name = '<buket_name>'
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# file_upload in s3 (creating csv and upload to s3)
    df = pd.DataFrame(new_order_objects)
    csv_data = df.to_csv(index=False)

    folder_name_inside_s3 = 'inbound
    object_name = f'{folder_name_inside_s3}/file_name.csv'  # S3 object name
    s3.put_object(Bucket=bucket_name, Key=object_name, Body=csv_data)

# download a file from s3
    object_key = '<folder_name/file_name.csv'  # location in s3

    local_file_path = f"/media/downloads/file_name.csv"  # where we are going to save
    s3.download_file(bucket_name, object_key, local_file_path)

# read content of a file from s3
    object_key = '<folder_name/file_name.txt'  # location in s3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    file_content = response['Body'].read().decode('utf-8')

# move a file from 1 folder to another

    previous_s3_destination = '<folder-1/file_name.txt'
    new_s3_destination = '<folder-2/file_name.txt'

    s3.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': object_key}, Key=destination_key)

    # Delete the old object (to simulate a move)
    s3.delete_object(Bucket=bucket_name, Key=object_key)

# delete an s3 object
    s3.delete_object(Bucket=bucket_name, Key=object_key)

# upload same file in 2 diffrent folder
    file_obj = io.BytesIO(summary_raw_text_data.encode('utf-8'))

    s3.put_object(Bucket=bucket_name, Key=f'outbound/{outboud_file_name}', Body=file_obj)
    s3.put_object(Bucket=bucket_name, Key=f'outboundarchive/{outboud_file_name}', Body=file_obj)
    file_obj.close()