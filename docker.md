# install 
>Step 1: Update the Package Repository

    sudo apt update

> Step 2: Install Prerequisite Packages
    
    sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

> Step 3: Add GPG Key
    
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

> Step 4: Add Docker Repository
    
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

> Step 5: Specify Installation Source
    
    apt-cache policy docker-ce

> Step 6: Install Docker
    
    sudo apt install docker-ce -y

> Step 7: Check Docker Status
    
    sudo systemctl status docker


# commands