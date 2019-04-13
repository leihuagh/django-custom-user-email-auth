# base image to be used
FROM python:3.6
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1


# Set the working directory to the created dir
WORKDIR /code

# add the requiremnets file to the working dir
COPY requirements.txt /code/

#instal the requirements (install before adding rest of code to avoid rerunning this at every code change-built in layers)
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /music_service
COPY . /code/


EXPOSE 8000

#run the service docker app
CMD /code/start.sh