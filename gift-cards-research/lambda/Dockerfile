# AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.11

# Copy and install deps
COPY requirements.txt  .
RUN pip install --no-cache-dir -r requirements.txt

# Copy function code
COPY handler.py auth.py fetch.py ${LAMBDA_TASK_ROOT}/

# Run the handler
CMD ["handler.lambda_handler"]
