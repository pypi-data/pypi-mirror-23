Some of you may not be aware of important new features and bugfixes in cf-boot
since the first "stable" release (v1 in December 2016). Below is a summary of important recent
changes. All of the changes are backwards-compatible, so if you are a cf-boot user running
into any of the below bugs, or if you could make use of some of the new features,
I would recommend upgrading.

# New features

-   fast cf-push-app for dummy-app **(pre-versioning)**
    -   for dummy apps used for only for binding and extracting service credentials,
        only a cf-api POST is needed, saving several minutes on `cf push`,
        `cf start`,  `git clone`
-   versioning support ****(1.2.1)****
    -   single-source versioning support and cli flag to output current version:
        `cf-boot --version`
-   cf-push "domain" option **(1.3.0)**
    -   expose `cf push`'s domain option,
        allowing app's route to be mapped to a specific domain.
    -   requested by UOM in AWS which has multiple domains for deploying kibana UI
-   support for async provisioning **(1.4.0)**
    -   `create-service` will now block until provisioning has completed.
        This prevents jobs which depend on the provisioned service to
        fail to bind and crash.
    -   requested by UOM, which needs to provision dedicated `postgres` instances
-   pip integration **(1.5.0)**
    -   it is now possible to install cf-boot via pip
        -   pip allows for easy distribution, version control and enforces version stability
-   new `service` wrapper subscript **(1.6.0)**
    -   This is a wrapper script around "create-service", "cf-push-app", and
        "extract-service-credentials",
        which replaces the low-level trio with a more declarative way to create a
        service and extract binding credentials
    -   `create-service` still supported but discouraged in new specs
-   `if_exists` option in `service` and `create-service` **(1.7.0)**
    -   feature to explicitly specify what to do when a service instance already exists ("ignore", "delete", or "update")
    -   allows changing a service instance plan via "update", or updating provisioning payload for brokers
        that support it
-   `create-uaa-clients` can now crate users, groups, add users to groups **(1.8.0)**
    -   useful for automating the setup of test users/tenants as part of bootstrapt
-   human-friendly cf-home directory names **(1.8.1)**
    -   instead of  
               `/tmp/cf-homes/f81c012cede168f92048ed58f12f46cc`, user will see  
               `/tmp/cf-homes/HUBS-dev-f81c012cede168f92048ed58f12f46cc`  
               which allows for reuse cf-boot's `CF_HOME` logins in the cli to issue one-off commands
        against certain environments. eg:
        
            CF_HOME=/tmp/cf-homes/HUBS-dev-f81c012cede168f92048ed58f12f46cc cf env cfboot-refapp | less

# Bug fixes

-   fix infinite loop in async provisioning support **(1.4.2)**
-   fix relying on inconsistent cf cli output in  cf-push-app **(1.4.5)**
    -   at some point in the cf cli, `cf target` changed to sentence-cased property names,
        eg. `Org` instead of `org`, causing cf-push-app to fail.
    -   we now directly parse `${CF_HOME}/.cf/config.json`,
        which is more stable
-   fix sorting only stdout and not `results.json` output file **(1.7.2)**
-   fix `cf-push-app` not providing valid "memory" property in dummy app POST **(1.7.4)**
    -   some versions of the cf api give "insufficient memory" error
        when memory property is missing.
    -   we now give dummy apps 1Mb memory

# Upgrading

-   To upgrade, use `sudo -E pip install --upgrade cf-boot`
-   To upgrade or revert to a specific version, use `sudo -E pip install --upgrade cf-boot==1.7.4`

As always, if something doesn't work as expected or for any new feature ideas, please let me know via this DL.

Thanks,

Ernesto