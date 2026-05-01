# wifi-flooder

A simple multi-threaded UDP flooding script written in Python for educational and sandbox testing purposes.

## Disclaimer
**WARNING**: 
> This script is strictly for educational purposes and testing within a controlled sandbox environment (such as Docker). Do not use this tool against any network or device without explicit authorization. The author is not responsible for any misuse or damage caused by this script.

## Requirements
- Python 3.10 or higher
- Docker (for sandbox environment)

## Usage

### Running in Docker Sandbox
1. Create a network:
   ```bash
   docker network create --driver bridge sandbox-network
   ```

    Run target container:
    ```bash
    docker run -d --name target-victim --network sandbox-network nginx
    ```
    
    Run attacker container:
    ```bash
    docker run -it --rm --name attacker-node --network sandbox-network python:3.10 /bin/bash
    ```

    Write the script as main.py then execute the script
   ```bash
   python3 main.py
   ```
