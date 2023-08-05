Formica
=======

|Build Status| |PyPI version| |license| |Coverage Status|

Formica makes it easy to create and deploy CloudFormation stacks. It
uses CloudFormation syntax with yaml and json support to define your
templates. Any existing stack can be used directly, but formica also has
built-in modularity so you can reuse and share CloudFormation stack
components easily. This allows you to start from an existing stack but
split it up into separate files easily.

For dynamic elements in your templates Formica supports
`jinja2 <http://jinja.pocoo.org/docs/2.9/templates/>`__ as a templating
engine. Jinja2 is widely used, for example in ansible configuration
files.

Installation
------------

Formica can be installed through pip:

.. code:: shell

    pip install formica-cli

Alternatively you can clone this repository and run

.. code:: shell

    python setup.py install

After installing Formica take a look at the `quick start
guide <#quick-start-guide>`__ or the `in-depth
documentation <docs#formica-documentation>`__ and
`examples <docs#examples>`__

AWS Credentials
---------------

Formica supports all the standard AWS credential settings, so you can
use profiles through the ``--profile`` option, provide no specific
profile which will use the default profile or set environment variables
like **AWS\_ACCESS\_KEY\_ID**. Take a look at the `AWS credentials
docs <http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html>`__
for more details on how to configure these credentials.

Why
---

AWS CloudFormation provides a great service for automatically deploying
and updating your infrastructure. But while the service itself is great
the tooling to deploy and manage CloudFormation has been lacking. This
means that many teams aren't using CloudFormation or automating their
infrastructure as much as they should. Formica tries to be a great
CloudFormation client by making it easy to build modular templates, make
parts of templates reusable and give you great tooling to deploy to and
inspect your CloudFormation stacks.

Our goal is that you should never have to log into the AWS Console to
look at your CloudFormation stacks, because Formica gives you all the
info you need right in your shell.

Quick Start Guide
-----------------

You can also jump to the `in-depth docs <docs>`__ for more information.

You define your CloudFormation template through
``*.template.(json/yaml/yml)`` files. Those files will be automatically
loaded from the current working directory and executed to create your
template.

In this example we'll create an S3 Bucket. We use jinja templating to
set a variable and use it for the bucket logical name. Put the following
into a ``bucket.template.yml`` file:

.. code:: yaml

    {% set bucket = "DeploymentBucket" %}
    Resources:
      {{ bucket }}:
        Type: "AWS::S3::Bucket"

In the same folder run ``formica template`` which should show you the
following template:

.. code:: json

    {
        "Resources": {
            "DeploymentBucket": {
                "Type": "AWS::S3::Bucket"
            }
        }
    }

Now we'll create a new stack with this template:

.. code:: shell

    formica new --stack formica-example-stack

This will create a new ChangeSet in CloudFormation that we can deploy in
a next step. It will also describe all the changes that will be done.
Instead of setting ``--stack`` for every command you can also set the
``FORMICA_STACK`` environment variable which will be picked up
automatically.

.. code:: shell

    root@62d81801cc09:/app/examples/s3-bucket# formica new --stack formica-example-stack
    Creating change set for new stack, ...
    Change set submitted, waiting for CloudFormation to calculate changes ...
    Change set created successfully
    Deployment metadata:
    +---------------+--+
    | Parameters    |  |
    +---------------+--+
    | Tags          |  |
    +---------------+--+
    | Capabilities  |  |
    +---------------+--+

    Resource Changes:
    +--------+------------------+------------+-----------------+-------------+---------+
    | Action |    LogicalId     | PhysicalId |      Type       | Replacement | Changed |
    +========+==================+============+=================+=============+=========+
    | Add    | DeploymentBucket |            | AWS::S3::Bucket |             |         |
    +--------+------------------+------------+-----------------+-------------+---------+
    Change set created, please deploy.

For more detail on the ChangeSet description check out the `describe
command documentation <TODO>`__.

All changes, whether you want to create a new stack or update an
existing one, are done through
`ChangeSets <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html>`__.
This makes sure you can inspect the specific actions that CloudFormation
will take before deploying them. In a CI context you can of course
simply run both commands one after the other to get a fully automated
deployment.

Now we can deploy the changes:

``formica deploy --stack formica-example-stack``

The command will follow the CloudFormation stack events and print them
to the command line. If the deployment fails, so will the command.

.. code:: shell

    root@62d81801cc09:/app/examples/s3-bucket# formica deploy --stack formica-example-stack
    +------------------------------+--------------------------+--------------------------------+--------------------------------+----------------------------------------------------+
    |          Timestamp           |          Status          |              Type              |           Logical ID           |                   Status reason                    |
    +------------------------------+--------------------------+--------------------------------+--------------------------------+----------------------------------------------------+
    2017-02-15 10:14:27 UTC+0000   CREATE_IN_PROGRESS         AWS::CloudFormation::Stack       formica-example-stack            User Initiated
    2017-02-15 10:14:31 UTC+0000   CREATE_IN_PROGRESS         AWS::S3::Bucket                  DeploymentBucket
    2017-02-15 10:14:32 UTC+0000   CREATE_IN_PROGRESS         AWS::S3::Bucket                  DeploymentBucket                 Resource creation Initiated
    2017-02-15 10:14:53 UTC+0000   CREATE_COMPLETE            AWS::S3::Bucket                  DeploymentBucket
    2017-02-15 10:14:55 UTC+0000   CREATE_COMPLETE            AWS::CloudFormation::Stack       formica-example-stack

After the deployment we will now see our new S3 Bucket. As we didn't set
a name the name of the bucket is generated by S3:

.. code:: shell

    root@62d81801cc09:/app/examples/s3-bucket# aws s3 ls
    2017-02-15 11:21:18 formica-example-stack-deploymentbucket-57ouvt2o46yh

We can also check out all the resources for a specific stack with the
resources command:

::

    root@67c57a89511a:/app/docs/examples/s3-bucket# formica resources --stack formica-example-stack
    +------------------+------------------------------------------------------+-----------------+-----------------+
    |    Logical ID    |                     Physical ID                      |      Type       |     Status      |
    +==================+======================================================+=================+=================+
    | DeploymentBucket | formica-example-stack-deploymentbucket-57ouvt2o46yh  | AWS::S3::Bucket | CREATE_COMPLETE |
    +------------------+------------------------------------------------------+-----------------+-----------------+

If we want to add an additional bucket we can change add a second file
``bucket2.template.json`` file with the following content:

.. code:: json

    {"Resources": {
      "DeploymentBucket2": {
        "Type": "AWS::S3::Bucket"
        }
      }
    }

Running ``formica template`` again will now result in both files being
picked up and merged:

.. code:: json

    {
        "Resources": {
            "DeploymentBucket": {
                "Type": "AWS::S3::Bucket"
            },
            "DeploymentBucket2": {
                "Type": "AWS::S3::Bucket"
            }
        }
    }

and then run the change and deploy commands:

::

    formica change --stack formica-example-stack
    formica deploy --stack formica-example-stack

And we can now see both buckets in S3:

.. code:: shell

    root@62d81801cc09:/app/examples/s3-bucket# aws s3 ls
    2017-02-15 11:21:18 formica-example-stack-deploymentbucket-57ouvt2o46yh
    2017-02-15 11:21:18 formica-example-stack-deploymentbucket2-1jv31cwqdh5gk

And we can list all the stacks to see the status with
``formica stacks``:

.. code:: shell

    root@62d81801cc09:/app/examples/s3-bucket# formica stacks
    Current Stacks:
    +-------------------------------+----------------------------------+----------------------------------+-----------------+
    |             Name              |            Created At            |            Updated At            |     Status      |
    +===============================+==================================+==================================+=================+
    | formica-example-stack         | 2017-02-15 10:02:56.809000+00:00 | 2017-02-15 10:57:54.641000+00:00 | UPDATE_COMPLETE |
    +-------------------------------+----------------------------------+----------------------------------+-----------------+

Last but not least we'll remove the stack with
``formica remove --stack formica-example-stack``

.. code:: shell

    root@62d81801cc09:/app/examples/s3-bucket# formica remove --stack formica-example-stack
    Removing Stack and waiting for it to be removed, ...
    +------------------------------+--------------------------+--------------------------------+--------------------------------+----------------------------------------------------+
    |          Timestamp           |          Status          |              Type              |           Logical ID           |                   Status reason                    |
    +------------------------------+--------------------------+--------------------------------+--------------------------------+----------------------------------------------------+
    2017-02-15 11:09:07 UTC+0000   DELETE_IN_PROGRESS         AWS::CloudFormation::Stack       formica-example-stack            User Initiated
    2017-02-15 11:09:10 UTC+0000   DELETE_IN_PROGRESS         AWS::S3::Bucket                  DeploymentBucket
    2017-02-15 11:09:31 UTC+0000   DELETE_COMPLETE            AWS::S3::Bucket                  DeploymentBucket
    2017-02-15 11:09:32 UTC+0000   DELETE_COMPLETE            AWS::CloudFormation::Stack       formica-example-stack

And now you've created, inspected, updated, deployed and removed a
CloudFormation stack with Formica.

For more in-depth information check out `our documentation <docs>`__

.. |Build Status| image:: https://travis-ci.org/flomotlik/formica.svg?branch=master
   :target: https://travis-ci.org/flomotlik/formica
.. |PyPI version| image:: https://badge.fury.io/py/formica-cli.svg
   :target: https://pypi.python.org/pypi/formica-cli
.. |license| image:: https://img.shields.io/github/license/mashape/apistatus.svg
   :target: LICENSE
.. |Coverage Status| image:: https://coveralls.io/repos/github/flomotlik/formica/badge.svg?branch=master
   :target: https://coveralls.io/github/flomotlik/formica?branch=master
