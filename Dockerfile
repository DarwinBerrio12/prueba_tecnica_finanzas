# Set the base image
FROM python:3.10.9
 
# Create a new directory to work in
RUN mkdir /app
 
# Set the working directory
WORKDIR /app
 
# Copy the main.py file from the host to the container
COPY . .
 
# Install dependencies
COPY requirements.txt .
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
RUN apt-get install tzdata -y
#RUN pip install -r requirements.txt
ENV TZ=America/Bogota
# Set the entrypoint
ENTRYPOINT ["python", "main.py"]