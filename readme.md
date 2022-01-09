# Web application for calculating your mileage through the Space relative to the Sun

### Deployment:
1. build docker container
    docker build -t space_odometer_image .
    docker save -o space_odometer_image.tar 

2. Copy to the server and load
    scp space_odometer_image.tar user@host:/destination_path
    docker load -i /destination_path/space_odometer_image.tar

4. Run container
    docker run -dp 80:8088 space_odometer_image


