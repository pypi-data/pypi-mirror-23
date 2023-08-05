# Inputs

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="left" />

<col  class="left" />

<col  class="left" />
</colgroup>
<tbody>
<tr>
<td class="left">**arg name**</td>
<td class="left">**JSON type**</td>
<td class="left">**example**</td>
<td class="left">**description**</td>
</tr>


<tr>
<td class="left">uaa\_uri</td>
<td class="left">string</td>
<td class="left">"<https://079e5b8e-3d78-4140-b27c-ba038918ffea.predix-uaa.run.asv-pr.ice.predix.io>"</td>
<td class="left">uaa url</td>
</tr>


<tr>
<td class="left">uaa\_client\_secret</td>
<td class="left">string</td>
<td class="left">"******REMOVED******"</td>
<td class="left">uaa admin secret</td>
</tr>


<tr>
<td class="left">client\_payloads</td>
<td class="left">list</td>
<td class="left">client payloads as per the UAA API</td>
<td class="left">list of client payloads</td>
</tr>


<tr>
<td class="left">user\_payloads</td>
<td class="left">list</td>
<td class="left">user payloads as per the UAA API</td>
<td class="left">list of user payloads</td>
</tr>


<tr>
<td class="left">group\_payloads</td>
<td class="left">list</td>
<td class="left">group payloads as per the UAA API</td>
<td class="left">list of group payloads</td>
</tr>


<tr>
<td class="left">group\_mems</td>
<td class="left">list</td>
<td class="left">(see example below)</td>
<td class="left">group membership spec</td>
</tr>
</tbody>
</table>

For reference on the client, user, group payloads, consult the uaa REST api: <https://docs.cloudfoundry.org/api/uaa/>

## Examples:

-   create uaa clients for ui-app-hub's config manager

    {
       "uaa_uri": "https://079e5b8e-3d78-4140-b27c-ba038918ffea.predix-uaa.run.asv-pr.ice.predix.io",
       "uaa_client_secret": "***REMOVED***",
       "client_payloads" : [{
          "client_id": "cm_client_id",
          "client_secret": "***REMOVED***",
          "authorized_grant_types": ["client_credentials"],
          "autoapprove": ["openid"],
          "scope": ["uaa.none", "openid", "hub.config.read", "hub.config.write", "hub.config.admin"],
          "authorities": ["openid", "hub.config.read", "hub.config.write", "hub.config.admin"],
       }, {
          "client_id": "sb_client_id",
          "client_secret": "***REMOVED***",
          "authorized_grant_types": ["client_credentials"],
          "autoapprove": ["openid"],
          "scope": ["uaa.none", "openid", "hub.config.write"],
          "authorities": ["openid", "hub.config.write"],
       }, {
          "client_id": "***REMOVED***_client_id",
          "client_secret": "***REMOVED***",
          "authorized_grant_types": ["client_credentials"],
          "autoapprove": ["openid"],
          "scope": ["uaa.none", "openid", "hub.config.read"],
          "authorities": ["openid", "hub.config.read"],
       }, {
          "client_id": "acs_client_id",
          "client_secret": "acs_client_secret",
          "authorized_grant_types": ["client_credentials"],
          "autoapprove": ["openid"],
          "scope": ["uaa.none", "openid", "acs.policies.read", "acs.policies.write", "acs.attributes.read", "acs.attributes.write", "acs_zone"],
          "authorities": ["openid", "acs.policies.read", "acs.policies.write", "acs.attributes.read", "acs.attributes.write", "uaa.resource", "uaa.none", "acs_oauth_scope"],
       }]
    }

-   create a uaa with a sample test user, a sample group, and add the test user to the test group

    {
      "uaa_uri": "https://651b3f38-9af3-4784-8622-304cb9219164.predix-uaa.run.aws-usw02-pr.ice.predix.io",
      "user_payloads": [
        {
          "userName": "ernesto@ge.com",
          "password": "**REMOVED***",
          "name": {
            "givenName": "Ernesto",
            "familyName": "Ernesto"
          },
          "emails": [
            {
              "primary": true,
              "value": "ernesto@ge.com"
            }
          ]
        }
      ],
    
      "client_payloads": [
        {
          "authorized_grant_types": [
            "client_credentials",
            "authorization_code"
          ],
          "autoapprove": [
            "openid"
          ],
          "client_id": "framework-client",
          "scope": [
            "openid",
            "uaa.user",
            "uaa.none",
            "analytics.zones.74734c7a-bd0f-4e12-95d6-ca51526a8aff.user"
          ],
          "authorities": [
            "openid",
            "uaa.user",
            "uaa.none",
            "analytics.zones.74734c7a-bd0f-4e12-95d6-ca51526a8aff.user"
          ],
          "client_secret": "ernesto"
        }
      ],
      "uaa_client_secret": "ernesto",
      "group_payloads": [
        {
          "displayName": "analytics.zones.74734c7a-bd0f-4e12-95d6-ca51526a8aff.user"
        }
      ],
      "group_mems": [
        {
          "group": {
            "displayName": "analytics.zones.74734c7a-bd0f-4e12-95d6-ca51526a8aff.user"
          },
          "users": [
            {
              "userName": "ernesto@ge.com",
              "email": "ernesto@ge.com"
            }
          ]
        }
      ]
    }

# Output

    {}

# Idempotence

The script may be called any number of times. If a client/user/group exists, it is deleted and re-created, to ensure it has the specified payload.