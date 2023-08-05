import setuptools

version = '0.3.8'

setuptools.setup(
        name='ctec_consumer',
        version=version,
        packages=['ctec_consumer', 'ctec_consumer.models', 'ctec_consumer.dummy', 'ctec_consumer.dummy.models',
                  'ctec_consumer.gevent', 'ctec_consumer.gevent.models'],
        author='ZhangZhaoyuan',
        author_email='zhangzhy@chinatelecom.cn',
        url='http://www.189.cn',
        description='189 rabbitMQ consumer',
        install_requires=['kombu==3.0.35', 'gevent==1.2.1', 'pika==0.10.0']
)
