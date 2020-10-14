# talking_pythons
Two python programs talking to each other through RabbitMQ


# Setup
- To get RabbitMQ started `docker-compose up`
- Using RabbitMQ admin [http://localhost:15673/](http://localhost:15673/) 
- Install and activate virtualenv `python3 -m venv venv`
- Install requirements `pip install -r requirements.txt`

# Environmental variables
The following environmental variables are required:
- `export PYTHONPATH=.`
- `export RABBIT_QUEUE='hello'`
- `export CLOUDAMQP_URL='amqp://guest:guest@localhost:9672'`

# Run
Now start the send.py program in one terminal and receive.py program in another. Then see programs talking.
- `python3 app/send.py`
- `python3 app/receive.py`
