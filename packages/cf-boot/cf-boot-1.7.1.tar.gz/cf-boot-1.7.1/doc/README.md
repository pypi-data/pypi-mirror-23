<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Quick Start</a>
<ul>
<li><a href="#sec-1-1">1.1. Installation</a></li>
<li><a href="#sec-1-2">1.2. Usage</a></li>
</ul>
</li>
<li><a href="#sec-2">2. Overview</a>
<ul>
<li><a href="#sec-2-1">2.1. cf-boot components</a></li>
<li><a href="#sec-2-2">2.2. Architecture diagram</a></li>
<li><a href="#sec-2-3">2.3. Benefits</a></li>
</ul>
</li>
<li><a href="#sec-3">3. Project Spec specification</a>
<ul>
<li><a href="#sec-3-1">3.1. Jobs</a></li>
<li><a href="#sec-3-2">3.2. Spec file</a></li>
<li><a href="#sec-3-3">3.3. Job execution order</a></li>
</ul>
</li>
<li><a href="#sec-4">4. Subscripts</a>
<ul>
<li><a href="#sec-4-1">4.1. Built-in subscripts</a></li>
<li><a href="#sec-4-2">4.2. Creating a new sub-script</a></li>
<li><a href="#sec-4-3">4.3. Adding custom subscripts to the cf-boot path</a></li>
<li><a href="#sec-4-4">4.4. Subscript environment variables, proxies</a></li>
</ul>
</li>
</ul>
</div>
</div>

**cf-boot** provides a declarative mechanism for bootstrapping
   cloudfoundry products.  
The project provides a cleaner and more robust alternative to long, complex, monolithic
bootstrap scripts, by decoupling the `how` and `what`
  components of bootstrapping.

# Quick Start<a id="sec-1" name="sec-1"></a>

## Installation<a id="sec-1-1" name="sec-1-1"></a>

    $ sudo -E pip install cf-boot
    $ cf-boot -h
     usage: cf-boot [-h] [-i INPUT] [-o OUTPUT] [-f] [-p PATH]
                    [-g DEPENDENCY_GRAPH_PDF] [-v VERBOSE] [-s]
                    project-spec
     ...

Or from the source tree:

    $ git clone https://github.build.ge.com/hubs/cf-boot
    $ cd cf-boot
    $ sudo python setup.py install

## Usage<a id="sec-1-2" name="sec-1-2"></a>

    $ cf-boot ui-app-hub-boot.json -i envs/hubs-poc.json -o hubs-poc-results.json

-   Obtain or create the project spec: `ui-app-hub-boot.json`
-   Determine the free variables for the project spec
    
        cf-boot ui-app-hub-boot.json --free-vars
        [
          "app_hub_redis_instance_name",
          "CF_PASSWORD",
          "CF_TARGET",
          "uaa_service_instance_name",
          "uaa_admin_secret",
          "CF_SPACE",
          "CF_ORG",
          "logstash_instance_name",
          "kibana_basicauth_password",
          "service_broker_redis_instance_name",
          "postgres_instance_name",
          "CF_USER",
          "kibana_basicauth_username",
          "acs_service_instance_name"
        ]
-   Create a file: `envs/hubs-poc.json` initializing all free variables
    
        {
            "CF_TARGET": "https://api.system.asv-pr.ice.predix.io",
            "CF_USER": "service.hubsservice@ge.com",
            "CF_PASSWORD": "***REMOVED***",
            "CF_ORG": "HUBS",
            "CF_SPACE": "poc",
            "uaa_service_instance_name": "hubs-config-manager-uaa",
            "acs_service_instance_name": "hub-acs-dev-configservice",
            "logstash_instance_name": "logstash-space-wide",
            "service_broker_redis_instance_name": "app-hub-service-broker-redis",
            "postgres_instance_name": "apphub-configuration-postgres-service",
            "app_hub_redis_instance_name": "app-hub-redis-service",
            "kibana_basicauth_username": "kibana_user",
            "kibana_basicauth_password": "***REMOVED***",
            "uaa_admin_secret": "***REMOVED***",
            "new_relic_license_key": "***REMOVED***"
        }
-   Run jobs to bootstrap the environment.
    
        $ cf-boot ui-app-hub-boot.json --input envs/hubs-poc.json --output envs/hubs-poc-results.json
        ...
        RUNNING CHILD 3/12: 'create-service' with input:
        {
          "instance_name": "apphub-service-broker-redis",
          "cf_home": "/tmp/cf-home-98296",
          "plan": "shared-vm",
          "service": "redis"
        }
        ...
-   View bootstrap results: `cat envs/hubs-poc-results.json`
    
        {
          "CF_PASSWORD": "***REMOVED***",
          "CF_TARGET": "https://api.system.asv-pr.ice.predix.io",
          "uaa_service_instance_name": "hubs-config-manager-uaa",
          "config_manager_client_secret": "***REMOVED***-secret",
          "CF_SPACE": "dev",
          "CF_ORG": "ernesto.alfonsogonzalez@ge.com",
          "logstash_instance_name": "logstash-space-wide",
          "postgres-bootstrapper-guid": "3f1ab0cc-1656-4f96-8031-3e45f905b1fa",
          "uaa_service_guid": "07b7ba0b-15a5-4783-83c5-f2f76c80ffd1",
          "ref_app_name": "ref-app",
          "acs_service_instance_name": "hub-acs-dev-configservice",
          "postgres-bootstrapper-url": "https://postgres-bootstrapper-ernesto-alfonsogonzalez-ge-com-dev.run.asv-pr.ice.predix.io",
          "ref_app_guid": "635f6fe2-40ac-4827-ae59-d97ee2da2ae3",
          "config_manager_client_id": "***REMOVED***",
          "postgres_instance_name": "apphub-configuration-postgres-service",
          "CF_USER": "ernesto.alfonsogonzalez@ge.com",
          "uaa_client_secret": "***REMOVED***",
          "config_manager_jdbc_uri": "jdbc:postgres://***REMOVED***@10.131.54.5:5432/d642cc209e6354ecb86430a810ae2b3d0?sslmode=disable",
          "CF_HOME": "/tmp/cf-home-545030",
          "***REMOVED***": "***REMOVED***-secret",
          "postgres_service_guid": "1af550dc-08d6-4fd7-8b4d-4d20d80045c5",
          "acs_client_secret": "***REMOVED***-secret",
          "acs_client_id": "zT28Bsi4vkkf8-id",
          "service_broker_client_id": "***REMOVED***",
          "uaa_uri": "https://07b7ba0b-15a5-4783-83c5-f2f76c80ffd1.predix-uaa.run.asv-pr.ice.predix.io",
          "acs_zone": "74160e49-36a6-400d-befd-9116a7436c33",
          "service_broker_redis_instance_name": "apphub-service-broker-redis",
          "service_broker_client_secret": "***REMOVED***-secret",
          "***REMOVED***_client_id": "***REMOVED***",
          "acs_uri": "https://predix-acs.run.asv-pr.ice.predix.io"
        }

# Overview<a id="sec-2" name="sec-2"></a>

## cf-boot components<a id="sec-2-1" name="sec-2-1"></a>

-   **project spec** (`what`)
    -   User-provided specification of the bootstrap requirements:
        A JSON DSL specifying a set of `jobs`,
        each of which specifies
        -   the script to execute it
        -   the inputs to the script
        -   the outputs to capture from the script
        
        Outputs from one job can be passed as inputs to another job
    -   **free variables** (`what`)
        -   environment-specific values or sensitive values such as passwords
            or other credentials, which are decoupled from the project spec
-   **subscripts** (`how`)
    -   Executable, reusable scripts that are invoked
        by the master script to carry out a job
        specified in the user's project spec.
-   **master script** (`what` + `how`)
    -   project-spec parsing and execution engine, organizing jobs by dependency,
        piping job inputs and outputs, producing final JSON key-value map  
               The master script links the `what` and the `how`

## Architecture diagram<a id="sec-2-2" name="sec-2-2"></a>

![img](cfboot/master/hubs-bootstrapper-architecture.png "Architecture diagram")

## Benefits<a id="sec-2-3" name="sec-2-3"></a>

-   Decoupling of `how` and `what` allows users to bootstrap
    their products declaratively instead of writting code
-   Arbitrary chaining of jobs and the data they produce
-   Automatic dependency management based on inputs/outputs
-   Decoupling of environment-specific values, credentials, passwords from the
    project spec
    -   Allows project spec to be published and serve as bootstrap documentation
    -   Allows project spec to remain stable across environments
-   Flexibility to allow user to provide custom subscripts
    to meet highly product-specific bootstrap needs
-   Idempotence as a way to cleanly address the need to update,
-   Idempotence as a way to handle or clean up undefined or undesirable state

# <a id="project-spec" name="project-spec"></a> Project Spec specification<a id="sec-3" name="sec-3"></a>

The project spec is a JSON document

## Jobs<a id="sec-3-1" name="sec-3-1"></a>

A job is a JSON map with 3 required fields, **script**, **input**, **output**, and optionally a **description**

<table border="2" cellspacing="0" cellpadding="6" rules="all" frame="border">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">**field name**</td>
<td class="left">**field type**</td>
<td class="left">**field description**</td>
<td class="left">**example**</td>
</tr>


<tr>
<td class="left">script</td>
<td class="left">string</td>
<td class="left">the name of the sub-script to carry out the job</td>
<td class="left">"create-uaa-service"</td>
</tr>


<tr>
<td class="left">output</td>
<td class="left">map of string -> string</td>
<td class="left">keys much match sub-script output names. values are the names that other jobs may refer to.</td>
<td class="left">{"service\_guid":"uaa\_service\_guid", "client\_secret":"uaa\_client\_secret", "uaa\_uri":"uaa\_uri"}</td>
</tr>


<tr>
<td class="left">input</td>
<td class="left">map of string -> JSON</td>
<td class="left">keys must match sub-script input names. values may be any JSON object. nested strings starting with `$` are substituted with their known value</td>
<td class="left">{"uaa\_uri":"$uaa\_uri", "uaa\_client\_secret":"$uaa\_client\_secret", "acs\_zone":"$acs\_zone"}</td>
</tr>


<tr>
<td class="left">description</td>
<td class="left">string</td>
<td class="left">optional description of the job</td>
<td class="left">"uaa service for config manager"</td>
</tr>
</tbody>
</table>

## Spec file<a id="sec-3-2" name="sec-3-2"></a>

A spec file is a JSON mapping "jobs" to a list of jobs:

    {
       "jobs": [
    ...
          {
             "script": "create-unique-cf-home",
             "description": "unique cf login for all sub-scripts that must use cf commands",
             "input": {
                "CF_TARGET": "$CF_TARGET",
                "CF_USER": "$CF_USER",
                "CF_PASSWORD": "$CF_PASSWORD",
                "CF_ORG": "$CF_ORG",
                "CF_SPACE": "$CF_SPACE"
             },
             "output": {
                "CF_HOME": "CF_HOME"
             }
          },
          {
             "script": "create-service",
             "description": "create config manager postgres instance",
             "input": {
                "instance_name": "$postgres_instance_name",
                "service": "postgres",
                "plan": "shared-nr",
                "cf_home": "$CF_HOME"
             },
             "output": {
                "SERVICE_GUID": "postgres_service_guid"
             }
          },
          {
             "script": "extract-service-credentials",
             "description": "obtain jdbc uri of config manager postgres instance",
             "input": {
                 "app_guid": "$postgres-bootstrapper-guid",
                 "cf_home": "$CF_HOME",
                 "service_instance_guid": "$postgres_service_guid",
                 "credential_paths": {"jdbc_uri" : ["jdbc_uri"]}
              },
              "output": {
                 "jdbc_uri": "config_manager_jdbc_uri"
              }
           }
    
          ...
        ]
    }

-   In the first job
    -   `$CF_TARGET`, `$CF_USER`, `$CF_PASSWORD`, `$CF_ORG`, `$CF_SPACE` are free variables since they are not produced by any other job.
    -   `create-unique-cf-home` script outputs a variable `CF_HOME`, which we capture internally as `CF_HOME`
-   The second job
    -   refers to the `$CF_HOME` produced by the first job
    -   Its script outputs a variable `SERVICE_GUID`,
        which we capture internally as `postgres_service_guid`
-   The third job uses `postgres-service-guid` from the second job, as
    well as `CF_HOME` from the first job, and produces `config_manager_jdbc_uri`

A project spec is malformed if it contains two jobs which output the same
variable

## Job execution order<a id="sec-3-3" name="sec-3-3"></a>

The master script automatically determines job order based on variable dependencies. If
-   Job **A** outputs **X** and
-   Job **B** refers to **$X**, then
-   Job **A** must run before Job **B**

This implies no job can depend on a job that produces no outputs.
For such cases, a job may produce a dummy indicator variable that can be refered by any dependent jobs.  

A project spec is malformed if it contains cyclic job dependencies

# Subscripts<a id="sec-4" name="sec-4"></a>

## Built-in subscripts<a id="sec-4-1" name="sec-4-1"></a>

The following subscripts are provided by default as basic cf bootstrapping
building blocks:

-   [create-unique-cf-home](cfboot/scripts/create-unique-cf-home)
    -   Allows other subscripts to call cf commands against a
        particular environment safely
    -   Allow jobs to target different environments simultaneously without
        conflict
-   [create-service](cfboot/scripts/create-service),
    -   create or update a service service
-   [cf-cups](cfboot/scripts/cf-cups)
    -   create or update a user-provided service service
-   [extract-service-credentials](cfboot/scripts/extract-service-credentials)
    -   extract one or more credentials from an existing service based on their
        path within the credentials' JSON map
-   [cf-push-app](cfboot/scripts/cf-push-app)
    -   push a reference app, diagnostic app, or environment-administrative app
-   [create-uaa-clients](cfboot/scripts/create-uaa-clients)
    -   create or update clients on a uaa server
-   [create-acs-policy](cfboot/scripts/create-acs-policy)
    -   create or update an acs policy

## Creating a new sub-script<a id="sec-4-2" name="sec-4-2"></a>

A subscript is any executable file NAME.EXT that conforms to the following requirements:
-   Is executable
-   Lives under `NAME/NAME.EXT` somewhere on the subscripts **path**
-   Read all its input from stdin JSON
-   Output all data as a JSON key-value pairs
    -   May display progress/debug logs to stderr
-   Must be idempotent. Running the script multiple times should be equivalent to running it once
    -   Most of the cf api, as well as cf commands already have this property

Sub-scripts should also observe the following guidelines
-   Have small and clearly defined scope and meaningful name
-   Be self-contained and not interfere with OS user or other processes
    -   Any scripts running CF commands must explicitly set the CF\_HOME environment variable
    -   Should not use uaac until CF\_HOME-like support is added

Pull requests are welcome for subscripts which meet the above guidelines
and provide functionality not already covered

## Adding custom subscripts to the cf-boot path<a id="sec-4-3" name="sec-4-3"></a>

Use the `--path` flag to specify the custom subscript's directory:

     $ cf-boot -h
     ...
    -p PATH, --path PATH  colon-delimited path where to find additional
                           subscripts
     $ cf-boot ui-app-hub-bootstrap.json --path /path/to/my/own/subscripts --input envs/hubs-poc.json
     ...

## Subscript environment variables, proxies<a id="sec-4-4" name="sec-4-4"></a>

The master script's environment variables are passed onto its children subscripts, including https\_proxy.  
   It is up to the subscripts to either use or override these variables.