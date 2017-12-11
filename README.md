# Flask Waiter Caller

Flask Waiter Caller Project taken from Flask By Example Ebook

---

1. Install Requirements
```bash
$ pip install -r requirements.txt
```

2. Install Apache2, mod_wsgi, Git
```bash
$ sudo apt-get install apache2 libapache2-mod-wsgi git
```

3. Clone this repo to `/var/www/` directory
```bash
$ git clone https://github.com/repodevs/flask-waitercaller.git /var/www/flask-waitercaller
```

4. Copy this `apache2/waitercaller.conf` config to `site-available` apache2 directory
```bash
$ sudo cp apache2/waitercaller.conf /etc/apache2/sites-available/
```

5. Enable configuration and disable default apache2 configuration
```bash
# disable default conf, or disable other conf
$ sudo a2dissite 000-default.conf
$ sudo a2ensite waitercaller.conf
$ sudo service apache2 reload
```

6. Open in your browser [http://127.0.0.1](http://127.0.0.1)


---

## Others


If using mongo database

1. Install Mongo Database
```bash
$ sudo apt-get install -y mongodb-org
```

2. Install `pymongo` package
```bash
$ pip install pymongo
```

3. Create Index In Mongo
```bash
$ python create_mongo_indices.py
```

4. Change `config.py` from `test=True` to `test=False`

5. Run It!
```bash
$ python waitercaller.py
```
