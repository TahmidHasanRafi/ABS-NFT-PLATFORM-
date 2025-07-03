import os
import io
import json
import time
import boto3
import logging
from botocore.exceptions import ClientError, NoCredentialsError
from botocore.client import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_s3_client():
    """Initialize and return S3 client with credentials"""
    FILEBASE_KEY = os.getenv("FILEBASE_KEY")
    FILEBASE_SECRET = os.getenv("FILEBASE_SECRET")
    FILEBASE_ENDPOINT = os.getenv("FILEBASE_ENDPOINT", "https://s3.filebase.com")
    
    if not FILEBASE_KEY or not FILEBASE_SECRET:
        logger.error("Missing Filebase credentials in environment")
        raise ValueError("Filebase credentials not configured")
    
    try:
        session = boto3.session.Session()
        return session.client(
            's3',
            aws_access_key_id=FILEBASE_KEY,
            aws_secret_access_key=FILEBASE_SECRET,
            endpoint_url=FILEBASE_ENDPOINT,
            config=Config(signature_version='s3v4'),
            region_name='us-east-1'
        )
    except Exception as e:
        logger.error(f"Error creating S3 client: {e}")
        raise

def upload_file_to_filebase(file_obj, key_prefix, filename):
    try:
        s3 = get_s3_client()
        BUCKET_NAME = os.getenv("BUCKET_NAME", "zk-nft-marketplace")
        GATEWAY_URL = os.getenv("GATEWAY_URL", "https://ipfs.filebase.io/ipfs/")
        
        s3_key = f"{key_prefix}/{filename}"
        
        # Handle file-like objects
        if isinstance(file_obj, io.IOBase):
            file_obj.seek(0)
            content = file_obj.read()
            file_obj = io.BytesIO(content)
        elif hasattr(file_obj, 'file'):  # Flask FileStorage
            file_obj.stream.seek(0)
            content = file_obj.stream.read()
            file_obj = io.BytesIO(content)
        
        s3.upload_fileobj(
            Fileobj=file_obj,
            Bucket=BUCKET_NAME,
            Key=s3_key,
            ExtraArgs={'Metadata': {'cid': 'true'}}
        )
        
        head = s3.head_object(Bucket=BUCKET_NAME, Key=s3_key)
        cid = head['Metadata'].get('cid')
        if not cid:
            raise RuntimeError(f"CID not found for {s3_key}")
            
        return f"{GATEWAY_URL}{cid}", s3_key
    except NoCredentialsError:
        logger.error("Missing Filebase credentials")
        raise RuntimeError("Filebase credentials not configured")
    except ClientError as e:
        logger.error(f"Filebase API error: {e.response['Error']['Message']}")
        raise RuntimeError(f"Filebase upload failed: {e.response['Error']['Message']}")
    except Exception as e:
        logger.error(f"Unexpected upload error: {str(e)}")
        raise RuntimeError(f"Upload failed: {str(e)}")