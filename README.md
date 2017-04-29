This repo was born as answer to [this stackoverflow question](http://stackoverflow.com/questions/38415209/solved-daphne-server-cannot-connect-with-websockets-on-https)

1) create app on openshift from DIY cartridge through admin panel or
`$ rhc app create <exampleapp> diy-0.1`
2) add redis cartridge https://github.com/gerardogc2378/openshift-redis-cart
don't forget to set redis password) with:
`$ rhc set-env OPENSHIFT_REDIS_PASSWORD=my-secret-redis-pass --app=<exampleapp>`
3) clone your freshly created app skeleton from openshift and cd to <exampleapp>
 (you don't have to clone repo from openshift if you were used CLI tool)
4) merge this repo with yours
`$ git remote add upstream -m master https://github.com/StevenLudwig/openshift-diy-daphne.git`
`$ git pull -s recursive -X theirs upstream master`
`$ git push`

This will download and install python-3.4, setuptools + packages listed in requirements.txt
After quite long installation (will run only once), it will run daphne + worker (on redis based layer) 
handling simple ping-pong websocket app called djangoproject/djangoapp:
you will see simple input field which will send message to server through websocket and logs response.

Repo is done for testing/developing purposes as openshift doesn't ask 
for credit card or another payment info (opposite to heroku) so, for me, it is more confident.
Feel free to add Nginx and other stuff as author of [stackoverflow question](http://stackoverflow.com/questions/38415209/solved-daphne-server-cannot-connect-with-websockets-on-https), mentioned above, explains.

Have a nice day and be happy!
