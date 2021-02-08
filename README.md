# django-keycloak-sample
Sample repository for a django and keycloak implementation. 

## Repositories needed 
The repositories that we need for this to work are the following:
1. [Django](https://github.com/django)
2. [Keycloak extension for python, version 3.0.1rc1](https://github.com/chunky-monkeys/keycloak-client)

To install these repositories set up your virtual environment and then install.

`pipenv install Django keycloak==3.0.1rc1`

## Running keycloak server and setting up the client
Run the `standalone.sh` file of the keycloak server to set up the environment.

1. Go into the Realm you want to set up for your Django application
2. Create a Client for the django application 
![create client](https://github.com/jerojero/django-keycloak-sample/blob/main/tutorial/images/createclient.png)
3. Change `Access Type` to `confidential`
4. Switch `Authorization Enabled` to `ON`
![options](https://github.com/jerojero/django-keycloak-sample/blob/main/tutorial/images/confidential.png)
5. Save Changes
6. Go into the Installation Tab, select format as `Keycloak OIDC JSON`, download and replace the file in the Django app.

## Modifying the `keycloak` package to access roles
Locate the package (if you use linux and pipenv it should be in `~/.local/share/virtualenvs/<env name>/<python version>/site-packages/keycloak/`. We have to modify the file that is in `extensions/django.py`.

Jump into line 43 near the `# fetch user info` comment. And add the following lines:

```python
user_token = self.kc.rpt(access_token)
decoded_token = self.kc.decode(user_token["access_token"])
request.session["decoded_token"] = decoded_token
```
![modifications](https://github.com/jerojero/django-keycloak-sample/blob/main/tutorial/images/modifications.png)

This will let us acccess the token from the `request` on the django views. We could modify these lines further to give access just to the roles or other user data. This token is refreshed when the user logs in/out. So changes in permission require the user to log in back again to take effect.

## This example
In this django example we need users with the roles `normaluser`, `moderator` and `administrator`. These roles will make the paragraphs in `test` be different for different kinds of users. Use keycloak to manage roles. 

These roles are configured, for this example, to be on realm-level. But it is also possible to access the client-level roles if necessary. The modifications to the package could incorporate that. 
