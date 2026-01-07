import os

S3_BUCKET_FOLDER = "mock_s3_bucket"

def lambda_handler():
    files = os.listdir(S3_BUCKET_FOLDER)
    
    for file in files:
        print(f"lambda triggerd for file: {file}")
        
if __name__ == "__main__":
    lambda_handler()     