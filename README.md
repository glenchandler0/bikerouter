# bikerouter

## Tracking setup steps
- lsb_release -a: ubuntu 22.04 jammy

### Docker
Remove old verions
`sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc docker-buildx podman-docker containerd runc | cut -f1)`

```
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```

Actually get the repository
`sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

Verify Running:
`sudo systemctl status docker`

Start with:
`sudo systemctl start docker`

Hello world:
`sudo docker run hello-world`

Add user to docker group
`sudo groupadd docker`
`sudo usermod -aG docker $USER`
`newgrp docker`

## Starting PostGres
1. Setup `compose.yaml`
2. Navigate to folder with `compose.yaml`
3. Run `docker compose up -d`
    - Stop with: `docker compose stop`
4. Health check: `docker compose ps`
5. Connect: `docker compose exec db psql -U bikerouter -d bikerouter`