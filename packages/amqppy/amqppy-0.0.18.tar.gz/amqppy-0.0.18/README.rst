amqppy
======
AMQP simplified client for Python

|Version| |Versions| |Status| |Coverage| |License| |Docs|

Introduction to amqppy
----------------------
**amqppy** is a very simplified AMQP client stacked over `Pika <https://github.com/pika/pika>`_. It has been tested with `RabbitMQ <https://www.rabbitmq.com>`_, however it should also work with other AMQP 0-9-1 brokers.

The motivation of **amqppy** is to provide a very simplified and minimal AMQP client interface which can help Python developers to implement easily messaging patterns such as:

* `Topic Publisher-Subscribers <https://www.rabbitmq.com/tutorials/tutorial-five-python.html>`_
* `RPC Request-Reply <https://www.rabbitmq.com/tutorials/tutorial-six-python.html>`_

Others derivative `messaging patterns <https://www.rabbitmq.com/getstarted.html>`_ can be implemented tunning some parameters of the Topic and Rpc objects.


Installing amqppy
-----------------
**amqppy** is available for download via PyPI and may be installed using easy_install or pip::

    pip install amqppy


To install from source, run "python setup.py install" in the root source directory.

Documentation
-------------
**amqppy**  documentation can be found here: `https://amqppy.readthedocs.io <https://amqppy.readthedocs.io>`_

Topic Publisher-Subscribers
---------------------------
This is one of the most common messaging pattern where the publisher publishes message to an AMQP exchange and the subscriber receives only the messages that are of interest. The subscriber's interest is modeled by the *Topic* or in terms of AMQP by the **rounting_key**. 

.. image:: https://www.rabbitmq.com/img/tutorials/python-five.png

Image from RabbitMQ `Topic tutorial <https://www.rabbitmq.com/tutorials/tutorial-five-python.html>`_.

Topic Subscriber
________________
Firstly, we need to start the Topic Subscriber (*also known as Consumer*). In **amqppy** the class **amqppy.consumer.Worker** has this duty.

.. code-block:: python

    import amqppy
    BROKER = 'amqp://guest:guest@localhost:5672//'

    def on_topic_status(exchange, routing_key, headers, body):
        print('Received message from topic \'amqppy.publisher.topic.status\': {}'.format(body))

    # subscribe to a topic: 'amqppy.publisher.topic.status'
    worker = amqppy.Worker(BROKER)
    worker.add_topic(exchange='amqppy.test',
                     routing_key='amqppy.publisher.topic.status',
                     on_topic_callback=on_topic_status)
    # it will wait until worker is stopped or an uncaught exception
    worker.run()

The subscriber worker will invoke the *on_topic_callback* every time a message is published with a topic that matches with the specified **routing_key**: `'amqppy.publisher.topic.status'`. Note that **routing_key** can contain `wildcards <https://www.rabbitmq.com/tutorials/tutorial-five-python.html>`_ therefore, one subscriber might be listening a set of *Topics*.

Once the topic subscriber is running we able to launch the publisher.

Topic Publisher
________________

.. code-block:: python

    import amqppy
    BROKER = 'amqp://guest:guest@localhost:5672//'

    # publish my current status
    amqppy.Topic(BROKER).publish(exchange='amqppy.test',
                                 routing_key='amqppy.publisher.topic.status',
                                 body='RUNNING')

The topic publisher will send a message to the AMQP exchange with the Topic **routing_key**: `'amqppy.publisher.topic.status'`, therefore, all the subscribed subscribers will receive the message unless they do not share the same queue. In case they share the same queue a round-robin dispatching policy would be applied among subscribers/consumers like happens in `work queues <https://www.rabbitmq.com/tutorials/tutorial-two-python.html>`_.

RPC Request-Reply
-----------------
This pattern is commonly known as *Remote Procedure Call* or *RPC*. And is widely used when we need to run a function *request* on a remote computer and wait for the result *reply*.

.. image:: https://www.rabbitmq.com/img/tutorials/python-six.png

Image from RabbitMQ `RPC tutorial <https://www.rabbitmq.com/tutorials/tutorial-six-python.html>`_

RPC Reply
_________
An object of type **amqppy.consumer.Worker** listens incoming **RPC requests** and computes the **RPC reply** in the *on_request_callback*. In the example below, the RPC consumer listens on Request **rounting_key**:`'amqppy.requester.rpc.division'` and the division would be returned as the RPC reply.

.. code-block:: python

    import amqppy
    BROKER = 'amqp://guest:guest@localhost:5672//'

    def on_rpc_request_division(exchange, routing_key, headers, body):
        args = json.loads(body)
        return args['dividend'] / args['divisor']

    # subscribe to a rpc request: 'amqppy.requester.rpc.division'
    worker = Worker(BROKER)
    worker.add_request(exchange='amqppy.test',
                       routing_key='amqppy.requester.rpc.division',
                       on_request_callback=on_rpc_request_division)
    # it will wait until worker is stopped or an uncaught exception
    worker.run()


RPC Request
___________
The code below shows how to do a **RPC Request** using an instance of class *amqppy.publisher.Rpc*

.. code-block:: python

    import amqppy
    BROKER = 'amqp://guest:guest@localhost:5672//'

    # do a Rpc request 'amqppy.requester.rpc.division'
    result = amqppy.Rpc(BROKER).request(exchange='amqppy.test',
                                        routing_key='amqppy.requester.rpc.division',
                                        body=json.dumps({'dividend': 3.23606797749979, 'divisor': 2.0}))
    print('RPC result: {}.'.format(result))




.. |Version| image:: https://img.shields.io/pypi/v/amqppy.svg?
   :target: http://badge.fury.io/py/amqppy

.. |Versions| image:: https://img.shields.io/pypi/pyversions/amqppy.svg
    :target: https://pypi.python.org/pypi/amqppy

.. |Status| image:: https://img.shields.io/travis/marceljanerfont/amqppy.svg?
   :target: https://travis-ci.org/marceljanerfont/amqppy

.. |Coverage| image:: https://img.shields.io/codecov/c/github/marceljanerfont/amqppy.svg?
   :target: https://codecov.io/github/marceljanerfont/amqppy?branch=production

.. |License| image:: https://img.shields.io/pypi/l/amqppy.svg?
   target: https://pypi.python.org/pypi/amqppy

.. |Docs| image:: https://readthedocs.org/projects/amqppy/badge/?version=stable
   :target: https://amqppy.readthedocs.org
   :alt: Documentation Status
