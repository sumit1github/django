
sudo apt-get install default-jdk


'''find the latest version change it in the url 8.11.2'''
wget https://downloads.apache.org/lucene/solr/8.11.2/solr-8.11.2.tgz


#extract the folder and go inside of it
tar xzf solr-8.11.2.tgz solr-8.11.2/bin/install_solr_service.sh --strip-components=2

#run this command to install
sudo bash ./install_solr_service.sh solr-8.11.2.tgz

#varify solr installation by 

localhost:8983


#---------------------------------------------- create solr core -------------------------------

sudo su - solr -c "/opt/solr/bin/solr create_core -c core_name"

systemctl restart solr

#---------------------------------------------- delete solr core -------------------------------

sudo su - solr -c "/opt/solr/bin/solr delete -c core_name"

sudo rm -rf /var/solr/data/core_name

systemctl restart solr