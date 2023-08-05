Provides a script to create an event hub instance
along with pub/sub clients with appropriate scopes.

-   Install cf-boot
    
        sudo -E pip install cf-boot
-   Create sample-environment.json with environment information
    
        {
         "CF_TARGET": "https://api.system.asv-pr.ice.predix.io",
         "CF_USER": "ernesto.alfonsogonzalez@ge.com",
         "CF_PASSWORD": "***REMOVED***",
         "CF_ORG": "HUBS",
         "CF_SPACE": "poc",
         "CF_SPACE_UAA": "sandbox",
        
         "event-hub-instance-name": "event-hub-audit-poc",
         "uaa_instance_name": "event-hub-audit-uaa-poc",
         "uaa_admin_secret": "ernesto",
        
         "event_hub_subscribe_client_id": "eh-subscribe",
         "event_hub_subscribe_client_secret": "eh-subscribe-secret",
        
         "event_hub_publish_client_id": "eh-publish",
         "event_hub_publish_client_secret": "eh-publish-secret"
        }

-   Run bootstrap
    
        cf-boot event-hub-boot.json -i sample-free-vars.json