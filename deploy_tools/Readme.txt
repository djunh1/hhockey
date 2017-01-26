Objective:  Provide basic overview for deploying this application onto AWS.


Prerequisites:

(1) Ensure EC2 and RDS instances are operating.  Make sure the EC2 instance can connect to the RDS, and that the RDS
is private.  Both instances must be a part of the same VPC.

(2) Supervisor is installed : sudo easy_install suypervisor.

(3) Ensure ownership to run files is for user of EC2 instance.

(4) Install superlance - sudo pip install superlance.  Ensure sendmail is installed ( sudo yum install sendmail)


Precautions:

(1) Installing python requirements using pip install -r requirements.txt often yields dependency errors depending on
the Linux distro.
    (a) mysqlclient (Ubuntu) -  dependencies needed are python-dev.  Run the following command to get them installed
        sudo apt-get -y install gcc make build-essential libssl-dev libffi-dev python-dev
    (b) mysqlclient (Centos) -  python-devel needed as dependency.  Search yum repo (yum search python3 |grep level).
      Install  the python34-devel package.
    (c) rjsmin, and rcssmin need to be installed "without C extensions".  from the source folder:
        (I) ../virtualenv/bin/pip install rjsmin --install-options="--without-c-extensions"
        (II) ../virtualenv/bin/pip install rcssmin --install-options="--without-c-extensions"


Procedure:

SECTION 1 -  FABRIC DEPLOYMENT

(1) Use FABRIC to deploy the application. (located in deploy_tools)
    fab deploy:host=ec2-user@ec2-35-166-188-189.us-west-2.compute.amazonaws.com.  Modify host as needed.

(2) Log into EC2 instance.
    ssh -i "$HOME/.ssh/hopewell-hockey-kp.pem" ec2-user@ec2-35-166-188-189.us-west-2.compute.amazonaws.com

(3) Set up Environment
    (a) Ubuntu - sudo apt-get install nginx git python3 python3-pip
    (b) Centos - sudo yum install nginx git python3 python3-pip
    (c) sudo pip3 install virtualenv

(4)  MODIFY nginx.template.conf:
    sed "s/SITENAME/hopewellhockey.com/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/nginx.conf

(5) Activate File:  sudo ln -s ../sites-available/hopewellhockey.com /etc/nginx/nginx.conf

(6) Replace sitename script to run the server
    sed "s/SITENAME/staging-hopewellhockey.com/g" gunicorn-start.sh | sudo tee gunicorn-start.sh

(7) Reload nginx if required to update the settings: sudo service nginx restart

(8) Run the application
    (a) Change permission of hhockey/deploy tools (if needed):
        sudo chmod 775 /home/ec2-user/sites/staging-hopewellhockey.com/source/deploy_tools
    (b) MODIFY /deploy_tools/supervisord.conf :
        sed "s/SITENAME/staging-hopewellhockey.com/g" supervisord.conf | sudo tee supervisord.conf
    (c) Find supervisor bin and run it: supervisord -c supervisord.conf -n



SECTION 2 - Installing Jenkins

   Pre-req - As root ( sudo su -) update yum ( yum update)
            yum install -y docker nginx git

(1) Install java sudo yum -y install java

(2) Download Jenkins via red hat repo
    sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo

(3) Import a verification key using RPM :
    sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key

(4) Install Jenkins
    sudo yum install jenkins

(5) Find the service and start jenkins:
    (a) To find the service : yum whatprovides service
    (b) start Jenkins (as root) : service jenkins start

Section 3 -Covers various commands to restart services.  run as the default user (ec2-user)

(1) To restart nginx:
     sudo service nginx restart

(2)  TEMP , to pull after changing the deploy tools, reset first than configure scripts:
    git reset HEAD --hard

(3) To stop gunicorn script:
      (a)  Stop the service : pkill gunicorn
      (b) Check the file can be run : ls -l gunicorn-start.sh
      (c) change ownership : chmod 777 gunicorn-start.sh
      (d) Run it in the current directory: ./gunicorn-start.sh   (permission issues should be ok)

(4) To Restart supervisord:  NOT WORKING!!
    This file doesn't run yet.  Make sure the command works.  It likely needs sudo, or to change owner of the
    gunicorn file






