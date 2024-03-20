# API Information Storage

This repository c ontains the necessary tools and scripts to build a library of API information, automatically aggregating data from various API repositories. By requiring developers to include an `api_info.json` in the root of their repositories, this system can dynamically compile and store API data into a DynamoDB table for easy access and management.

The purpose of this setup is to automate the process of collecting and storing API information. By having a standardized api_info.json in each API repository, this system can fetch and insert the necessary information into a DynamoDB table. This process simplifies the management and discovery of API resources, making it easier for developers to find and use the APIs they need.

## Repository Structure

The repository is structured as follows:

- `Dockerfile`: A Dockerfile to containerize the Python application.
- `README.md`: This documentation.
- `api_info.json`: The JSON file containing API information to be inserted into DynamoDB.
- `app/`: Contains the Python script (`app.py`) and the requirements file (`requirements.txt`).
- `terraform/`: Contains Terraform configurations to deploy the DynamoDB table.

## Deployment

### Terraform Deployment

1. **Initialize Terraform**

   Navigate to the `terraform/` directory and run:

   ```sh
   terraform init
   ```

2. **Apply Terraform Configuration**

    Still in the terraform/ directory, execute:

    ```sh
    terraform plan -out=plan.out
    terraform apply plan.out
    ```
    You'll be prompted to review the proposed changes. Type yes to proceed with the deployment of the DynamoDB table.
   ![tf.png](images%2Ftf.png)
### Docker Build
1. **Build the Docker Image**

    From the root of the repository, build the Docker image using:

    ```sh
    docker build -t api_information_storage .
    ```
    This command creates a Docker image named api_information_storage, containing the Python application and its dependencies.
   ![docker_build.png](images%2Fdocker_build.png)
### Running the Container
1. **Run the Docker Container**

    To run the container, use the following command:

    ```sh
    docker run -v <LOCAL_AWS_CREDENTIALS_LOCATION>.aws:/root/.aws:ro -e AWS_PROFILE=<LOCAL_AWS_PROFILE> api_information_storage
    ``` 
   This command does a few important things:
    ![docker_run.jpg](images%2Fdocker_run.jpg)
   * `-v <LOCAL_AWS_CREDENTIALS_LOCATION>/.aws:/root/.aws:ro` mounts your AWS credentials from your host machine into the container. This is necessary for the application to access AWS services using your credentials.
   * `-e AWS_PROFILE=<LOCAL_AWS_PROFILE>` sets the environment variable AWS_PROFILE inside the container. This specifies which AWS profile to use for authentication, allowing the script to use the correct credentials.
   * `api_information_storage` is the name of the Docker image to run.

![stored_info.jpg](images%2Fstored_info.jpg)
### Why Declare and Mount
* **Declaring Environment Variables:** Environment variables like TABLE_NAME and AWS_PROFILE are declared to customize the container's behavior without hardcoding sensitive information or configuration details into the Docker image. This approach enhances security and flexibility.
* **Mounting AWS Credentials:** Mounting the .aws directory as a read-only volume ensures that the container can authenticate with AWS services using your credentials without including them in the Docker image. This method keeps your credentials secure while allowing the application to interact with AWS resources.

Goal of the Repository
The ultimate goal is to automate the creation of a comprehensive library of API information. This library will be automatically updated from developer contributions, significantly reducing manual overhead and improving consistency across the organization's APIs. By centralizing API information in a DynamoDB table, developers can more easily access, manage, and discover APIs, facilitating better integration and utilization of available services.