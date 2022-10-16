# Phoenix2

## Installation

at root create your environment with
```bash
virtualenv [envname]
```
then run your env
```bash
source [envname]/bin/activate
```
* install django requirement
```bash
pip install -r requirements.txt
```
* go to tailwind folder
```bash
cd tailwind
```
* update npm package 
* =========== only update npm in [tailwind] folder ===========
```bash
npm i
npm upgrade
```

## Start dev
start environment
```bash
source [envname]/bin/activate
```
[First Terminal] run django server
```bash
python manage.py runserver 
```
[Second Terminal] run tailwind server
```bash
cd tailwind
npm run start
```

## Static file

Static file is store in 
tailwind/static
can use in template with

`{% load webpack_loader static %}`
`<img src="{% static 'static/images/webpack.png' %}"/>`


## Available Scripts

In the project directory, you can run:

### `npm run start`

`npm run start` will launch a server process, which makes `live reloading` possible.

If you change JS or SCSS files, the web page would auto refresh after the change. Now the server is working on port 9091 by default, but you can change it in `webpack/webpack.config.dev.js`

### `npm run watch`

run webpack in `watch` mode.

### `npm run build`

[production mode](https://webpack.js.org/guides/production/), Webpack would focus on minified bundles, lighter weight source maps, and optimized assets to improve load time.


