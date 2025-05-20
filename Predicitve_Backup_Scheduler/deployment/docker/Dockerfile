# Assuming your Dockerfile starts with a base image, e.g.:
FROM python:3.10-slim-buster

# Set the working directory inside the container
# This will be the root of your application inside the container
WORKDIR /app

# Copy your requirements.txt and install dependencies
# This is usually done before copying all code to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- ADD THIS LINE TO COPY YOUR MODELS FOLDER ---
# Assuming 'models' is a sibling of 'deployment' and 'app' from the context
# The '.' at the end of 'docker build' command indicates the build context.
# If you are running `docker build -f deployment/docker/Dockerfile .`
# from `Predicitve_Backup_Scheduler`, then 'models' is directly available.
COPY C:/Users/Ravik/autonomous-index-tuner/Predicitve_Backup_Scheduler/models

# Copy your 'app' folder (and other code)
COPY C:/Users/Ravik/autonomous-index-tuner/Predicitve_Backup_Scheduler/app

# If you have other project-level code that needs to be copied:
# COPY ../../<other_project_folder> /app/<other_project_folder>

# Expose the port your FastAPI app runs on
EXPOSE 80

# Command to run your FastAPI application with Uvicorn
CMD ["uvicorn", "app.fastapi_app:app", "--host", "0.0.0.0", "--port", "80"]