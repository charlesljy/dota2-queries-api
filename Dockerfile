# Sets the base image for subsequent instructions
FROM python:3.9

# Sets the working directory in the container  
WORKDIR /app

# # Copies the files to the working directory
# COPY form.html /app/form.html

# Copies the dependency files to the working directory
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copies everything to the working directory
COPY . /app

# Command to run on container start    
CMD [ "python" , "./app.py" ]