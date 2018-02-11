# papa1024-ui

## Docker deploay and run
```
sudo docker build -t papa1024-ui .
sudo docker run -i -t -p 8888:8888  papa1024-ui
```

## Pre-Development

### install tornado
```
pip install tornado
```

### motor: 
An asynchronous MongoDB driver for Python and Tornado

HomePage: https://github.com/mongodb/motor/

```
pip install motor
```

### tornado-redis
An asynchronous Redis driver for Python and Tornado

HomePage: https://github.com/leporo/tornado-redis

```
pip install tornado-redis
```

### momoko
An asynchronous postgre driver for Python and Tornado

HomePage: https://github.com/FSX/momoko

```
pip install momoko
```
## Development

### Generate requirements.txt
```
pip install pipreqs

cd project-root-path
pipreqs ./
```

### Recover project
```
pip install -r requirements.txt
```