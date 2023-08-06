import asyncio
import os
import pickle
import logging

import aiobotocore
import botocore
import botocore.session
import botocore.exceptions

import ws_storage.base
import ws_storage.exceptions

logger = logging.getLogger(__name__)


class Storage(ws_storage.base.Storage):
    """
    :param conf: configuration object

    the configuraion must have the following attributes

    - ``AWS_ACCESS_KEY_ID``
    - ``AWS_SECRET_ACCESS_KEY``
    - ``AWS_BUCKET``
    - ``AWS_REGION``

    """
    def __init__(self, conf, loop):
        super(Storage, self).__init__()
        self.conf = conf
        self.loop = loop
        
        self.session = botocore.session.get_session()
        #self.session = aiobotocore.get_session(loop=loop)

        self.client_kwargs = {
            'region_name': self.conf.AWS.REGION,
            'aws_secret_access_key': self.conf.AWS.SECRET_ACCESS_KEY,
            'aws_access_key_id': self.conf.AWS.ACCESS_KEY_ID,
            }
        
        logger.debug('client kwargs')
        for k, v in self.client_kwargs.items():
            logger.debug('{:32}{}'.format(k, v))

    async def _write_binary_TEST(self, id_, b):
        logger.debug('write')
        
        client = self.session.create_client(
                's3', **self.client_kwargs)

        logger.debug('client={}'.format(client))
        #await client.create_bucket(
        #        Bucket=self.conf.AWS.BUCKET,)
        
        # upload object to amazon s3
        resp = client.put_object(
                Bucket=self.conf.AWS.BUCKET,
                Key=id_,
                Body=b)
        
        logger.debug('resp={}'.format(resp))

    async def _read_binary_TEST(self, id_, endpoint_url=None):
        logger.debug('read')
        
        client = self.session.create_client(
                's3', **self.client_kwargs, endpoint_url=endpoint_url)
        
        logger.debug('client={}'.format(client))
        # get object from s3
        
        try:
            resp = client.get_object(
                    Bucket=self.conf.AWS.BUCKET,
                    Key=id_)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchKey':
                raise ws_storage.exceptions.FileNotFound(id_)
            else:
                raise

        # this will ensure the connection is correctly re-used/closed
        logger.debug('resp={}'.format(resp))
        
        b = resp['Body'].read()
        
        return b
    
    async def _write_binary(self, id_, b):
        logger.debug('write')
        return (await self._write_binary_TEST(id_, b))
        
        async with self.session.create_client(
                's3', **self.client_kwargs) as client:
            logger.debug('client={}'.format(client))
            #await client.create_bucket(
            #        Bucket=self.conf.AWS.BUCKET,)
            
            try:
                # upload object to amazon s3
                resp = await client.put_object(
                        Bucket=self.conf.AWS.BUCKET,
                        Key=id_,
                        Body=b)
            except Exception as e:
                logger.error(e)
                raise
            
            logger.debug('resp={}'.format(resp))

    async def _read_binary(self, id_, endpoint_url=None):
        logger.debug('read')
        return (await self._read_binary_TEST(id_, endpoint_url))
        
        async with self.session.create_client(
                's3', **self.client_kwargs, endpoint_url=endpoint_url) as client:
            logger.debug('client={}'.format(client))
            # get object from s3
            
            try:
                resp = await client.get_object(
                        Bucket=self.conf.AWS.BUCKET,
                        Key=id_)
            except botocore.exceptions.ClientError as e:
                logger.error(e)
                logger.error(e.response['Error'])
                
                if e.response['Error']['Code'] == 'TemporaryRedirect':
                    if endpoint_url is None:
                        return await self._read_binary(id_, endpoint_url='https://'+e.response['Error']['Endpoint'])
                    else:
                        logger.error('already retried with endpoint_url={}'.format(repr(endpoint_url)))
                
                raise
            except Exception as e:
                logger.error(e)
                raise

            # this will ensure the connection is correctly re-used/closed
            logger.debug('resp={}'.format(resp))
            async with resp['Body'] as stream:
                b = await stream.read()
            return b

    async def list_files_TEST(self):
        client = self.session.create_client(
                's3', **self.client_kwargs,)

        paginator = client.get_paginator('list_objects')

        logger.debug('paginator={}'.format(paginator))
        
        ret = []

        for result in paginator.paginate(Bucket=self.conf.AWS.BUCKET):
            for c in result.get('Contents', []):
                logger.debug('key={}'.format(c['Key']))
                ret.append(c['Key'])
        
        return ret

    async def list_files(self):
        return (await self.list_files_TEST())
        
        logger.debug('list files')
        ret = []
        async with self.session.create_client(
                's3', **self.client_kwargs) as client:
            
            logger.debug('client={}'.format(client))

            # list files
            paginator = client.get_paginator('list_objects')

            logger.debug('paginator={}'.format(paginator))

            async for result in paginator.paginate(Bucket=self.conf.AWS.BUCKET):
                logger.debug('result={}'.format(result))
                 
                for c in result.get('Contents', []):
                    logger.debug('c={}'.format(c))
                    ret.append(c)

        return ret

    async def _delete(self, id_):
        logger.debug('delete')
        
        client = self.session.create_client('s3', **self.client_kwargs)
        
        try:
            resp = client.delete_object(
                    Bucket=self.conf.AWS.BUCKET,
                    Key=id_)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchKey':
                raise ws_storage.exceptions.FileNotFound(id_)
            else:
                raise

        logger.debug(resp)


