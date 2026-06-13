# 1. Use an official lightweight Python image from the Docker Hub
FROM python:3.10-slim

# 2. Set environment variables to keep Python from writing pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Install system dependencies that might be needed to compile packages (like bcrypt)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy only the requirements file first to take advantage of Docker's caching mechanism
COPY requirements.txt .

# 6. Install the Python dependencies inside the container
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 7. Copy the rest of your application code (including your src/ folder and app.py)
COPY . .

# 8. Expose the port that Streamlit runs on
EXPOSE 8501

# 9. Set the command to run your application when the container starts
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]