# GAuth

## Certificate Authentication for Google Forms

### Setup

Copy gauth/settings.example.py to gauth/settings.py and fill in the places
marked "TODO."

Note that GAuth expects that the server will handle certificate authentication.
It expects the `SSL_CLIENT_S_DN_Email` field of the request to hold the user's
email address. You can change the field name in `redirector/certs.py`. This
should work out-of-the-box on scripts.mit.edu.

### Contributing

Fork the repo on GitHub, make your changes, and submit a pull request.

### License

GAuth is licensed under the MIT license, included in `LICENSE.txt`. Resources
used, including those acknowledged below, may have their own licenses.

### Acknowledgements

* [Django](https://www.djangoproject.com/)
* [Bootstrap](http://twitter.github.com/bootstrap/)
* [Hydrogen666, "Flock Wallpaper Pattern"](http://hydrogen666.deviantart.com/art/Flock-Wallpaper-Pattern-89953817)
* [Renee Ramsey-Passmore, from The Noun Project](http://thenounproject.com/noun/fleur-de-lis/#icon-No5419)

### Author

[Ben Weissmann](mailto:bsw@mit.edu)
