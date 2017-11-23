Pre-requiste
--
Install Python, DJango, WSGI and NGINX

To run the application
use below command

Perferred way - uwsgi --ini mydjangosite_wsgi.ini

Other ways -- 
uwsgi --socket mydjangosite.sock --wsgi-file mydjangosite/test.py
, uwsgi --socket mydjangosite.sock --module mydjangosite.wsgi

URL
--
http://mydjango.com:8000/


Follow below URL for reference

http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html#before-you-start-setting-up-uwsgi


To run the application
----
pip install django-sslserver
python manage.py runsslserver 8001 --certificate certs/abc_cert_1.pem --key certs/abc_selfsigned_1.key
